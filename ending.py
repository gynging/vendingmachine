# -*- coding: utf-8 -*-
import os
import sqlite3
dbfile2 = sqlite3.connect('zibunnkannri.db')
c = dbfile2.cursor()


def ending1(self):
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


dbfile2.commit()
dbfile2.close()
