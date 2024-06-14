# 安装软件包之前请先看这个

## 请先建一个python虚拟环境，建议用conda,以下以conda为例

### 1. install tensorflow(或者用linux,具体请看官方文档)
```bash
conda install -c conda-forge cudatoolkit=11.8 cudnn=8.1.0
# Anything above 2.10 is not supported on the GPU on Windows Native
python -m pip install "tensorflow<2.11"
# Verify the installation:
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```
### 2. install pytorch
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 3. install other packages
```bash
pip install -r requirements.txt
```

### 4. misc
- 由于开发过程中没有一次性搭建好所有环境，使用了一些不同的库，所以可能会有一些冲突，如果有冲突请按照提示更换版本
- requirements.txt中也许没有包含所有的库，如果有缺失请自行安装