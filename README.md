# Korean LipNet

### 작품 소개

딥러닝 분야에서 핵심기술인 STCNN(시공간 이미지 학습)과 LSTM(순차데이터 처리학습)동시에 사용하여 학습모델을 구축하고 한글 모델에 따른 전처리를 통한 한국어 학습 및 인식한다. 동영상의 경우 음성이 깨져서 들을 수 없거나, 자막이 없어서 청각 장애인이 영상을 보는데 어려움이 있을 때 저희 모델을 사용하여 입술의 움직임을 읽은 후 한국어 자막을 포함된 영상을 볼 수 있다.

### 시스템 구조

![image](https://user-images.githubusercontent.com/32935365/58874826-c8cce180-8704-11e9-9526-d406882d5e20.png)


### 예시 영상

[![Watch the video](https://user-images.githubusercontent.com/32935365/60746344-3fd1f000-9fb9-11e9-9e4e-a24461563e6f.PNG)](https://youtu.be/ycvjTZhqAIs)

[![Watch the video](https://user-images.githubusercontent.com/32935365/60746354-4fe9cf80-9fb9-11e9-9c80-c1d700bd21f3.PNG)](https://youtu.be/EvRNIGnaLbY)

[![Watch the video](https://user-images.githubusercontent.com/32935365/60746368-61cb7280-9fb9-11e9-8281-445703cc3154.PNG)](https://youtu.be/CAZAeY2GuVk)

### 주요 적용 기술

- **Library** : Keras, Tensorflow, OpenCV, DLib
- **Tool** : Visual Code, TensorBoard
- **Language** : Python
- **Hardware** : Web Camera, Desktop(NVIDIA GTX 2080)



# 개발환경 설정
### Ubuntu 16.04 LTS, CUDA 8.0, cudNN v5.1, Tensorflow-gpu 1.0.1

### - NVIDIA 드라이버 다운로드
```
1. System Settings -> Software & Updates -> Additional Drivers
2. Using NVIDA binary version ~ (open source) 클릭
3. apply changes & MOK 비밀번호 설정
4. 재부팅 후 secure boot 창이 뜨면 MOK로 들어가서 비밀번호 치고 key 등록 후 부팅
5. nvidia-smi 및 NVIDIA X Server Settings로 확인
```

### - Anaconda 설치
```
1. python 2.7 버전으로 다운로드
2. bash Anaconda2-2019.03-Linux-x86_64
3. 계속 yes
4. 마지막 쯤에 PATH에 anaconda2가 있는지 확인
5. gedit ~/.bashrc
6. 맨 마지막에  
export PATH="/home/kykymouse/anaconda2/bin:$PATH"
있는지 확인
7. 터미널 끄고 다시 터미널 킨 후
python
import matplotlib
되는지 확인
```

### - CUDA Toolkit 설치
```
1. https://developer.nvidia.com/cuda-toolkit-archive 접속 후 각 pc에 맞는 CUDA Toolkit 설치(여기선 CUDA Toolkit 8.0 GA2를 사용, Base Installer 다운)
2. Linux - x86_64 - Ubuntu - 16.04 - runfile(local)
3. 다운로드 폴더에서 터미널을 연 후 sudo sh cuda_8.0.61_375.26_linux.run 명령 실행
4. 쭉 문서를 읽다가  

Do you accept the previously read EULA?
(a)ccept/(d)ecline/(q)uit: **accept**  

Install NVDIA Accelerated Graphics Driver for Linux-86_61 375.26?  
(y)es/(n)o/(q)uit: **no**  

Enter Toolkit Location  
[ default is /usr/localcuda-8.0 ] : **[enter치고 그냥 넘어감]**  

Do you want to install a symbolic link at /usr/local/cuda?  
(y)es/(n)o/(q)uit : **yes**  

Install the CUDA 8.0 Samples?  
(y)es/(n)o/(q)uit: **no**

5. gedit ~/.bashrc하고 맨 밑에 3줄 추가
export CUDA_HOME=/usr/local/cuda-8.0  
export PATH=/usr/local/cuda-8.0/bin${PATH:+:${PATH}}  
export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}  
6. source ~/.bashrc
7. nvcc --version으로 설치 되었는지 확인
```

### - cuDNN 설치
```
1. https://developer.nvidia.com/cudnn에 접속하여 해당 버전 다운르도(여기선 cuDNN v5.1(Jan 20, 2017) for CUDA 8.0 사용)
2. 다운 후 압축 풀기
3. 터미널에서 sudo nautilus 명령으로 관리자 권한으로 탐색기 열기
4. usr/local/cuda로 들어감
5. cuda/include 에 있는 파일을 usr/localcuda/include에 복사
6. cuda/lib64 에 있는 파일을 usr/localcuda/lib64에 복사
7. sudo chmod a+r /usr/local/cuda/lib64/libcudnn*
```

### - Tensorflow-gpu 설치
```
1. tensorflow gpu 1.0.1 설치(python 2.7기준)  
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.0.1-cp27-none-linux_x86_64.whl
```

### - dlib 설치
```
1. sudo apg-get install cmake
2. sudo apt-get install libboost-all-dev
```

### - ffmpeg 설치
```
1. sudo apt-get install ffmpeg
2. sudo apt-get update
```

### - final
```
1. pip install -e . 실행
2. 라이브러리들이 버전이 맞는지 pip list | grep 패키지명 으로 비교
3. 완료가 되면 빨간 오류 없이 진행된다.
4. 만약 오류가 뜬다면 해당 패키지를 삭제 후 재설치
```
# 사용법
### - clone repository
```
git clone https://github.com/rizkiarm/LipNet
```
### - directory structure
바탕화면에 align 폴더를 만든다.
그리고 각각 training/overlapped_speakers/s{i}/datasets 와 training/overlapped_speakers/datasets에 symbolic link를 건다.
- 전체 directory structure

![1](https://user-images.githubusercontent.com/32935365/60745074-a522e280-9fb3-11e9-8a2e-fa20ddf00551.PNG)

- training/overlapped_speakers/s{i}/datasets

![2](https://user-images.githubusercontent.com/32935365/60745117-d0a5cd00-9fb3-11e9-8bca-fc2f0c7df938.PNG)

- training/overlapped_speakers/datasets

![3](https://user-images.githubusercontent.com/32935365/60745122-da2f3500-9fb3-11e9-9c3f-ecbe9a517415.PNG)

### - prepare dataset for training
필요한 준비물은 다음과 같다.
1. 360 * 288 크기, 초당 25frame의 동영상을 준비한다.
2. 각 동영상에 해당하는 align 파일을 만든다.
3. grid.txt에 학습시키는 모든 align 문장이 들어있다.


### - align
align은 각 동영상에 대한 정답파일이다.
따라서, 동영상1개당 1개의 align파일이 존재해야한다.
align작성은 각 글자에 해당하는 frame을 적어준다.
(sil : 묵음, sp : 공백을 의미)

![4](https://user-images.githubusercontent.com/32935365/60745563-dd2b2500-9fb5-11e9-9938-9f9ca74de5c3.png)

# Train
학습시킬 동영상 폴더를 지정해준다
```
python train.py s{i}
```

# Predict
학습으로 생성된 가중치 파일과 예측할 동영상을 지정해준다
```
python predict.py [path to weight] [path to video]
```
