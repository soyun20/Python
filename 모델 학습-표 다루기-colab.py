# 라이브러리 사용
import tensorflow as tf
import pandas as pd

# 파일들로부터 데이터 읽어오기
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
레모네이드 = pd.read_csv(파일경로)

#파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
#보스턴 = pd.read_csv(파일경로)

#파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
#아이리스 = pd.read_csv(파일경로)

# 데이터 모양으로 확인하기
print(레모네이드.shape)
#print(보스턴.shape)
#print(아이리스.shape)

# 칼럼 이름 출력
print(레모네이드.columns)
#print(보스턴.columns)
#print(아이리스.columns)

독립 = 레모네이드[['온도']]
종속 = 레모네이드[['판매량']]
print(독립.shape, 종속.shape)

#독립 = 보스턴[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
#       'ptratio', 'b', 'lstat']]
#종속 = 보스턴[['medv']]
#print(독립.shape, 종속.shape)

#독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
#종속 = 아이리스[['품종']]
#print(독립.shape, 종속.shape)

레모네이드.head()

#보스턴.head()

#아이리스.head()

# 모델을 만듭니다.
X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

# 모델을 학습합니다.
model.fit(독립, 종속, epochs=10)

종속

model.predict([[15]])
