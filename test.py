# coding: UTF-8
from modules import ScreenShot
import tkinter

class app(tkinter.Frame):
  def screen_capture():
    ScreenShot()

root = tkinter.Tk()
# フォーム
root.title("すぐぐる")
root.geometry("500x700")

label = tkinter.Label(root, text="")
label.pack()
# テキストボックス
frame = tkinter.Frame(root)
frame.pack(fill = tkinter.BOTH)
button = tkinter.Button(frame, 
                        text="ボタン", 
                        command=app.screen_capture, 
                        bg='#f0e68c', 
                        height=2, 
                        width=20)
button.pack()

# テキストボックス
txt = tkinter.Text()
txt.pack()

root.mainloop()