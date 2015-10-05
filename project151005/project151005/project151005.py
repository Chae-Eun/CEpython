#class A(): 
#    def __init__(self, a): 
#        self.a = a 
#    def show(self): 
#        print('show:', self.a) 
        
#class B(A): 
#    def __init__(self, b, **arg): 
#        super().__init__(**arg)
#        self.b = b 
#    def show(self): 
#        print('show:', self.b) 
#        super().show() 
        
#class C(A): 
#    def __init__(self, c, **arg): 
#        super().__init__(**arg) 
#        self.c = c 
#    def show(self): 
#        print('show:', self.c) 
#        super().show()

#class D(B,C):
#    def __init__(self, d, **arg):
#        super().__init__(**arg)
#        self.d = d
#    def show(self):
#        print('show:', self.d)
#        super().show()

#data = D(a=1,b=2,c=3,d=4)
#data.show()

#class Mapping:
#    def __init__(self, iterable):
#        self.items_list = []
#        self.__update(iterable)
#    def update(self, iterable):
#        for item in iterable:
#            self.items_list.append(item)
#    # private copy of original update() method
#    __update = update

#class MappingSubclass(Mapping):
#    def update(self, keys, values):
#        # provides new signature for update()
#        # but does not break __init__()
#        for item in zip(keys, values):
#            self.items_list.append(item)

#list = [1, 2, 3, 4]
#keys = ['a', 'b', 'c']
#values = ['d', 'e', 'f']

#data = MappingSubclass(list)
#print(data.items_list)
#data.update(keys, values)
#print(data.items_list)

#number1 = float(input("enter a number : "))
#number2 = float(input("enter a number : "))
#
#try :
#    result = number1 / number2
#    print(result)
#except :
#    print("I am sorry something went wrong")

import sys

#number1 = float(input("enter a number : "))
#number2 = float(input("enter a number : "))

try :
    number1 = float(input("enter a number : "))
    number2 = float(input("enter a number : "))
    result = number1 / number2
    print(result)
except ZeroDivisionError as e :
    print(e)
    print("The answer is infinity")
except :
    error = sys.exc_info()[0]
    print(error)
    #sys.exit()
finally:
    print("Done")