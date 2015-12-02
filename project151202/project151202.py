import numpy as np
from matplotlib import pyplot as plt

#ctiy 사이의 거리 구하기
mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544, 1913, 2448])
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
print(distance_array)

#그리드 또는 네트워크 기반 거리 계산
x, y = np.arange(5), np.arange(5)[:, np.newaxis]
distance = np.sqrt(x**2 + y**2)
print(distance)

#plt.pcolor(distance)
#plt.colorbar()
#plt.show()

x, y = np.ogrid[0:5, 0:5]
print(x, y)
print('브로드캐스팅')
print(x+y)

x, y = np.mgrid[0:5, 0:5]
print(x, y)
print(x+y)

#flattening
a = np.array([[1,2,3],[4,5,6]])
print(a.ravel())
print(a.T)
print(a.T.ravel())

#reshaping
print('reshaping')
a.shape
b = a.ravel()
b = b.reshape((2,3))
print(b)
print(b.reshape((2,-1)))

#adding a dimension
z = np.array([1,2,3])
print(z[:, np.newaxis])
print(z[np.newaxis, :])

#resizing
a = np.arange(4)
a.resize((8,))
print(a)

#sorting data
a = np.array([[4,3,5], [1,2,1]])
b = np.sort(a, axis=1)
print(b)
a.sort(axis=1)
print(a)

a = np.array([4,3,1,2])
j = np.argsort(a)
print(j)
j_max = np.argmax(a)
j_min = np.argmin(a)
print(j_max, j_min)

#polynomials
p = np.poly1d([3,2,-1])
print(p(0))
print(p.roots)
print(p.order)
p = np.polynomial.Polynomial([-1,2,3])

x = np.linspace(0, 1, 20)
y = np.cos(x) + 0.3*np.random.rand(20)
p = np.poly1d(np.polyfit(x, y, 3))
t = np.linspace(0, 1, 200)
#plt.plot(x, y, 'o', t, p(t), '-')
#plt.show()

x = np.linspace(-1, 1, 2000)
y = np.cos(x) + 0.3*np.random.rand(2000)
p = np.polynomial.Chebyshev.fit(x, y, 90)
t = np.linspace(-1, 1, 200)
#plt.plot(x, y, 'r.')
#plt.plot(t, p(t), 'k-', lw=3)
#plt.show()

#images
img = plt.imread('muzi.png')
print(img.shape, img.dtype)
imgcut = img[:40, :60]
plt.imshow(img)
plt.show()
plt.imshow(imgcut)
plt.show()
