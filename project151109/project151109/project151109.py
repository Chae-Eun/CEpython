import sqlite3 as sqlite
from werkzeug import check_password_hash, generate_password_hash
import pymysql as mysql

def get_db():
    db = sqlite.connect("test.db") 
    return db

def init_db():
    db = sqlite.connect("test.db")
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
        db.commit()

def menu():
    while 1:
        print('''회원가입&로그인 연습
        1. 회원가입
        2. 로그인
        3. db읽기''')
        select = int(input())
        if select == 1:
            register()
        elif select == 2:
            login()
        elif select == 3:
            read_db()
        else:
            print("bye!")
            break

def register():
    print("*****회원가입*****")
    while 1:
        print("user id : ", end="")
        userid = input()
        db = get_db()
        cur = db.cursor()
        cur.execute("select * from user where userid=?;", [userid])
        if cur.fetchone() == None:
            print("사용가능합니다.")
            break   
        else:
            print("이미 존재합니다.")
            continue
    print("user name : ", end="")
    username = input()
    print("user passwd : ", end="")
    userpassswd = input()
    insertsql="insert into user (userid, username, userpw) values(?, ?, ?)"
    cur.execute(insertsql, [userid, username, generate_password_hash(userpassswd)])
    db.commit()
    db.close()

def read_db():
    db = get_db()
    cur = db.cursor()
    cur.execute("select * from user;")
    for row in cur:
        print(row)
    print("")

def login():
    db = get_db()
    cur = db.cursor()
    print("******로그인******")
    while 1:
        print("id : ", end="")
        userid = input()
        cur.execute("select * from user where userid=?;", [userid])
        if cur.fetchone() == None:
            print("존재하지 않는 아이디입니다.")
            continue   
        else:
            break
    while 1:
        print("password : ", end="")
        userpw = input()
        cur.execute("select userpw from user where userid=?;", [userid])
        a = cur.fetchone()
        if check_password_hash(a[0], userpw):
            print("로그인 성공!")
            break
        else:
            print("로그인 실패!")
            continue

menu()