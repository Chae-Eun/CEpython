def printdata(data, level=0):    #재귀함수로 출력
    for item in data:
        if isinstance(item, list):
            printdata(item, level+1)
        else:
            for i in range(level):
                print("\t", end="")
            print(item)