import sqlite3
con = sqlite3.connect("test.db")
con1 = sqlite3.connect("test.db")

cur=con.cursor()
#dropsql='''drop table if exists phonebook;'''
#cur.execute(dropsql)

#sql='''create table if not exists
#           phonebook(name text, phonenum text);'''
#cur.execute(sql)

#insertsql='''insert into phonebook
#                values('bluejoa1', '010-3333-4444');'''
#cur.execute(insertsql)

#insertsql='''insert into phonebook
#                values('greenjoa1', '010-3333-4444');'''
#cur.execute(insertsql)

#insertsql='''insert into phonebook
#                values('skyjoa1', '010-3333-4444');'''
#cur.execute(insertsql)

#cur.execute("select * from phonebook;")
#for row in cur:
#    print(row)
#    print(row[0])
#print(cur.fetchone())
#print(cur.fetchmany(2))
#print(cur.fetchall())

#name='redjoa2'
#phonenumber='010-7777-8888'
#insertsql='''insert into phonebook values(?,?);'''
#cur.execute(insertsql, (name, phonenumber))
#cur.execute("select * from phonebook;")
#print(cur.fetchall())

#name='yellowjoa1'
#phonenumber='010-2222-3333'
#insertsql='''insert into phonebook
#               values(:inputname, :inputnum);'''
#cur.execute(insertsql, {"inputnum":phonenumber, "inputname":name})
#cur.execute("select * from phonebook;")
#print(cur.fetchall())

#insertsql='''insert into phonebook values(?,?);'''
#datalist=(('greenjoa4','010-4444-4444'),('greenjoa5','010-5555-5555'))
#cur.executemany(insertsql, datalist)
#cur.execute("select * from phonebook;")
#print(cur.fetchall())

#def datagenerator():
#    datalist=(('bluejoa4','010-4444-4444'),('bluejoa5','010-5555-5555'))
#    for item in datalist:
#        yield item
#cur.executemany(insertsql, datagenerator())
#cur.execute("select * from phonebook;")
#print(cur.fetchall())
#con.commit()

con.isolation_level=None

#cur.execute("select * from phonebook order by name;")
#print(cur.fetchall())
#cur.execute("select * from phonebook order by name desc;")
#print(cur.fetchall())
#name='redjoa2'
#phonenumber='010-7777-8888'
#insertsql='''insert into phonebook values(?,?);'''
#cur.execute(insertsql, (name, phonenumber))
#cur.execute("select * from phonebook order by name;")
#print(cur.fetchall())

#def orderfunc(str1, str2):
#    s1 = str1.upper()
#    s2 = str2.upper()
#    return (s1 > s2) -(s1 < s2) # 앞(음수), 같음(0), 뒤(양수)
#con.create_collation('myordering', orderfunc)
#cur.execute("select * from phonebook order by name collate myordering;")
#print(cur.fetchall())

#cur.execute("insert into phonebook(phonenum) values('010-9999-9999');")

#cur.execute("select count(*) from phonebook;")
#print(cur.fetchone()[0])

#cur.execute("select count(name) from phonebook;")
#print(cur.fetchone()[0])

sql='''create table if not exists
           user(name text, age integer);'''
cur.execute(sql)

#insertsql='''insert into user values(?,?);'''
#datalist=(('hi','23'),('hello','17'),('lulu','35'),('mimi','28'))
#cur.executemany(insertsql, datalist)
cur.execute("select * from user;")
print(cur.fetchall())

#제일 높은 나이의 쿼리만 출력 어떻게 하지?
cur.execute("select * from user;")
print(cur.fetchone()[0])

cur.execute("select min(age) from user;")
print(cur.fetchone()[0])

class Average:
    def __init__(self):
        self.sum = 0
        self.cnt = 0

    def step(self, value):
        self.sum += value
        self.cnt += 1

    def finalize(self):
        return self.sum/self.cnt

cur1=con1.cursor()
con1.create_aggregate("avg", 1, Average)
cur1.execute("select avg(Age) from user;")
print(cur1.fetchall())