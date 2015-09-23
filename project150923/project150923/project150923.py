
from abc import ABCMeta, abstractmethod

#class HousePark:
#    lastname = "박"
#    def __init(self, name):
#        self.fullname = self.lastname + name
#    def travel(self, where):
#        print("%s, %s 여행을 가다."%(self.fullname, where))

#class HouseKim(HousePark):
#    lastname = "김"
#    def __init__(self, name, age):
#        HousePark.__init__(self, name)
#        self.age = age
#    def travel(self, where, day):
#        HousePark.travel(self, where)
#        print("%s, %d살에 %s여행 %d일 가네."%(self.fullname, self.age, where, day))

#class A:
#    def __init__(self):
#        print("A 생성자 호출")
#class B:
#    def __init__(self):
#        print("B 생성자 호출")
#class C(A, B):
#    def __init__(self):
#        A.__init__(self)
#        B.__init__(self)
#        print("C 생성자 호출")

#class Terran(metaclass=ABCMeta):
#    def __init__(self, name):
#        slef.name = name
#    @abstractmethod
#    def attack(self):
#        pass

#class Tank(Terran):
#    def __init__(self, name, damage):
#        super().__init__(self, name)
#        self.damage = damage

#    def attack(self):
#        print("탱크를 쏩니다.")

#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(self, name)
#        self.hp = hp

#    def attack(self):
#        print("총를 쏩니다.")

#def Attack(terran):
#    terran.attack()

#T1 = Tank("tank", 0)
#M1 = Marine("marine", 200)

#tlist = [Tank("tank1", 0), Tank("tank2", 50), Marine("marine1", 300)]
#for item in tlist:
#    Attack(item)

#Attack(T1)
#Attack(M1)

class MyList(list):
    name=""
    def __init__(self, name):
        super().__init__([])
        self.name = name
    def __str__(self):
        return self.name+":"+super().__str__()

list1 = MyList("greenjoa")
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
print(list1)
#print(dir(list1))

# a1+10 (add 재정의)
# 10+a1 (radd 재정의)