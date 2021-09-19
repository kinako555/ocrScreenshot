# coding: UTF-8
from PIL import Image, ImageTk

import tkinter
import time
import pyautogui

class app(tkinter.Frame):

  RESIZE_RETIO = 2 # 縮小倍率の規定
  def click_screenshot_button():
    # メインディスプレイのスクリーンショット
    img = pyautogui.screenshot()
    # スクリーンショットした画像は表示しきれないので画像リサイズ
    global resized_image
    resized_image = img.resize(size=(int(img.width / app.RESIZE_RETIO),
                                   int(img.height / app.RESIZE_RETIO)),
                                   resample=Image.BILINEAR)
    app.__view_image_screenshot_canvas(resized_image)
    

  # ドラッグ開始した時のイベント
  def get_start_point(event):
    global start_x, start_y

    # すでに"rect1"タグの図形があれば削除
    view_screenshot_canvas.delete("rect1")

    view_screenshot_canvas.create_rectangle(event.x,
                             event.y,
                             event.x + 1,
                             event.y + 1,
                             outline="red",
                             tag="rect1")
    start_x, start_y = event.x, event.y

  # ドラッグ中のイベント
  def rect_drawing(event):
    
    if app.__is_out_of_area_mouse_pointer(event.x):
      end_x = 0
    else:
      end_x = min(resized_image.width, event.x)

    if app.__is_out_of_area_mouse_pointer(event.y):
      end_y = 0
    else:
      end_y = min(resized_image.height, event.y)

    # "rect1"タグの画像を再描画
    view_screenshot_canvas.coords("rect1", start_x, start_y, end_x, end_y)

  # ドラッグを離したときのイベント
  def release_action(event):
    # "rect1"タグの画像の座標を元の縮尺に戻して取得
    start_x, start_y, end_x, end_y = [
      round(n * app.RESIZE_RETIO) for n in view_screenshot_canvas.coords("rect1")
    ]

    # 取得した座標を表示
    # TODO: ここ消す
    pyautogui.alert("start_x : " + str(start_x) + "\n" + "start_y : " +
                    str(start_y) + "\n" + "end_x : " + str(end_x) + "\n" +
                    "end_y : " + str(end_y))
    
  # ドラッグ中のマウスポインタが領域外の場合はtrue
  def __is_out_of_area_mouse_pointer(mouse_pointer):
    return mouse_pointer < 0

  def __view_image_screenshot_canvas(image):
    # グローバル変数にしないと、create_imageが使用できないためグローバル変数にする
    global  img_tk
     # tkinterで表示できるように画像変換
    img_tk = ImageTk.PhotoImage(image)

    # Canvasウィジェットの描画
    global view_screenshot_canvas
    view_screenshot_canvas = tkinter.Canvas(root,
                             bg="green",
                             width=image.width,
                             height=image.height)
    # Canvasウィジェットに取得した画像を描画
    view_screenshot_canvas.create_image(0, 0, image=img_tk, anchor=tkinter.NW)
    view_screenshot_canvas.pack()
    app.__set_event_canvas()
  
  def __set_event_canvas():
    # Canvasウィジェットを配置し、各種イベントを設定
    view_screenshot_canvas.bind("<ButtonPress-1>", app.get_start_point)
    view_screenshot_canvas.bind("<Button1-Motion>", app.rect_drawing)
    view_screenshot_canvas.bind("<ButtonRelease-1>", app.release_action)


if __name__ == "__main__":
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
                          command=app.click_screenshot_button, 
                          bg='#f0e68c', 
                          height=2, 
                          width=20)
  button.pack()

  # テキストボックス
  txt = tkinter.Text()
  txt.pack()

  root.mainloop()