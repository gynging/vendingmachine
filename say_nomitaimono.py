# -*- coding: utf-8 -*-
import os
import sqlite3
import os


class Zihan:


    def __init__(self):
        self.kin = None
        self.zyusu = {}
        self.kig = None
        self.oturi = None
        self.sagaku = None
        self.yesno = None
        self.owariflag = None
        self.menukind = None
        self.menukist = None
        self.choice = None
        self.choicekind = None
        self.choicemenu = None
        self.add = None
        self.kind = None
        self.newkind = None
        self.deletedrink = None
        self.editlist = None
        self.editlist2 = None
        self.control1 = None
        self.control2 = None
        self.menuback = None
        self.countdrink = None
        self.someprice = None
        self.realprice = None
        self.a = None
        self.b = None
        self.sagaku = None
        self.d = None
        self.f = None
        self.h = None
        self.i = None
        self.g = None
        self.sagaku2 = None
        self.endmessage = None
        self.control = None
        self.modoru = None

    def say_nomitaimono(self):
        dbfile2 = sqlite3.connect('zibunnkannri.db')
        c = dbfile2.cursor()
        c.execute("select drinkkind,price from zihannkicount")
        p = c.fetchall()
        # print("p = {}".format(p))
        self.control = None
        while self.control == None:
                for redict in p:
                    self.zyusu[redict[0]] = redict[1]
                    # print("これはデバック{}".format(self.zyusu))
                    print("{}:{}円".format(redict[0], redict[1]))

                self.kin = str(input("飲みたい物を入力してください"))

                if self.kin in self.zyusu:
                    c.execute("select * from zihannkicount where drinkkind = ? ", (self.kin,))
                    self.d = c.fetchone()
                    # print("d = {}".format(d))
                    self.a = int(self.d[1])

                    if self.a != 0:

                        print("{}の在庫数は{}個です。".format(self.kin, self.a))
                        self.b = int(self.d[2])
                        while True:
                            try:
                                self.countdrink = int(input("何本購入しますか？"))
                                if self.a >= self.countdrink:
                                    self.someprice = self.b * self.countdrink
                                    print("合計金額は{}円になります。".format(self.someprice))
                                    break

                                else:
                                    print("申し訳ございません。在庫切れです。")
                            except ValueError:
                                print("数値で入力してください。")
                        self.control2 = None
                        while self.control2 == None:
                            try:
                                self.kig = int(input("お金を投入してください"))
                                self.realprice = int(self.zyusu[self.kin]) * int(self.countdrink)
                                # print("これはデバックrealprice = {}".format(self.realprice))

                                if int(self.realprice) <= self.kig:
                                    self.oturi = self.kig - self.realprice
                                    if self.oturi == 0:
                                        print("お釣りは有りません")
                                        self.f = int(self.d[1]) - int(self.countdrink)
                                        c.execute("update zihannkicount set buycount=? where drinkkind=?",(self.f, self.kin))
                                        c.execute("select * from mydrinkcount where drinkkind = ?", (self.kin,))
                                        self.g = c.fetchone()
                                        # print("これはデバックself.g = {}".format(self.g))
                                        self.h = int(self.g[1]) + int(self.countdrink)
                                        c.execute("update mydrinkcount set buycount=? where drinkkind=?",(self.h, self.kin))
                                        c.execute("select * from mydrinkcount where drinkkind = ?", (self.kin,))
                                        self.i = c.fetchone()
                                        print("{0}の購入数はこれで{1}本目です".format(self.kin, self.i[1]))
                                        self.control2 = 1
                                        self.control = 1
                                        zihann = Zihan()
                                        zihann.back()

                                    else:
                                        print("お釣りは{}".format(self.oturi))
                                        self.f = int(self.d[1]) - int(self.countdrink)
                                        c.execute("update zihannkicount set buycount=? where drinkkind=?",(self.f, self.kin))
                                        c.execute("select * from mydrinkcount where drinkkind = ?", (self.kin,))
                                        self.g = c.fetchone()
                                        self.h = int(self.g[1]) + int(self.countdrink)
                                        c.execute("update mydrinkcount set buycount=? where drinkkind=?",(self.h, self.kin))
                                        c.execute("select * from mydrinkcount where drinkkind = ?", (self.kin,))
                                        self.i = c.fetchone()
                                        print("{0}の購入数はこれで{1}個目です".format(self.kin, self.i[1]))
                                        self.control2 = 1
                                        self.control = 1
                                        zihann = Zihan()
                                        zihann.back()

                                else:
                                    self.sagaku = int(self.realprice) - int(self.kig)
                                    # self.sagaku2 = str(self.sagaku)
                                    print("お金が{}円足りません。".format(self.sagaku))

                            except ValueError:
                                print("数値で入力してください")
                    else:
                        print("在庫数が足りません。")
                else:
                    print("在庫がありません")
        dbfile2.commit()

    def back(self):
        dbfile2 = sqlite3.connect('zibunnkannri.db')
        c = dbfile2.cursor()
        self.modoru = None
        while self.modoru == None:
            try:
                self.yesno = str(input("購入を続けますか？yesかnoで入力して下さい。"))

                if self.yesno == "yes":
                    self.modoru = 1
                    zihann = Zihan()
                    zihann.say_nomitaimono()

                elif self.yesno == "no":
                    print("お疲れ様でした")
                    self.modoru = 1
                    dbfile2.close()

                else:
                    print("yesかnoで入力して下さい")

            except ValueError:
                print("yesかnoで入力して下さい")







