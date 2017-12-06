import configparser
from flask import Flask
import pymysql
app=Flask(__name__)
cf = configparser.ConfigParser()
cf.read('flaskr.conf')
sec = cf.sections()
print('sections = %s' % sec)
opts = cf.options('USER')
print('opts = %s' % opts)
print(cf['USER']['USERNAME'])


conn = pymysql.connect(host='127.0.0.1',user='root', password='mysql', database='test')
cursor = conn.cursor()
print(1)
cursor.execute('''drop table if exists entries2;
    create table entries2 (
    id INT  primary key AUTO_INCREMENT,
                        title VARCHAR(20) not null,
                                          text VARCHAR(40) not null
);''')
print(2)
cursor.execute('insert into entries2 values (7,\'title7\',\'text7\')')
print(3)
cursor.execute('insert into entries2 values (8,\'title8\',\'text8\')')
print(4)
conn.commit()
cursor.execute('select title, text from entries2 order by id desc')
aa=cursor.fetchall()
print(aa)

bb=[dict(title=row[0], text=row[1]) for row in aa]
print(bb)



