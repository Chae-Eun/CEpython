import numpy as np
from matplotlib import pyplot as plt

data = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(data)
#차원 묻기
print(data.ndim)
#(?,?)인지 묻기
print(data.shape)
#배열 길이 묻기
print(len(data))
#???
print(data.dtype)

#data가 모두 ?.으로 끝남
data = np.array([[1,2,3],[4,5,6],[7,8,9.]])
print(data)

#데이터형 변경
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
data.astype(np.float)
data = np.array([1,2,3])
data.astype(np.int)

#데이터형 지정
data = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=float)
print(data)
data = np.array([1,2,3], dtype=complex)
print(data)

print("*1로 채워진 행렬*")
print(np.ones((3,2)))
print("*0으로 채워진 행렬*")
print(np.zeros((3,2)))
print("*단위 행렬")
print(np.eye((3)))
print("*대각 행렬*")
print(np.diag(np.array([1,2,3,4])))
print("*전치 행렬*")
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data.T)

#등간격 배열
print(np.arange(10))
print(np.arange(10, 1, -1))
print(np.arange(10, 1, -1)[:, np.newaxis])
print(np.arange(2, 8, dtype=np.float))
print(np.arange(35).reshape(5,7))

#지정된 수의 배열
print(np.linspace(1., 4., 6))
print(np.linspace(1., 4., 6, endpoint=False))

#난수 발생
data = np.random.rand(4)
print(data)
data = np.random.randn(4)
print(data)

#data.txt 읽어서 배열과 그래프 그리기
#data = np.loadtxt('data.txt')
#year, hares, lynxes, carrots = data.T
#print(year, hares, lynxes, carrots)
#plt.plot(year, hares, year, lynxes, year, carrots)
#plt.show()

data = np.array([[1,2,3],[4,5,6],[7,8,9,10]])
#첫번째 행
print(data[0])
print(data[-1])
print(data[0:2])
print(data[2][0])
print(data[:2])
#print(data[2,0])
print(data[0:1])
print(data[1:4:2])
#print(data[1:4:2, ::3])

x = np.arange(10, 1, -1)
print(x[np.array([3, 3, 1, 8])])
print(x[np.array([[1,1],[2,3]])])

y=np.arange(35).reshape(5,7)
print(y[np.array([0,2,4])])


data = np.arange(36).reshape(6,6)
print(data)
mask = np.array(np.array([1,0,1,0,0,1], dtype=bool))
print(data[mask, 2])

mask1 = np.array([0,1,2,3,4])
mask2 = np.array([1,2,3,4,5])
print(data[mask1, mask2])

mask3 = np.array([0,2,5])
print(data[3, mask3])
print(data[4, mask3])
print(data[5, mask3])
