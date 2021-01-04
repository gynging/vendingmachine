# -*- coding: utf-8 -*-
import os
import sqlite3


class Editing():

    def editdrinking(self):
        dbfile2 = sqlite3.connect('zibunnkannri.db')
        c = dbfile2.cursor()
        c.execute("select * from zihannkicount")
        p = c.fetchall()
        # print("p = {}".format(p))
        for i in p:
            print(i)
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