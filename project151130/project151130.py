import numpy as np
from matplotlib import pyplot as plt

list = [1, 2, 3]
print(list*2)

# 요소별 연산
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data+2)
print(data-2)
print(data*data)
print(data/3)
print(data**2)
print(data**0.5)
# 매핑되어야만 dot을 사용 가능
print(data.dot(data))

# 비교 연산
a = np.array([1,2,3,4])
b = np.array([4,2,2,4])
print(a == b)
print(a > b)
# array 비교 연산
c = np.array([1,2,3,4])
print(np.array_equal(a,b))
print(np.array_equal(a,c))

#논리 연산1
a = np.array([1,1,0,0], dtype=bool)
b = np.array([1,0,1,0], dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))
print(np.all([True, True, False]))
print(np.any([True, True, False]))
# 초월함수
a = np.arange(5)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))

# 전이행렬
a = np.triu(np.ones((3,3)), 1)
print(a)
print(a.T)

# sum
print('sum')
x = np.array([1,2,3,4])
print(np.sum(x))
print(x.sum())
x = np.array([[1,1],[2,2]])
print(x.sum(axis=0))
print(x.sum(axis=1))
print(x[0, :].sum(), x[1,:].sum())

# 최대, 최소
x = np.array([1,3,2])
print(x.min())
print(x.max())
print(x.argmin())
print(x.argmax())

# 논리연산2
np.all([True, True, False])
np.any([True, True, False])
a = np.zeros((100,100))
print(np.any!=0)
print(np.all(a==a))

# 통계
x = np.array([1,2,3,1])
y = np.array([[1,2,3],[5,6,1]])
print(x.mean()) # 평균
print(np.median(x)) # 중간값
print(np.median(y,axis=-1))
print(x.std()) # 표준편차

# 응용
data = np.loadtxt('data.txt')
year, hares, lynxes, carrots = data.T
print(data.T)
#plt.plot(year, hares, year, lynxes, year, carrots)
#plt.show()

# 각각의 연도별 평균, 표준편차
print('    year   hares   lynxes   carrots')
print(data)
print(data.mean(axis=0))
print(np.std(data, axis=0))

# 최대 개체수를 갖는 연도 구하기~
print(np.argmax(data, axis=0))
max=np.argmax(data, axis=0)
#print(' hares : '+data[0][max[1]])
#print(' lynxes : '+data[0][max[2]])
#print(' carrots : '+data[0][max[3]])
# ---> 출력 다시 확인하기

# 브로드캐스팅
data = np.array([[0, 10, 20, 30, 40, 50]]).T
print(data.shape)
print(data+[0,1,2,3,4,5])