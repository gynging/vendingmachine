# -*- coding: utf-8 -*-
import os
from say_nomitaimono import Zihan
from adddrink import Addrinking
from addkind import Addkinding
from editdrink import Editing

control1 = None
while control1 == None:
    menukind = ["1:自動販売機飲み物購入機能", "2:販売機編集", "3:終了する"]
    for menulist in menukind:
        print(menulist)

    try:
        choicemenu = int(input("どちらかを数字で選んで下さい"))
                # print("debug self.choicemenu = {}".format(self.choicemenu))
        if choicemenu == 1:
            zihann = Zihan()
            zihann.say_nomitaimono()

        elif choicemenu == 2:
            editlist = ["1 自動販売機飲み物個数追加機能", "2 自動販売機飲み物種類追加機能", "3 自動販売機飲み物種類削除機能"]
            for editlist2 in editlist:
                print(editlist2)

            editcommnd = int(input("1か2か3で選んで下さい"))

            if editcommnd == 1:
                addrinking = Addrinking()
                addrinking.addrink()

            elif editcommnd == 2:
                addkinding = Addkinding()
                addkinding.addkind()

            elif editcommnd == 3:
                editing = Editing()
                editing.editdrinking()


            else:
                continue

        elif choicemenu == 3:
            while True:
                try:
                    endmessage = str(input("終了しますか？yes or no"))

                    if endmessage == "yes":
                        print("またのご利用お待ちしております。")
                        control1 = 1
                        break
                    elif endmessage == "no":
                        break

                    else:
                        print("yesかnoで入力してください。")

                except ValueError:
                    print("数値を入れないでください。")

        else:
            print("1か2か3で選んで下さい。")
    except ValueError:
        print("数値で入力してください。")













