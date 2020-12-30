# coding=utf-8
import sqlite3
dbfile2 = sqlite3.connect('zibunnkannri.db')
c = dbfile2.cursor()
"""
#c.execute("drop table zihannkicount;")
c.execute("create table zihannkicount(drinkkind,buycount,price)")
c.execute("INSERT INTO zihannkicount VALUES ('コーラ','10','100')")
c.execute("INSERT INTO zihannkicount VALUES ('ソーダ','10','150')")
c.execute("INSERT INTO zihannkicount VALUES ('オレンジジュース','10','300')")
c.execute("select * from zihannkicount")
d = c.fetchall()#確認している
print(d)
"""

"""
c.execute("create table mydrinkcount(drinkkind,buycount)")
c.execute("INSERT INTO  mydrinkcount VALUES ('コーラ','10')")
c.execute("INSERT INTO mydrinkcount VALUES ('ソーダ','10')")
c.execute("INSERT INTO mydrinkcount VALUES ('オレンジジュース','10')")
"""
"""
c.execute("update mydrinkcount set buycount=? where drinkkind=?",(e,d[0]))
c.execute("select * from mydrinkcount where drinkkind = 'コーラ'")
print(c.fetchone())
"""





c.execute("select * from zihannkicount")
names = list(map(lambda x: x[0], c.description))
print(names)
for x in c.fetchall():
    print(x)

c.execute("select * from mydrinkcount")
names = list(map(lambda x: x[0], c.description))
print(names)
for x in c.fetchall():
    print(x)


dbfile2.commit()
dbfile2.close()
