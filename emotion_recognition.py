import pickle
import cv2
import numpy as np
import torch
from tensorflow.keras.models import Sequential

from face_detection import capture_face_from_frame
from train.train_sklearn_emotion.utils import get_face_landmarks
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from deepface import DeepFace

# 定义情绪标签
emotions = ['happy', 'sad', 'surprised']


# 加载模型
def load_models():
    with open('models/svm_model.pkl', 'rb') as f:
        model_pkl = pickle.load(f)

    model_h5 = Sequential()
    model_h5.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
    model_h5.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model_h5.add(MaxPooling2D(pool_size=(2, 2)))
    model_h5.add(Dropout(0.25))

    model_h5.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model_h5.add(MaxPooling2D(pool_size=(2, 2)))
    model_h5.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    model_h5.add(MaxPooling2D(pool_size=(2, 2)))
    model_h5.add(Dropout(0.25))

    model_h5.add(Flatten())
    model_h5.add(Dense(1024, activation='relu'))
    model_h5.add(Dropout(0.5))
    model_h5.add(Dense(3, activation='softmax'))

    model_h5.load_weights('models/model.h5')

    return model_pkl, model_h5


# 使用 model.pkl 进行情绪识别
def recognize_emotion_pkl(frame):
    # 初始化模型
    model_pkl, model_h5 = load_models()
    face = capture_face_from_frame(frame)
    face_landmarks = get_face_landmarks(face, draw=False, static_image_mode=True)
    if face_landmarks:
        prediction = model_pkl.predict([face_landmarks])
        print(emotions[int(prediction[0])])
        return emotions[int(prediction[0])]
    return None


# 使用 model.h5 进行情绪识别
def recognize_emotion_h5(frame):
    # 初始化模型
    model_pkl, model_h5 = load_models()
    face = capture_face_from_frame(frame)
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(gray, (48, 48)), -1), 0)
    prediction = model_h5.predict(cropped_img)
    maxindex = int(np.argmax(prediction))
    torch.cuda.empty_cache()
    print(emotions[maxindex])
    return emotions[maxindex]


def recognize_emotion_deepface(frame):
    result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    print(result[0]['dominant_emotion'])
    return result[0]['dominant_emotion']


def recognize_emotion(face_image, model_type='pkl'):
    if model_type == 'pkl':
        return recognize_emotion_pkl(face_image)
    elif model_type == 'h5':
        return recognize_emotion_h5(face_image)
    elif model_type == 'deepface':
        return recognize_emotion_deepface(face_image)
    else:
        raise ValueError("Invalid model type. Choose 'pkl','h5' or 'deepface'.")
