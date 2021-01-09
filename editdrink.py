# -*- coding: utf-8 -*-
import os
import sqlite3


class Editing():
    def __init__(self):
        self.zyusuall = {}

    def editdrinking(self):
        dbfile2 = sqlite3.connect('zibunnkannri.db')
        c = dbfile2.cursor()
        c.execute("select * from zihannkicount")
        p = c.fetchall()
        #print("debag:p = {}".format(p))
        for i in p:
            #print("これはデバック{}".format(i))
            self.zyusuall[i[0]] = i[2]
            print("{}:{}円".format(i[0], i[2]))

        while True:
            self.deletedrink = str(input("なんという飲み物を消去しますか？"))
            c.execute("select * from zihannkicount where drinkkind = ? ", (self.deletedrink,))
            wantdelete = c.fetchone()
            if wantdelete != None:
                c.execute("delete from zihannkicount where drinkkind = ?", (self.deletedrink,))
                c.execute("select * from zihannkicount")
                d = c.fetchall()
                print(d)
                break
            else:
                print("選択した飲み物は存在しません。")
#editing = Editing()
#editing.editdrinking()

        dbfile2.commit()
        dbfile2.close()