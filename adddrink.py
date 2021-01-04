# -*- coding: utf-8 -*-
import os
import sqlite3


class Addrinking():

    def addrink(self):
        dbfile2 = sqlite3.connect('zibunnkannri.db')
        c = dbfile2.cursor()
        c.execute("select * from zihannkicount")
        o = c.fetchall()
        #print("これはデバック{}".format(o))
        for i in o:
            print("{}:{}本".format(i[0], i[1]))
        repetition = None
        while repetition == None:
            self.add = str(input("どの飲み物を追加しますか？"))
            c.execute("select * from zihannkicount where drinkkind = ? ", (self.add,))
            m = c.fetchone()
            # print("m = {}".format(m))
            if m == None:
                print("入力した飲み物は存在しません。")
            else:
                repetition2 = None
                while repetition2 == None:
                    try:
                        count = int(input("何本追加しますか？"))
                        newcount = m[1]
                        newcount = newcount + count
                        c.execute("update zihannkicount set buycount=? where drinkkind=?", (newcount, self.add))
                        print("{}が{}本になりました。".format(self.add, newcount))
                        repetition = 1
                        repetition2 = 1
                    except ValueError:
                        print("数値を入力してください。")

        dbfile2.commit()
        dbfile2.close()
