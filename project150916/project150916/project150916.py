#fileName="kong.txt"
#with open(fileName, "r") as myfile:
    #myfile.write("201311239 이채은\n")
    #myfile.write("안녕하세요\n")
    #myfile.write("hello!\n")
    #myfile.write("bonjour\n")

    #content = myfile.read()
    #print(content)

    #while True:
    #    content = myfile.readline()
    #    if not content: break
    #    print(content)

    #content = myfile.readlines()
    #for line in content:
    #    print(line)

#fileName="file_example1.txt"
#with open(fileName, "r") as myfile:
#    #for line in myfile:
#    #    print(line)
#    for line in myfile:
#        newfile="Monica.txt"
#        (role, etc)=line.strip().split(":")
#        #print(role)
#        if role == "Monica":
#            mynewfile=open(newfile, "a")
#            mynewfile.write(line)

#import pickle

#fileName="file_example2.txt"
#newfile="Monica2.txt"
#roles=[]
#with open(fileName, "r") as myfile, open(newfile, "wb") as monica:
#    #for content in myfile:
#    #    (role, etc) = content.strip().split(":", 1)
#    #    monica.write(etc)
#    #    monica.write("\n")
#    for content in myfile:
#        (role, etc) = content.strip().split(":", 1)
#        roles.append(role)
#    pickle.dump(roles, monica)

#with open(newfile, "rb") as monica:
#    result=pickle.load(monica)
#    print(result)

import csv
fileName = "test.csv"
READ = "r"
with open(fileName, READ) as myFile :
    dataFromFile = csv.reader(myFile)
    for currentRow in dataFromFile :
        print(currentRow)