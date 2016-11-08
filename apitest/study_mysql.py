# coding=utf-8
__author__ = 'sherry'


import MySQLdb


conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '',
    db = 'automind'
)

curs = conn.cursor()

# curs.execute('create table resume(id varchar(20), chinese_name VARCHAR(20))')

sql = 'insert into resume values(%s, %s)'

 curs.execute(sqli, ('4', u'王二小'))

curs.close()
conn.commit()
conn.close()