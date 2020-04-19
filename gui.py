from  tkinter import  messagebox,scrolledtext

import pymysql.cursors
from  tkinter import *

def Enterprise_owner():
    mysql = pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='rent_company',
                           charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from Enterprise_owner"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('Enterprise_owner')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def Branch_Office():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from Branch_Office"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('Branch_Office')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def Staff():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from Staff"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('Staff')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def Customer():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from Customer"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('Customer')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def Private_owener():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from Private_owener"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('Private_owener')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def House_property():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from House_property"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('House_property')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def Advertisement():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from Advertisement"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('Advertisement')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def News():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from News"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('News')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def Ad_details():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from Ad_details"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('Ad_details')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def Record():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from Record"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('Record')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def Rent_contract():
    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123456',
                            db='rent_company',
                            charset='utf8')

    cursor = mysql.cursor()
    sql0 = "select * from Rent_contract"
    cursor.execute(sql0)
    text = ""
    top = Tk()
    top.title('Rent_contract')
    top.geometry("500x500+100+100")
    n = 0
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

root = Tk()
root.title('Rent_company')
toolbar = Frame(root, height=0, bg='lemonchiffon')
root.geometry("1000x500+100+100")

Label(root, text='Rent_company', font=('微软雅黑', 36),compound='center').place(x=135, y=40)

shortButton = Button(toolbar, text='Enterprise_owner', command=Enterprise_owner)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar, text='Private_owener', command=Private_owener)
shortButton.pack(side=LEFT, padx=10, pady=5)
toolbar.pack(expand=NO, fill=X)

shortButton = Button(toolbar, text='House_property', command=House_property)
shortButton.pack(side=LEFT, padx=13, pady=5)

shortButton = Button(toolbar, text='Customer', command=Customer)
shortButton.pack(side=LEFT, padx=13, pady=5)

shortButton = Button(toolbar, text='Staff', command=Staff)
shortButton.pack(side=LEFT, padx=13, pady=5)

shortButton = Button(toolbar, text='Record', command=Record)
shortButton.pack(side=LEFT, padx=13, pady=5)

Label(root, text='satff_by_con_id', font=('微软雅黑', 20)).place(x=30, y=350)
Label(root, text='add_Pri_owner', font=('微软雅黑', 20)).place(x=30, y=400)

textPad = Text(root, undo=True)
textPad.place(x=260, y=360, height=30, width=200)

textPad0 = Text(root, undo=True)
textPad0.place(x=260, y=410, height=30, width=200)

textPad1 = Text(root, undo=True)
textPad1.place(x=480, y=410, height=30, width=200)

textPad2 = Text(root, undo=True)
textPad2.place(x=700, y=410, height=30, width=200)

##单表查询
def search_customer_by_id():
    searches = textPad.get(1.0, END).strip()
    top = Tk()
    top.title('search_customer_by_id')
    top.geometry("500x400+100+100")
    n = 0
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='991218',
                           db='rent_company',
                           charset='utf8')
    # 创建一个游标
    cursor = mysql.cursor()
    # int id = int(searches)
    cursor.execute("SELECT * FROM Customer WHERE area = % s", searches)
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

##多表查询 通过租约编号查询签订该合约的员工
def search_stff_by_contract_id():
    searches = textPad.get(1.0, END).strip()
    top = Tk()
    top.title('search_stff_by_contract_id')
    top.geometry("500x400+100+100")
    n = 0
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='991218',
                           db='rent_company',
                           charset='utf8')
    # 创建一个游标
    cursor = mysql.cursor()
    # int id = int(searches)
    cursor.execute("SELECT * FROM Staff,Rent_contract WHERE Staff_id = Contract_id", searches)
    for i in cursor.fetchall():
        print(str(i))
        n = n + 18
        Label(top, text=i, font=('楷体', 10)).place(x=135, y=n)
    cursor.close()  # 关闭游标
    mysql.close()  # 关闭连接

def add_Private_owner():
    Owner_id = "4"
    Title = textPad0.get(1.0, END).strip()
    Tel = textPad1.get(1.0, END).strip()
    Address = textPad2.get(1.0, END).strip()
    cursor = mysql.cursor()
    cursor.execute("insert into Private_owner values(%s,%s,%s,%s)", [Owner_id,Title, Tel, Address])
    mysql.commit()
    cursor.execute("SELECT * FROM Private_owner WHERE Owner_id = 4")
    result = cursor.fetchall()
    print(result)
    messagebox.showinfo("info", "Appreciate your evaluation!")

shortButton = Button(root, text='OK', font=('微软雅黑', 13), command=search_customer_by_id)
shortButton.place(x=900, y=355)

shortButton = Button(root, text='OK', font=('微软雅黑', 13), command=add_Private_owner)
shortButton.place(x=900, y=405)

root.mainloop()
