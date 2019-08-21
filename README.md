# Korean LipNet

### - 추진 배경 및 목적
우연히 청각장애인들과 의사소통을 하면서, 청각장애인들은 수화를 하지 못하는 일반인과 의사소통을 할 때 입모양을 읽어 상대방의 말을 유추해 소통한다고 알게 되었다. 이를 통해 입술의 움직임만을 읽어 무슨 말을 하는지 텍스트화 시킬 수 있다면 좀 더 원활한 의사소통이 가능하지 않을까 생각하게 되었다. 또한, 요즈음엔 직접 만나지 않고 다대다 화상채팅으로 회의나 의사소통을 자주 하게 되는데 진행 중 동시에 여러명이 말을 하면 음성이 겹쳐 못 듣거나 다시 말해야 하는 불편함이 있고 또는 시끄러운 환경이라면 소통이 힘들다. 그러한 경우에 화면 옆에 채팅창처럼 시각적으로 보여준다면 더 좋지 않을까 생각을 했는데, 음성인식 기술만으로는 한계가 있어 더 찾아보니 LipNet이라고 하는 입술 움직임을 읽어 무슨 말을 하는지 도출해 낼 수 있는 모델이 존재했다. 허나 영어만 인식이 가능하게 만들어진 모델이여서 한국어도 가능한 모델을 만들면 어떨까 하여 Korean LipNet을 구상하게 되었다.

### - 작품 소개
딥러닝 분야에서 핵심기술인 STCNN(시공간 이미지 학습)과 LSTM(순차데이터 처리학습)동시에 사용하였고, 입술의 입 모양 뿐만 아니라, 혀의 움직임 등을 처리하기 위해 3D 학습모델 구축하였습니다. 이뿐만 아니라 “필통, 축구, 숫자”등과 같은 단어학습 뿐만 아니라 “안녕하세요, 저는 OOO입니다. 잘 부탁드립니다.”등과 같은 여러 개의 단어로 이루어진 문장 또한 인식할 수 있게 학습모델을 구축하였습니다. 저희 작품을 통하여 동영상의 경우 음성이 깨져서 들을 수 없거나, 음성이 없는 동영상에 대하여 한국어 자막을 넣어주는 역할을 할 수 있는 모델입니다.

### - 시나리오
사용자들이 자막 삽입을 하고 싶은 영상을 웹에 등록하면, 서버에서 Korean LipNet을 통해 등록된 동영상 안의 사람의 입모양을 읽은 후 도출된 자막을 입히고 사용자들에게 자막이 삽입된 새로운 영상을 제공한다. 또한, 화상회의와 같은 스트리밍의 형태의 경우 회의 참석자의 말을 채팅창과 같은 방식으로 제공해 원활한 의사소통을 할 수 있게 한다.

* Flask Web Demo URL  
 <a href="https://github.com/kykymouse/KoreanLipNetWeb">KoreanLipNetWeb</a>


### - 시스템 구조
![11](https://user-images.githubusercontent.com/32935365/60751021-cd7a0380-9fea-11e9-9321-f8f0c561632e.png)


### - 예시 영상

![a](https://user-images.githubusercontent.com/32935365/60869619-4044e200-a26a-11e9-82d6-e246158d233a.gif)

![b](https://user-images.githubusercontent.com/32935365/60869711-71251700-a26a-11e9-8559-70a085a368ac.gif)

![c](https://user-images.githubusercontent.com/32935365/60869723-797d5200-a26a-11e9-9b0d-7834224d417a.gif)

### - 기대효과
* 다양한 플랫폼에서 청각장애인과 원활한 의사소통 기대
* 주위에서 흔하게 볼 수 있는 음성인식 시스템에서도 주위환경에 소음이 있는 제한된 환경에서 입모양을 읽어 음성인식 보완 기대
* 다중 화상회의의 경우 여러 명의 음성이 맞물리는 경우 원활한 의사소통이 쉽지 않은 곳에 있어서 Korean LipNet 모델을 이용해 자막을 제공하여 원활한 의사소통 기대
* 음성이 깨진 영상 파일에서의 음성인식 시스템을 대체하여 자막생성을 가능하게 할 수 있는 기대
* 음성인식 시스템과 Korean LipNet모델을 결합하여 보다 높은 인식률의 자막 시스템 기대

### - 사용 환경
- **Library** : Keras, Tensorflow, OpenCV, DLib
- **Tool** : Visual Code, TensorBoard
- **Language** : Python
- **Hardware** : Web Camera, Desktop(NVIDIA GTX 2080ti)



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
  - 만약 안된다면
  $ chmod +x NVIDIA-Linux-x86_64–410.57.run
  $ sudo ./NVIDIA-Linux-x86_64–410.57.run --no-x-check
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
git clone https://github.com/kykymouse/koreanLipNet.git
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
