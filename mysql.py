
import pymysql.cursors

mysql = pymysql.connect(host='localhost',
                       user='root',
                       password='123456',
                       db='rent_company',
                       charset='utf8')

cursor = mysql.cursor()

sql = "select * from Customer"
cursor.execute(sql)

for i in cursor.fetchall():
    print(i)
print('共查询到：', cursor.rowcount, '条数据。')