#class Service:
#    secret = "hi"
#    def sum(self, a, b):
#        result=a+b
#        print("%s + %s = %s 입니다."%(a, b, result))

#pey = Service()
#print(pey.secret)

#pey.sum(1,1)
#Service.sum(pey, 1, 3)

#class Service:
#    secret = "hi"
#    def _init_(self, name, value=0):
#        self.name = name
#        self.value = value
#        self.secret = name
#    def sum(self, a, b):
#        result=a+b
#        print("%s + %s = %s 입니다."%(self.name, a, b, result))

#pey = Service()
#Service._init_(pey, "gg", 0)
#Service.sum(pey, 1, 1)

#class Movie:
#    title=""
#    director=""
#    def _init_(self, title, director):
#        self.title = title
#        self.director = director

#    def showInfo(self):
#        print(self.title + " " + self.director)

#test = Movie()
#test._init_("암살", "전지현")
#test.actor = "하정우"
#Movie.showInfo(test)

#example = Movie()
#example.title = "베테랑"
#example.director = "황정민"
#print(example.actor)

#coding:cp949


class Movie:
    '''영화 클래스입니다.'''
    count = 0
    title="암살"
    director="최동훈"
    def __init__(self, title, director):
        self.title = title
        self.director = director
        Movie.count+=1
        print(self.title + " 생성자 호출")

    def __del__(self):
        print(self.title + " 소멸자 호출")

    def showInfo(self):
        print(self.title + " " + self.director)

    @staticmethod #클래스 정보가 안 들어옴
    def showCount1():
        print(Movie.count)

    @classmethod
    def showCount2(cls):
        print(cls.count)

#m1 = Movie("베테랑","류승완")
#print(m1.title)
#print(m1.__doc__) #영화 클래스입니다.

#m1 = Movie("베테랑1","류승완1")
#m2 = Movie("베테랑2","류승완2")
#m3 = Movie("베테랑3","류승완3")
#m4 = Movie("베테랑4","류승완4")
#print(type(m4))
#print(id(m4))
#m4 = m3 #아무도 m4에 대한 객체를 참조하지 않기 때문에 소멸자 호출
#모든 대입연산은 얕은 복사
#print(id(m4))
#print(id(m3))
#m4.showInfo()

m1 = Movie("a", "b")
m2 = Movie("c", "d")
m3 = Movie("e", "f")
m4 = Movie("g", "h")
m5 = Movie("i", "j")

#print(m1.count)
#print(m2.count)

Movie.showCount1()
Movie.showCount2()