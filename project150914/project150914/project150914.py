#def sum_and_mul(a,b):
#    return a+b, a*b

#data = sum_and_mul(3,4)
#sum, mul = sum_and_mul(3,4)
#print(data)
#print(sum)
#print(mul)
#print(sum, mul)

#coding:cp949 인코딩모드를 cp949로 지정해줌

#def printData(data):
#    for item in data:
#        if isinstance(item, list):
#            for steps in item:
#                print(steps)
#        else:
#            print(item)

#def printdata(data, level=0):    #재귀함수로 출력
#    for item in data:
#        if isinstance(item, list):
#            printdata(item, level+1)
#        else:
#            for i in range(level):
#                print("\t", end="")
#            print(item)

#import printData

#data=["홍길동", ["베테랑", ["류승완", "황정민"]],
#      "고길동", ["암살", ["전지현", "하정우"]],
#      "김길동", ["오피스", ["고아성", "김병국"]]]

#printData.printdata(data)

import os

print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
#os.system("python setup.py sdist")
os.system("python setup.py install")