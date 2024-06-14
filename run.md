# 安装软件包之前请先看这个

## 请先建一个python虚拟环境，建议用conda,以下以conda为例

### 1. install tensorflow(这里用windows本机跑，其它选择请看[官方文档](https://www.tensorflow.org/install/pip#:~:text=conda%20install%20%2Dc%20conda%2Dforge%20cudatoolkit%3D11.2%20cudnn%3D8.1.0%0A%23%20Anything%20above%202.10%20is%20not%20supported%20on%20the%20GPU%20on%20Windows%20Native%0Apython%20%2Dm%20pip%20install%20%22tensorflow%3C2.11%22%0A%23%20Verify%20the%20installation%3A%0Apython%20%2Dc%20%22import%20tensorflow%20as%20tf%3B%20print(tf.config.list_physical_devices(%27GPU%27)))
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
- [如果有问题，请提issue](https://github.com/TwelveNight/emotion_attendance_system)

### 5. 所有软件包如下,实在不能跑请对比以下软件包版本
```bash
# packages in environment at D:\IDE\python\miniconda\envs\emotion_attendance_system:
#
# Name                    Version                   Build  Channel
absl-py                   2.1.0                    pypi_0    pypi
antlr4-python3-runtime    4.9.3                    pypi_0    pypi
anyio                     4.4.0                    pypi_0    pypi
argon2-cffi               23.1.0                   pypi_0    pypi
argon2-cffi-bindings      21.2.0                   pypi_0    pypi
arrow                     1.3.0                    pypi_0    pypi
asttokens                 2.4.1                    pypi_0    pypi
astunparse                1.6.3                    pypi_0    pypi
async-lru                 2.0.4                    pypi_0    pypi
attrs                     23.2.0                   pypi_0    pypi
babel                     2.15.0                   pypi_0    pypi
beautifulsoup4            4.12.3                   pypi_0    pypi
blas                      1.0                         mkl  
bleach                    6.1.0                    pypi_0    pypi
blinker                   1.8.2                    pypi_0    pypi
bottleneck                1.3.7           py310h9128911_0  
brotli                    1.0.9                h2bbff1b_8  
brotli-bin                1.0.9                h2bbff1b_8  
brotli-python             1.0.9           py310hd77b12b_8  
bzip2                     1.0.8                h2bbff1b_6  
ca-certificates           2024.6.2             h56e8100_0    conda-forge
cachetools                5.3.3                    pypi_0    pypi
certifi                   2024.2.2        py310haa95532_0  
charset-normalizer        2.0.4              pyhd3eb1b0_0  
click                     8.1.7                    pypi_0    pypi
colorama                  0.4.6                    pypi_0    pypi
comm                      0.2.2                    pypi_0    pypi
contourpy                 1.2.0           py310h59b6b97_0
cuda-cccl                 12.4.127                      0    nvidia
cuda-cudart               11.8.89                       0    nvidia
cuda-cudart-dev           11.8.89                       0    nvidia
cuda-cupti                11.8.87                       0    nvidia
cuda-libraries            11.8.0                        0    nvidia
cuda-libraries-dev        11.8.0                        0    nvidia
cuda-nvrtc                11.8.89                       0    nvidia
cuda-nvrtc-dev            11.8.89                       0    nvidia
cuda-nvtx                 11.8.86                       0    nvidia
cuda-profiler-api         12.4.127                      0    nvidia
cuda-runtime              11.8.0                        0    nvidia
cudatoolkit               11.8.0              h09e9e62_13    conda-forge
cudnn                     8.1.0.77             h3e0f4f4_0    conda-forge
cycler                    0.11.0             pyhd3eb1b0_0
debugpy                   1.8.1                    pypi_0    pypi
decorator                 5.1.1                    pypi_0    pypi
deepface                  0.0.91                   pypi_0    pypi
defusedxml                0.7.1                    pypi_0    pypi
dlib                      19.22.99                 pypi_0    pypi
exceptiongroup            1.2.1                    pypi_0    pypi
executing                 2.0.1                    pypi_0    pypi
face-recognition          1.3.0                    pypi_0    pypi
face-recognition-models   0.3.0                    pypi_0    pypi
fastjsonschema            2.19.1                   pypi_0    pypi
filelock                  3.14.0                   pypi_0    pypi
fire                      0.6.0                    pypi_0    pypi
flask                     3.0.3                    pypi_0    pypi
flask-cors                4.0.1                    pypi_0    pypi
flatbuffers               24.3.25                  pypi_0    pypi
fonttools                 4.51.0          py310h2bbff1b_0
fqdn                      1.5.1                    pypi_0    pypi
freetype                  2.12.1               ha860e81_0
fsspec                    2024.5.0                 pypi_0    pypi
gast                      0.4.0                    pypi_0    pypi
gdown                     5.2.0                    pypi_0    pypi
gmpy2                     2.1.2           py310h7f96b67_0
google-auth               2.29.0                   pypi_0    pypi
google-auth-oauthlib      0.4.6                    pypi_0    pypi
google-pasta              0.2.0                    pypi_0    pypi
grpcio                    1.64.0                   pypi_0    pypi
gunicorn                  22.0.0                   pypi_0    pypi
h11                       0.14.0                   pypi_0    pypi
h5py                      3.11.0                   pypi_0    pypi
httpcore                  1.0.5                    pypi_0    pypi
httpx                     0.27.0                   pypi_0    pypi
icc_rt                    2022.1.0             h6049295_2
icu                       73.1                 h6c2663c_0
idna                      3.7             py310haa95532_0
intel-openmp              2021.4.0                 pypi_0    pypi
ipykernel                 6.29.4                   pypi_0    pypi
ipython                   8.24.0                   pypi_0    pypi
isoduration               20.11.0                  pypi_0    pypi
itsdangerous              2.2.0                    pypi_0    pypi
jedi                      0.19.1                   pypi_0    pypi
jinja2                    3.1.4           py310haa95532_0
joblib                    1.4.0           py310haa95532_0
jpeg                      9e                   h2bbff1b_1
json5                     0.9.25                   pypi_0    pypi
jsonpointer               2.4                      pypi_0    pypi
jsonschema                4.22.0                   pypi_0    pypi
jsonschema-specifications 2023.12.1                pypi_0    pypi
jupyter-client            8.6.2                    pypi_0    pypi
jupyter-core              5.7.2                    pypi_0    pypi
jupyter-events            0.10.0                   pypi_0    pypi
jupyter-lsp               2.2.5                    pypi_0    pypi
jupyter-server            2.14.1                   pypi_0    pypi
jupyter-server-terminals  0.5.3                    pypi_0    pypi
jupyterlab                4.2.1                    pypi_0    pypi
jupyterlab-pygments       0.3.0                    pypi_0    pypi
jupyterlab-server         2.27.2                   pypi_0    pypi
keras                     2.10.0                   pypi_0    pypi
keras-facenet             0.3.2                    pypi_0    pypi
keras-preprocessing       1.1.2                    pypi_0    pypi
kiwisolver                1.4.4           py310hd77b12b_0
krb5                      1.20.1               h5b6d351_0
lapx                      0.5.9                    pypi_0    pypi
lcms2                     2.12                 h83e58a3_0
lerc                      3.0                  hd77b12b_0
libblas                   3.9.0              12_win64_mkl    conda-forge
libbrotlicommon           1.0.9                h2bbff1b_8
libbrotlidec              1.0.9                h2bbff1b_8
libbrotlienc              1.0.9                h2bbff1b_8
libcblas                  3.9.0              12_win64_mkl    conda-forge
libclang                  18.1.1                   pypi_0    pypi
libclang13                14.0.6          default_h8e68704_1
libcublas                 11.11.3.6                     0    nvidia
libcublas-dev             11.11.3.6                     0    nvidia
libcufft                  10.9.0.58                     0    nvidia
libcufft-dev              10.9.0.58                     0    nvidia
libcurand                 10.3.5.147                    0    nvidia
libcurand-dev             10.3.5.147                    0    nvidia
libcusolver               11.4.1.48                     0    nvidia
libcusolver-dev           11.4.1.48                     0    nvidia
libcusparse               11.7.5.86                     0    nvidia
libcusparse-dev           11.7.5.86                     0    nvidia
libdeflate                1.17                 h2bbff1b_1
libffi                    3.4.4                hd77b12b_1
libjpeg-turbo             2.0.0                h196d8e1_0
liblapack                 3.9.0              12_win64_mkl    conda-forge
libnpp                    11.8.0.86                     0    nvidia
libnpp-dev                11.8.0.86                     0    nvidia
libnvjpeg                 11.9.0.86                     0    nvidia
libnvjpeg-dev             11.9.0.86                     0    nvidia
libpng                    1.6.39               h8cc25b3_0
libpq                     12.17                h906ac69_0
libtiff                   4.5.1                hd77b12b_0
libuv                     1.44.2               h2bbff1b_0
libwebp-base              1.3.2                h2bbff1b_0
lz4-c                     1.9.4                h2bbff1b_1
markdown                  3.6                      pypi_0    pypi
markupsafe                2.1.5                    pypi_0    pypi
matplotlib                3.8.4           py310haa95532_0
matplotlib-base           3.8.4           py310h4ed8f06_0
matplotlib-inline         0.1.7                    pypi_0    pypi
mistune                   3.0.2                    pypi_0    pypi
mkl                       2021.4.0                 pypi_0    pypi
mkl-service               2.4.0           py310h2bbff1b_0
mkl_fft                   1.3.1           py310ha0764ea_0
mkl_random                1.2.2           py310h4ed8f06_0
mpc                       1.1.0                h7edee0f_1
mpfr                      4.0.2                h62dcd97_1
mpir                      3.0.0                hec2e145_1
mpmath                    1.3.0           py310haa95532_0
mtcnn                     0.1.1                    pypi_0    pypi
nbclient                  0.10.0                   pypi_0    pypi
nbconvert                 7.16.4                   pypi_0    pypi
nbformat                  5.10.4                   pypi_0    pypi
nest-asyncio              1.6.0                    pypi_0    pypi
networkx                  3.3                      pypi_0    pypi
notebook                  7.2.0                    pypi_0    pypi
notebook-shim             0.2.4                    pypi_0    pypi
numexpr                   2.8.4           py310hd213c9f_0
numpy                     1.24.3          py310hdc03b94_0
numpy-base                1.24.3          py310h3caf3d7_0
oauthlib                  3.2.2                    pypi_0    pypi
omegaconf                 2.3.0                    pypi_0    pypi
opencv-python             4.9.0.80                 pypi_0    pypi
openjpeg                  2.4.0                h4fc8c34_0
openssl                   3.3.0                h2466b09_3    conda-forge
opt-einsum                3.3.0                    pypi_0    pypi
overrides                 7.7.0                    pypi_0    pypi
packaging                 24.0                     pypi_0    pypi
pandas                    2.2.1           py310h5da7b33_0
pandocfilters             1.5.1                    pypi_0    pypi
parso                     0.8.4                    pypi_0    pypi
pillow                    10.3.0          py310h2bbff1b_0
pip                       24.0            py310haa95532_0
platformdirs              4.2.2                    pypi_0    pypi
ply                       3.11            py310haa95532_0
prometheus-client         0.20.0                   pypi_0    pypi
prompt-toolkit            3.0.45                   pypi_0    pypi
protobuf                  3.20.0                   pypi_0    pypi
psutil                    5.9.8                    pypi_0    pypi
pure-eval                 0.2.2                    pypi_0    pypi
py-cpuinfo                9.0.0                    pypi_0    pypi
pyasn1                    0.6.0                    pypi_0    pypi
pyasn1-modules            0.4.0                    pypi_0    pypi
pybind11-abi              5                    hd3eb1b0_0
pycparser                 2.22                     pypi_0    pypi
pygments                  2.18.0                   pypi_0    pypi
pyparsing                 3.0.9           py310haa95532_0
pyqt                      5.15.10         py310hd77b12b_0
pyqt5-sip                 12.13.0         py310h2bbff1b_0
pysocks                   1.7.1           py310haa95532_0
python                    3.10.14              he1021f5_1
python-dateutil           2.9.0post0      py310haa95532_2
python-json-logger        2.0.7                    pypi_0    pypi
python-tzdata             2023.3             pyhd3eb1b0_0
python_abi                3.10                    2_cp310    conda-forge
pytorch                   2.3.0           py3.10_cuda11.8_cudnn8_0    pytorch
pytorch-cuda              11.8                 h24eeafa_5    pytorch
pytorch-mutex             1.0                        cuda    pytorch
pytz                      2024.1          py310haa95532_0
pywin32                   306                      pypi_0    pypi
pywinpty                  2.0.13                   pypi_0    pypi
pyyaml                    6.0.1           py310h2bbff1b_0
pyzmq                     26.0.3                   pypi_0    pypi
qt-main                   5.15.2              h19c9488_10
referencing               0.35.1                   pypi_0    pypi
requests                  2.32.3                   pypi_0    pypi
requests-oauthlib         2.0.0                    pypi_0    pypi
retina-face               0.0.17                   pypi_0    pypi
rfc3339-validator         0.1.4                    pypi_0    pypi
rfc3986-validator         0.1.1                    pypi_0    pypi
rpds-py                   0.18.1                   pypi_0    pypi
rsa                       4.9                      pypi_0    pypi
scikit-learn              1.4.2           py310h4ed8f06_1
scipy                     1.13.1          py310h46043a1_0    conda-forge
seaborn                   0.13.2                   pypi_0    pypi
send2trash                1.8.3                    pypi_0    pypi
setuptools                69.5.1          py310haa95532_0
sip                       6.7.12          py310hd77b12b_0
six                       1.16.0             pyhd3eb1b0_1
sniffio                   1.3.1                    pypi_0    pypi
soupsieve                 2.5                      pypi_0    pypi
sqlite                    3.45.3               h2bbff1b_0
stack-data                0.6.3                    pypi_0    pypi
sympy                     1.12.1                   pypi_0    pypi
tbb                       2021.12.0                pypi_0    pypi
tensorboard               2.10.1                   pypi_0    pypi
tensorboard-data-server   0.6.1                    pypi_0    pypi
tensorboard-plugin-wit    1.8.1                    pypi_0    pypi
tensorflow                2.10.1                   pypi_0    pypi
tensorflow-estimator      2.10.0                   pypi_0    pypi
tensorflow-io-gcs-filesystem 0.31.0                   pypi_0    pypi
termcolor                 2.4.0                    pypi_0    pypi
terminado                 0.18.1                   pypi_0    pypi
threadpoolctl             2.2.0              pyh0d69192_0
tinycss2                  1.3.0                    pypi_0    pypi
tk                        8.6.14               h0416ee5_0
tomli                     2.0.1           py310haa95532_0
torch                     2.3.0                    pypi_0    pypi
torchaudio                2.3.0                    pypi_0    pypi
torchvision               0.18.0                   pypi_0    pypi
tornado                   6.3.3           py310h2bbff1b_0
tqdm                      4.66.4                   pypi_0    pypi
traitlets                 5.14.3                   pypi_0    pypi
types-python-dateutil     2.9.0.20240316           pypi_0    pypi
typing-extensions         4.12.0                   pypi_0    pypi
typing_extensions         4.11.0          py310haa95532_0
tzdata                    2024a                h04d1e81_0
ucrt                      10.0.22621.0         h57928b3_0    conda-forge
ultralytics               8.2.28                   pypi_0    pypi
ultralytics-thop          0.2.7                    pypi_0    pypi
unicodedata2              15.1.0          py310h2bbff1b_0
uri-template              1.3.0                    pypi_0    pypi
urllib3                   2.2.1           py310haa95532_0
vc                        14.2                 h2eaa2aa_1
vc14_runtime              14.38.33135         h835141b_20    conda-forge
vs2015_runtime            14.38.33135         h22015db_20    conda-forge
wcwidth                   0.2.13                   pypi_0    pypi
webcolors                 1.13                     pypi_0    pypi
webencodings              0.5.1                    pypi_0    pypi
websocket-client          1.8.0                    pypi_0    pypi
werkzeug                  3.0.3                    pypi_0    pypi
wheel                     0.43.0          py310haa95532_0
win_inet_pton             1.1.0           py310haa95532_0
wrapt                     1.16.0                   pypi_0    pypi
xz                        5.4.6                h8cc25b3_1
yaml                      0.2.5                he774522_0
zlib                      1.2.13               h8cc25b3_1
zstd                      1.5.5                hd43e919_2
```