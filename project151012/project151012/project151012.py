#coding:cp949
import os
import sys
import pickle

#os.system("python test.py")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, " : ", self.age)

hi = Student("ȫ�浿", 23)
hi.show()
Student.show(hi)

f = open("test.txt", 'wb')
pickle.dump(hi, f)
f.close()

f2 = open("test.txt", 'rb')
data = pickle.load(f2)
print(data)

Student.show(data)

#print(os.environ)
#print(os.getcwd())
#os.chdir("..")
#print(os.getcwd())
#os.startfile('C:/Users/im15/Documents/GitHub/CEpython/project151012/project151012/test.txt')
#print(list(os.walk(".")))

message ='helloworld'
print(message.find('rldd'))

import shutil
#���� ���丮�� ���� ���丮�� ����� ���ݱ��� ���� txt������ ��� ���� ���丮�� �־��

if os.path.exists("./sample") == False:
    os.mkdir("sample")

dir = list(os.walk("."))
print(dir)

for steps in dir:
    for line in steps:
        for step in line:
            if step.find('txt') >= 0:
                print(step)
                shutil.copy(step, "./sample/")

#print(os.path.dirname('c:/python34/python.exe'))
#os.path.expanduser('~\\python.exe')
#print(os.getcwd())

