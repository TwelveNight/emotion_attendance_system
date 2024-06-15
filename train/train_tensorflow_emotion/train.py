import numpy as np  # 导入NumPy库，用于数值计算
import os  # 导入os库，用于文件和目录操作
import matplotlib.pyplot as plt  # 导入Matplotlib库，用于绘图
from tensorflow.keras.models import Sequential  # 导入Sequential模型
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D  # 导入神经网络层
from tensorflow.keras.optimizers import Adam  # 导入Adam优化器
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # 导入ImageDataGenerator用于数据增强

# 设置TensorFlow的日志级别，减少不必要的警告信息
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 获取当前文件的目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# 定义数据目录
train_dir = os.path.join(base_dir, 'data/train')
val_dir = os.path.join(base_dir, 'data/test')

# 定义模型保存目录和路径
model_dir = os.path.join(base_dir, '../../models')
model_path = os.path.join(model_dir, 'model_test.h5')

# 定义绘制模型训练历史的函数
def plot_model_history(model_history, step=5):
    """
    根据模型训练历史绘制准确率和损失曲线
    """
    fig, axs = plt.subplots(1, 2, figsize=(15, 5))
    # 绘制准确率曲线
    axs[0].plot(range(1, len(model_history.history['accuracy']) + 1, step), model_history.history['accuracy'][::step])
    axs[0].plot(range(1, len(model_history.history['val_accuracy']) + 1, step),
                model_history.history['val_accuracy'][::step])
    axs[0].set_title('Model Accuracy')
    axs[0].set_ylabel('Accuracy')
    axs[0].set_xlabel('Epoch')
    axs[0].set_xticks(np.arange(1, len(model_history.history['accuracy']) + 1, step))
    axs[0].legend(['train', 'val'], loc='best')
    # 绘制损失曲线
    axs[1].plot(range(1, len(model_history.history['loss']) + 1, step), model_history.history['loss'][::step])
    axs[1].plot(range(1, len(model_history.history['val_loss']) + 1, step), model_history.history['val_loss'][::step])
    axs[1].set_title('Model Loss')
    axs[1].set_ylabel('Loss')
    axs[1].set_xlabel('Epoch')
    axs[1].set_xticks(np.arange(1, len(model_history.history['loss']) + 1, step))
    axs[1].legend(['train', 'val'], loc='best')
    fig.savefig('plot.png')  # 保存绘图
    plt.show()

# 定义训练和验证数据的数量、批次大小和训练周期
num_train = 15216
num_val = 3852
batch_size = 64
num_epoch = 50

# 定义数据生成器，用于从目录中读取图像数据并进行预处理
train_datagen = ImageDataGenerator(rescale=1. / 255)
val_datagen = ImageDataGenerator(rescale=1. / 255)

# 定义训练数据生成器
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(48, 48),
    batch_size=batch_size,
    color_mode="grayscale",
    class_mode='categorical')

# 定义验证数据生成器
validation_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(48, 48),
    batch_size=batch_size,
    color_mode="grayscale",
    class_mode='categorical')

# 创建卷积神经网络模型
model = Sequential()

# 添加卷积层、激活层、池化层和Dropout层
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 展平层和全连接层
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))  # 输出层，有3个类别，使用softmax激活函数

# 编译并训练模型
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.0001, decay=1e-6),
              metrics=['accuracy'])
model_info = model.fit(
    train_generator,
    steps_per_epoch=num_train // batch_size,
    epochs=num_epoch,
    validation_data=validation_generator,
    validation_steps=num_val // batch_size)

# 绘制训练过程中的准确率和损失曲线
plot_model_history(model_info)

# 检查模型保存目录是否存在，如果不存在则创建
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# 保存模型权重
model.save_weights(model_path)
