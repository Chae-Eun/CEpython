def printdata(data, level=0):    #����Լ��� ���
    for item in data:
        if isinstance(item, list):
            printdata(item, level+1)
        else:
            for i in range(level):
                print("\t", end="")
            print(item)