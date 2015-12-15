import time
import sys
import csv
import os

class MidTest:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def question1(self):
        print("학번 : " + self.id + ", 이름 : " + self.name)

    def question2(self, data, num):
        list = []
        list2 = []
        number = num;
        for key in data: 
            list.append((data[key], key))
            list.sort()
        i=0
        for (a, b) in list:
            le = len(list) - number;
            if i >= le:
                list2.insert(0, {b:a}) 
            i+=1        
        print(list2)

    def question3(self, file):
        os.chdir("./score")
        for (path, dir, files) in os.walk('.'):
            newfile = file
            for f in files: 
                with open(f, "r+") as file, open(newfile, "a+") as newFile:
                    contents = file.read()
                    newFile.write(contents)
        if(os.path.isfile(newfile)):
            print(newfile + "생성이 완료되었습니다.")
        else:
            print(newfile + "이 만들어지지 않았습니다.")
        os.chdir("..")

    def question4(self, file):
        try:
            newfile = file
            os.chdir("./score")
            sort = []
            with open(newfile, "r") as myfile:
                data = csv.reader(myfile)
                sum = []
                dic = {}
                a = []
                for line in data:
                    sum = int(line[1])+int(line[2])+int(line[3])
                    dic[line[0]]=sum
                    sort.append((sum, line[0]))
                    sort.sort()
                i = 0
                for (a, b) in sort:
                    i += 1
                    if i == len(sort):
                        print((b, a))
        except filenotfounderror as e:
            error = sys.exc_info()[0]
            print(error, e)
        except:
            error = sys.exc_info()[0]
            print(error)

    def question5(self):
        print(time.strftime("Current Time : %Y.%m.%d %H:%M:%S", time.localtime()))

greenjoa = MidTest("201311239", "이채은")
greenjoa.question1()
data = {"명량":4.5, "베테랑":4.0, "암살":4.6, "마션": 4.3}
greenjoa.question2(data, 2)
greenjoa.question3("question3.txt")
greenjoa.question4("question3.txt")
greenjoa.question5()