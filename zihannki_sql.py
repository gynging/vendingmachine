# -*- coding: utf-8 -*-
import os
import sqlite3
dbfile2 = sqlite3.connect('zibunnkannri.db')
c = dbfile2.cursor()
"""
メニュー画面を作成
　メニュー内容
　　・自動販売機飲み物購入機能
　　　→ 今まで課題で作成した自動販売機プログラム搭載
　　・販売機編集
　　　→ 以下機能を含んでいる
　　　　　1 自動販売機飲み物個数追加機能
　　　　　　→ 既存の飲み物の個数をユーザーが指定した個数に追加できる
　　　　　2 自動販売機飲み物種類追加機能
　　　　　　→ 既存の飲み物に加えて新しい種類の飲み物を買えるようにする
　　　　　3 自動販売機飲み物種類削除機能
　　　　　　→ 既存の飲み物をユーザーが任意に削除できるようにする
"""

class Zihan:
    def __init__(self):
        self.kin = None
        self.zyusu = {}
        self.kig = None
        self.oturi = None
        self.sagaku = None
        self.yesno = None
        self.modoru = None
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


    def menu(self):
        self.menukind = ["1:自動販売機飲み物購入機能", "2:販売機編集","3:終了する"]
        for self.menulist in self.menukind:
            print(self.menulist)

        while self.control1 == None:
            try:
                self.choicemenu = int(input("どちらかを数字で選んで下さい"))
                #print("debug self.choicemenu = {}".format(self.choicemenu))
                if self.choicemenu == 1:
                    zihann.say_nomitaimono()
                    self.control1 = 1

                elif self.choicemenu == 2:
                    self.editlist = ["1 自動販売機飲み物個数追加機能", "2 自動販売機飲み物種類追加機能", "3 自動販売機飲み物種類削除機能"]
                    for self.editlist2 in self.editlist:
                        print(self.editlist2)

                    self.editcommnd = int(input("1か2か3で選んで下さい"))

                    if self.editcommnd == 1:
                        zihann.addrink()
                        zihann.menu()

                    elif self.editcommnd == 2:
                        zihann.addkind()
                        zihann.menu()

                    elif self.editcommnd == 3:
                        zihann.editdrink()
                        zihann.menu()

                    else:
                            continue

                elif self.choicemenu == 3:
                    zihann.ending()
                    self.control1 = 1

                else:
                    print("1か2か3で選んで下さい。")
            except ValueError:
                print("数値で入力してください。")



    def addrink(self):
        c.execute("select * from zihannkicount")
        o = c.fetchall()
        for i in o:
            print("{}:{}本".format(i[0], i[1]))
        repetition = None
        while repetition == None:
            self.add = str(input("どの飲み物を追加しますか？"))
            c.execute("select * from zihannkicount where drinkkind = ? ", (self.add,))
            m = c.fetchone()
            #print("m = {}".format(m))
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
                        print("{}が{}本になりました。".format(self.add,newcount))
                        repetition = 1
                        repetition2 = 1
                    except ValueError:
                        print("数値を入力してください。")

    def addkind(self):
        self.newkind = str(input("なんという飲み物を追加しますか？"))
        repetition3 = None
        while repetition3 == None:
            try:
                addcount = int(input("何本追加しますか？"))
                addprice = int(input("価格はいくらにしますか？"))
                c.execute("INSERT INTO zihannkicount VALUES (?,?,?)",(self.newkind,addcount,addprice))
                c.execute("INSERT INTO mydrinkcount VALUES (?,?)", (self.newkind,0))
                #c.execute("select * from zihannkicount where　drinkkind = ? ",(self.newkind,))
                #l = c.fetchone()
                #print("l = {}".format(l))
                print("{}を{}本追加しました。".format(self.newkind,addcount))
                repetition3 = 1
            except ValueError:
                print("数値で入力してください")

    def editdrink(self):
        c.execute("select * from zihannkicount")
        p = c.fetchall()
        #print("p = {}".format(p))
        for i in p:
            print(i)
        while True:
            self.deletedrink = str(input("なんという飲み物を消去しますか？"))
            c.execute("select * from zihannkicount where drinkkind = ? ", (self.deletedrink,))
            wantdelete = c.fetchone()
            if wantdelete != None:
                c.execute("delete from zihannkicount where drinkkind = ?",(self.deletedrink,))
                c.execute("select * from zihannkicount")
                d = c.fetchall()
                print(d)
                break
            else:
                print("選択した飲み物は存在しません。")


    def say_nomitaimono(self):

        c.execute("select drinkkind,price from zihannkicount")
        p = c.fetchall()
        #print("p = {}".format(p))

        for redict in p:
            self.zyusu[redict[0]] = redict[1]
            #print("これはデバック{}".format(self.zyusu))
            print("{}:{}円".format(redict[0], redict[1]))
        while True:
            self.kin = str(input("飲みたい物を入力してください"))

            if self.kin in self.zyusu:
                c.execute("select * from zihannkicount where drinkkind = ? ",(self.kin,))
                self.d = c.fetchone()
                #print("d = {}".format(d))
                self.a = int(self.d[1])

                if self.a != 0:

                    print("{}の在庫数は{}個です。".format(self.kin,self.a))
                    self.b = int(self.d[2])
                    zihann.honnsuu()

                    zihann.nyukin()
                    break
                else:
                    print("在庫数が足りません。")
            else:
                print("在庫がありません")

        zihann.tudukemasuka()

    def honnsuu(self):
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

    def nyukin(self):

        while True:
            try:
                self.kig = int(input("お金を投入してください"))
                self.realprice = int(self.zyusu[self.kin]) * int(self.countdrink)
                #print("これはデバックrealprice = {}".format(self.realprice))

                if int(self.realprice) <= self.kig:
                    self.oturi = self.kig - self.realprice
                    if self.oturi == 0:
                        print("お釣りは有りません")
                        self.f = int(self.d[1]) - int(self.countdrink)
                        c.execute("update zihannkicount set buycount=? where drinkkind=?", (self.f, self.kin))
                        c.execute("select * from mydrinkcount where drinkkind = ?", (self.kin,))
                        self.g = c.fetchone()
                        #print("これはデバックself.g = {}".format(self.g))
                        self.h = int(self.g[1]) + int(self.countdrink)
                        c.execute("update mydrinkcount set buycount=? where drinkkind=?", (self.h, self.kin))
                        c.execute("select * from mydrinkcount where drinkkind = ?", (self.kin,))
                        self.i = c.fetchone()
                        print("{0}の購入数はこれで{1}本目です".format(self.kin, self.i[1]))
                        break
                    else:
                        print("お釣りは{}".format(self.oturi))
                        self.f = int(self.d[1]) - int(self.countdrink)
                        c.execute("update zihannkicount set buycount=? where drinkkind=?", (self.f, self.kin))
                        c.execute("select * from mydrinkcount where drinkkind = ?", (self.kin,))
                        self.g = c.fetchone()
                        self.h = int(self.g[1]) + int(self.countdrink)
                        c.execute("update mydrinkcount set buycount=? where drinkkind=?", (self.h, self.kin))
                        c.execute("select * from mydrinkcount where drinkkind = ?", (self.kin,))
                        self.i = c.fetchone()
                        print("{0}の購入数はこれで{1}個目です".format(self.kin, self.i[1]))
                        break
                else:
                    self.sagaku = int(self.realprice) - int(self.kig)
                    #self.sagaku2 = str(self.sagaku)
                    print("お金が{}円足りません。".format(self.sagaku))

            except ValueError:
                print("数値で入力してください")


    def tudukemasuka(self):
        self.modoru = None
        while self.modoru == None:

            self.yesno = input("購入を続けますか？yesかnoで入力して下さい。")

            if self.yesno == "yes":
                os.system('clear')
                self.modoru = 1
                zihann.say_nomitaimono()

            elif self.yesno == "no":
                print("お疲れ様でした")
                self.modoru = 1
                zihann.menu()



            else:
                print("yesかnoで入力して下さい")


    def ending(self):
        while True:
            self.endmessage = input("終了しますか？yes or no")

            if self.endmessage == "yes":
                print("またのご利用お待ちしております。")
                break
            elif self.endmessage == "no":
                zihann.menu()
                break
            else:
                print("yesかnoで入力してください。")





zihann = Zihan()

zihann.menu()

dbfile2.commit()
dbfile2.close()








