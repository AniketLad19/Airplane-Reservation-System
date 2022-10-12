import pymysql as p

def connect():
    return p.connect(host="localhost",user="root",passwd="",db="demo")

def insert(t):
    con=connect()
    cur=con.cursor()
    sql="insert into details values (%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def sendcontact(a):
    con=connect()
    cur=con.cursor()
    sql="insert into contact values (%s,%s,%s,%s)"
    cur.execute(sql,a)
    con.commit()
    con.close()

def select(email):
    con=connect()
    cur=con.cursor()
    sql="select email,password from details where email=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def reserve(r):
    con=connect()
    cur=con.cursor()
    print(r)
    sql="insert into booking values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,r)
    con.commit()
    con.close() 

def user_details():
    con=connect()
    cur=con.cursor()
    sql="select* from booking"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data


def take(email):
    con=connect()
    cur=con.cursor()
    sql="select * from booking where email=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
