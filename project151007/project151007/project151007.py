#num = [1, 2, 3, 4]
#print(dir(num))

#data = list(enumerate("greenjoa"))
#data2 = list(enumerate(num))
#print(data)
#print(data2)

#test = eval('1+2')
#print(test)

#def positive(l):
#    return l > 0

#print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

#def even(l):
#    return l%2 < 1 

#print(list(filter(even, [1, -3, 2, 0, -5, 6])))

#a=3
#print(id(3))
#print(id(a))

#print(list(filter(lambda l: l%2 < 1, [1,2,3,4])))

#a = [1, 2, 3]
#b = list(a)
#c = a

#print(a)
#print(b)
#print(c)

#print(list(map(lambda a: a*2, [1,2,3,4])))

#print(max([1,2,3]))
#print(max("python"))

#print(eval(repr("hi".upper())))
##print(eval(str("hi".upper())))

#list의 sort는 함수 실행 후 데이터가 바뀌지만 sorted는 정렬된 리스트를
#반환해주기 때문에 데이터의 변화가 없다.
#data=[20, 40, 10, 5, 8, 6, 17]
#data.sort()

#print(data)
#print(sorted([3,1,2]))
#print(sorted("zero"))

data={'홍길동':[80, 70, 60, 92],
       '김길동':[24, 35, 18, 10],
       '고길동':[10, 20, 8, 5]}

dic = {}
a = list(sorted(data.keys()))
print(a)

for steps in a :
    dic[steps] = 'i';

print(dic)

for step in data, a:
    dic[step] = sorted(data[step])

print(dic)

#dic={}

#for steps in a, b:
#    dic[a] = b

#print(dic)


#data["홍길동"] = sorted(data["홍길동"])
#data["김길동"] = sorted(data["김길동"])
#data["고길동"] = sorted(data["고길동"])
#print(data["홍길동"])
#print(data["김길동"])
#print(data["고길동"])