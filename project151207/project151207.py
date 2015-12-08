from matplotlib import pyplot as plt
import numpy as np

#plt.plot([1,2,3,4])
#plt.show()

#plt.plot([1,2,3,4])
#plt.plot([1,2,3,4], [1,4,9,16], 'mo-')
#t = np.arange(0., 5., 0.2)
#plt.plot(t, t, 'c--', t, t**2, 'bs', t, t**3, 'g^')
#plt.show()

#cosine, sine 10개만 그리기
#X=np.linspace(-np.pi, np.pi, 256, endpoint=True)
#C, S = np.cos(X), np.sin(X)
#plt.plot(X, C, color="magenta", linewidth=1.0, linestyle="-", label="cosine")
#plt.plot(X, S, color="cyan", linewidth=2.5, linestyle="-", label="sine")
#plt.legend(loc='upper left')
## 그래프 크기
#plt.figure(figsize=(8, 6), dpi=80)
#plt.subplot(1, 1, 1)
#plt.show()

# Set x limits
#plt.xlim(-4.0, 4.0)
## Set x ticks
#plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
## Set y limits
#plt.ylim(-1.0, 1.0)
## Set y ticks
#plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
#plt.show()

#subplot으로 그래프 2개 띄우기
#def f(t):
#    return np.exp(-t) * np.cos(2*np.pi*t)

#t1 = np.arange(0.0, 5.0, 0.1)
#t2 = np.arange(0.0, 5.0, 0.02)

#plt.figure(1)
#plt.subplot(211)
#plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#plt.subplot(212)
#plt.plot(t2, np.cos(2*np.pi*t2),'r--')
#plt.show()

#축 이동
#ax = plt.gca() # gca stands for 'get current axis'
#ax.spines['right'].set_color('red')
#ax.spines['top'].set_color('blue')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
#ax.yaxis.set_ticks_position('left')
#ax.spines['left'].set_position(('data',0.3))
#plt.show()

#동그라미 분포도
#n = 1024
#X = np.random.normal(0, 1, n)
#Y = np.random.normal(0, 1, n)
#T = np.arctan2(Y, X)
#plt.axes([0.025, 0.025, 0.95, 0.95])
#plt.scatter(X, Y, s=75, c=T, alpha=.5)
#plt.xlim(-1.5, 1.5)
#plt.xticks(())
#plt.ylim(-1.5, 1.5)
#plt.yticks(())
#plt.show()

def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

#등고선 그래프
#n = 256
#x = np.linspace(-3, 3, n)
#y = np.linspace(-3, 3, n)
#X,Y = np.meshgrid(x, y)

#plt.axes([0.025, 0.025, 0.95, 0.95])

#plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
#C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
#plt.clabel(C, inline=1, fontsize=10)

#plt.xticks(())
#plt.yticks(())
#plt.show()

def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3 ) * np.exp(-x ** 2 - y ** 2)

n = 10
x = np.linspace(-3, 3, 3.5 * n)
y = np.linspace(-3, 3, 3.0 * n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.imshow(Z, interpolation='nearest', cmap='bone', origin='lower')
plt.colorbar(shrink=.92)

plt.xticks(())
plt.yticks(())
plt.show()

#프언 시험범위 : 정규식부터 matplotlib 기본그래프까지