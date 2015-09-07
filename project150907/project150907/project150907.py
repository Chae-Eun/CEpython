#e = [1, 2, ['Life', 'is']]
#data=['a', 'b', 'c', ['abcd', 'efg']]
#print(data[0])
#print(data[-1])
#print(data[3][1])

#f = e+data
#print(f)
#print(e*3)

#print(data[-3])

#guests = ['a', 'b', 'c', 'd']

#guests[0] = 'greenjoa'
#guests[1] = ['greenjoa1', 'greenjoa2']
#guests[1:2] = ['greenjoa1', 'greenjoa2']

#print(guests)

#guests.insert(2, 'e')
#guests.append('greenjoa2')

#print(guests)
#print(guests[-1])

#id = ['abc', 'def', 'ghi']
#id.insert(1, '123')
#id.insert(3, '456')
#id.insert(5, '789')
#print(id)

#id.insert(2, ['가나다', '000-1111-2222'])
#id.insert(5, ['가나다', '000-1111-2222'])
#id.append(['가나다', '000-1111-2222'])
#print(id)

#guests = ['a', 'b', 'c', 'd']

#for steps in range(4) :
#    print(guests[steps])

#nEntries = len(guests)
#for steps in range(nEntries) :
#    print(guests[steps])

#for guest in guests :
#    print(guest)

#scores = [85, 62, 63, 45, 90]
#scores.sort()
#print(scores)
#scores.reverse()
#print(scores)

#data2 = [53, 48, 57, 63, 25, 78, 24, 56, 29]
#data2.sort()
#data2.reverse()
#print(data2)
#top = data2[0:5]
#print(top)

#for steps in data2 :
#    if isinstance(steps, list) :
#        for step in steps :
#            print(step)
#    else :
#        print(steps)


#즐거운 파이썬시간

#scores = [85, 63, 63, 45, 90]
#scores.extend([50, 60])
#scores.append([50, 60])
#print(scores)

#num = scores.pop(2)
#print(num)

t1 = (1,2,3)
t2 = 1,2,3
print(t1)
print(t2)
print(t1[1:])