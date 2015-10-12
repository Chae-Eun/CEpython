import glob
import os.path

#print(glob.glob("*.py"))

#for i in glob.iglob('*'):
#    print(i)

#ndir = nfile = 0
#def traverse(dir, depth):
#    global ndir, nfile
#    for obj in glob.glob(dir + '/*'):
#        if depth == 0:
#            prefix = '|--'
#        else:
#            prefix = '|' + ' '* depth + '|--'
#        if os.path.isdir(obj):
#            ndir += 1
#            print(prefix + os.path.basename(obj))
#            traverse(obj, depth+1)
#        elif os.path.isfile(obj):
#            nfile += 1
#            print(prefix + os.path.basename(obj))
#        else:
#            print(prefix + 'unknown object:', obj)

#if __name__ == '__main__':
#    traverse("../..", 0)
#    print('\n',ndir,'directories,',nfile,'files')

import tempfile

#with tempfile.TemporaryFile('w+', delete=False) as fp:
#    fp.write('Hello world!')
#    fp.seek(0)
#    data = fp.read()
#    data2 = fp.name
#    print(data, data2)

import time

#t1 = time.time()
#time.sleep(10)
#t2 = time.time()
#spendtime = t2 - t1
#print(spendtime)

#print(time.strftime("%B %dth %A %I:%M", time.localtime()))

#time1 = time.ctime(1234567)
#t = time.strptime(time1)
#print(t)
#print(time1)

import calendar

#calendar.calendar(2000)
#calendar.prcal(2000)

#a=calendar.weekday(2015, 10, 15)
#print(a)
#b=calendar.monthrange(2015, 10)
#print(b)

import random

#c = random.choice([1,2,3,4])
#print(c)
#d = random.shuffle()
#print(d)
#e = random.sample(range(100), 10)
#print(e)
#random.shuffle(e)
#g = random.choice(e)
#print(e)
#print(g)

#data = [('Red', 3), ('Blue',1), ('Green',4), ('Yellow',2)]
#datalist=[]
#for val, cnt in data:
#    for i in range(cnt):
#        datalist.append(val)

#print(datalist)

import webbrowser
#url='http://google.com'
#webbrowser.open_new_tab(url)
#webbrowser.open_new(url)
