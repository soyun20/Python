import numpy as np  # numpy 라이브러리 불러오기, numpy를 np로 줄여 사용
import matplotlib.pyplot as plt # 파이썬에서 데이타를 차트나 플롯(Plot)으로 그려주는 라이브러리인 Matplotlib 불러오기, plt로 줄여 사용
import tensorflow as tf # tensorflow 라이브러리 불러오기, tensorflow를 tf로 줄여 사용
from tensorflow import keras # keras 라이브러리 불러오기
from tensorflow.keras import datasets, layers, models # 모델을 만들 때 keras sequential API 사용

cifar10 = datasets.cifar10 # cifar10 에 데이터셋 cifar10 대입
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data() # cifar-10 데이터셋 다운로드

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'] # 클래스 10개의 이름을 각각 지정

print("Train samples:", train_images.shape, train_labels.shape) # 학습할 이미지 데이터셋과 라벨 형태 출력
print("Test samples:", test_images.shape, test_labels.shape) # 테스트할 이미지 데이터셋과 라벨 형태 출력

train_images = train_images.reshape((50000, 32, 32, 3)) # numpy 라이브러리 reshape 함수를 이용하여 적절한 형태의 배열로 변환
test_images = test_images.reshape((10000, 32, 32, 3)) # numpy 라이브러리 reshape 함수를 이용하여 적절한 형태의 배열로 변환


plt.figure(figsize=(10, 10)) # figure 함수를 이용하여 그림의 크기 변경
for i in range(25): # for 문을 이용하여 25번 반복
    plt.subplot(5, 5, i+1) # 5개의 행과 5개의 열로 구성한다.
    plt.xticks([]) # x축의 좌표의 눈금을 표시하지 않음
    plt.yticks([]) # y축의 좌표의 눈금을 표시하지 않음
    plt.grid(False) # 그림 중간에 그리드 선을 표시하지 않음
    plt.imshow(train_images[i]) # 25개의 그림을 그림
    plt.xlabel(class_names[train_labels[i][0]]) # 각각의 그림의 클래스 이름을 x축에 출력
plt.show() # 그림 출력


train_images = train_images/255.0 # 픽셀값을 0과 1사이의 값으로 정규화 (RGB는 각각 0부터 255까지의 숫자를 가질 수 있음)
test_images = test_images/255.0 # 픽셀값을 0과 1사이의 값으로 정규화 (RGB는 각각 0부터 255까지의 숫자를 가질 수 있음)

model = models.Sequential() # 선형으로 계층을 쌓는 모델 만들기
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3))) # Convolution layer 추가 (32개의 convolution 필터의 수와 3행과 3열로 이루어진 convolution 커널을 이용하며 활성화함수는 relu이고 입력 형태는 32 x 32 x 3)
model.add(layers.MaxPooling2D((2, 2))) # Max Pooling layer 추가 (2 x 2의 형태의 풀 사이즈로 max polling 하기)
model.add(layers.Conv2D(64, (3, 3), activation='relu')) # Convolution layer 추가 (64개의 convolution 필터의 수와 3행과 3열로 이루어진 convolution 커널을 이용하며 활성화함수는 relu로 사용)
model.add(layers.MaxPooling2D((2, 2))) # Max Pooling layer 추가 (2 x 2의 형태의 풀 사이즈로 max polling 하기)
model.add(layers.Conv2D(64, (3, 3), activation='relu')) # Convolution layer 추가 (64개의 convolution 필터의 수와 3행과 3열로 이루어진 convolution 커널을 이용하며 활성화함수는 relu로 사용)
model.add(layers.Flatten()) # 2차원 데이터를 1차원으로 바꿔주는 계층 추가
model.add(layers.Dense(64, activation='relu')) # 출력 뉴런을 64개로 설정하고 활성화함수를 relu로 사용하여 입력과 출력을 연결해주는 dense 계층을 추가
model.add(layers.Dense(10, activation='softmax')) # 출력 뉴런을 10개로 설정하고 활성화함수를 softmax로 사용하여 입력과 출력을 연결해주는 dense 계층을 추가

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']) # 모델 컴파일 단계로 optimizer(모델을 업데이트 하는 방법)는 adam을 이용, loss function(훈련하는 동안 모델의 오차 측정)은 sparse_categorical_crossentropy를 이용, metrics(훈련 단계와 테스트 단계를 모니터링 함)는 올바르게 분류된 이미지의 비율인 정확도를 사용
model.fit(train_images, train_labels, epochs=10) # 모델 훈련 단계로 모델이 이미지와 라벨을 매핑하는 방법을 배움. epochs(전체 데이터 학습 반복 횟수)는 10번으로 설정

test_loss, test_acc = model.evaluate(test_images, test_labels) # 테스트 데이터로 정확도 평가하기

print('Test accuracy:', test_acc) # 정확도 출력

predictions = model.predict(test_images) # 훈련된 모델을 사용하여 이미지에 대한 예측 만들기

def plot_image(i, predictions_array, true_label, img): # plot_image 함수 정의
  predictions_array, true_label, img = predictions_array[i], true_label[i], img[i] # 예측할 배열의 데이터와 라벨과 이미지를 변수에 대입
  plt.grid(False) # 그림 중간에 그리드 선을 표시하지 않음
  plt.xticks([]) # x축의 좌표의 눈금을 표시하지 않음
  plt.yticks([]) # y축의 좌표의 눈금을 표시하지 않음

  plt.imshow(img, cmap=plt.cm.binary) # 그림을 그리고 2가지 색상을 이용하여 맵을 그림

  predicted_label = np.argmax(predictions_array) # 예측 모델의 라벨을 배열 값의 최대값을 대입함
  if predicted_label == true_label: # 만약 예측한 라벨이 맞는 라벨이라면 실행
    color = 'blue' # color에 blue를 대입 (파란색으로 색을 지정)
  else: # if문의 조건에 맞지 않는다면 실행
    color = 'red' # color에 red를 대입 (빨간색으로 색을 지정)

 # 예측 그림의 x축 정보
  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label[0]]),
                                color=color)

def plot_value_array(i, predictions_array, true_label): # plot_value_array 함수 정의
  predictions_array, true_label = predictions_array[i], true_label[i] # 예측할 배열의 데이터와 라벨과 이미지를 변수에 대입
  plt.grid(False) # 그림 중간에 그리드 선을 표시하지 않음
  plt.xticks([]) # x축의 좌표의 눈금을 표시하지 않음
  plt.yticks([]) # y축의 좌표의 눈금을 표시하지 않음
  thisplot = plt.bar(range(10), predictions_array, color="#777777") # 그래프 막대를 10번 반복해서 예측 배열의 확률을 회색으로 그림
  plt.ylim([0, 1]) # 그래프 범위를 y축은 최소값을 0으로, 최대값을 1로 지정한다.
  predicted_label = np.argmax(predictions_array) # 예측 모델의 라벨을 배열 값의 최대값을 대입함

  thisplot[predicted_label].set_color('red') # 예측 최대값을 빨간색으로 지정
  thisplot[true_label[i]].set_color('blue') # 올바른 예측 라벨은 파란색으로 지정

i = 0 # 변수 i에 0 대입
plt.figure(figsize=(6,3)) # 그림과 그래프 크기 지정
plt.subplot(1,2,1) # 1개의 행과 2개의 열로 구성한다.
plot_image(i, predictions, test_labels, test_images) # plot_image 함수 실행
plt.subplot(1,2,2) # 1개의 행과 2개의 열로 구성한다.
plot_value_array(i, predictions,  test_labels) # plot_value_array 함수 실행
plt.show() # 그림 출력
