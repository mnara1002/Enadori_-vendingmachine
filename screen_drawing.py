#coding:utf8
import Tkinter as tk
from tkMessageBox import showinfo

class screen():
    def __init__(self):
        pass



    def create_screen(self):
        root = tk.Tk()#メイン画面作成
        root.title("エナドリ自販機") #メインタイトル
        root.geometry("250x200")#メインタイトルの高さx幅を指定
        description = tk.Message(width="150", text = "コインを入れてください(^_^)\n飲み物は200円です。")#中に表示する説明文を設定
        buttun_buydrink = tk.Button(root,text="飲み物を買う", width="10")#飲み物を買うボタン
        buttun_putmoney100 = tk.Button(root,text="100円入れる", width="10")#100円入れるボタン

        description.pack()#メッセージを表示させるための処理

        description.place(x=0,y=0)#メッセージをどこに表示させるかを指定
        buttun_buydrink.place(x=10,y=100)
        buttun_putmoney100.place(x=110,y=100)
        root.mainloop()#メイン画面を表示

