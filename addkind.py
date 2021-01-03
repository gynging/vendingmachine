# -*- coding: utf-8 -*-
import os
import sqlite3
dbfile2 = sqlite3.connect('zibunnkannri.db')
c = dbfile2.cursor()

class Addkinding():

    def addkind(self):
        self.newkind = str(input("なんという飲み物を追加しますか？"))
        repetition3 = None
        while repetition3 == None:
            try:
                addcount = int(input("何本追加しますか？"))
                addprice = int(input("価格はいくらにしますか？"))
                c.execute("INSERT INTO zihannkicount VALUES (?,?,?)", (self.newkind, addcount, addprice))
                c.execute("INSERT INTO mydrinkcount VALUES (?,?)", (self.newkind, 0))
                # c.execute("select * from zihannkicount where　drinkkind = ? ",(self.newkind,))
                # l = c.fetchone()
                # print("l = {}".format(l))
                print("{}を{}本追加しました。".format(self.newkind, addcount))
                repetition3 = 1
            except ValueError:
                print("数値で入力してください")
#addkinding = Addkinding()
#addkinding.addkind()

dbfile2.commit()
dbfile2.close()