# coding: UTF-8
from PIL import Image, ImageTk

from modules import Ocr
import tkinter
import time
import pyautogui

class App(tkinter.Frame):

  RESIZE_RETIO = 2 # 縮小倍率の規定
  def __init__(self):
    self.root = tkinter.Tk()
    # フォーム
    self.root.title("OCR Screenshot")
    self.root.geometry("900x800")

    self.label = tkinter.Label(self.root, text="")
    self.label.pack()
    # テキストボックス
    self.frame = tkinter.Frame(self.root)
    self.frame.pack(fill = tkinter.BOTH)
    self.screenshot_button = tkinter.Button(self.frame, 
                            text="スクリーンショット", 
                            command=self.click_screenshot_button, 
                            bg='#f0e68c', 
                            height=2, 
                            width=20)
    self.screenshot_button.pack()

    # テキストボックス
    self.view_text_area = tkinter.Text()
    self.view_text_area.pack()

    self.root.mainloop()


  def click_screenshot_button(self):
    # メインディスプレイのスクリーンショット
    img = pyautogui.screenshot()
    # スクリーンショットした画像は表示しきれないので画像リサイズ
    self.resized_image = img.resize(size=(int(img.width / App.RESIZE_RETIO),
                                   int(img.height / App.RESIZE_RETIO)),
                                   resample=Image.BILINEAR)
    self.__view_image_screenshot_canvas(self.resized_image)
    

  # ドラッグ開始した時のイベント
  def get_start_point(self, event):
    global start_x, start_y

    # すでに"rect1"タグの図形があれば削除
    self.view_screenshot_canvas.delete("rect1")

    self.view_screenshot_canvas.create_rectangle(event.x,
                             event.y,
                             event.x + 1,
                             event.y + 1,
                             outline="red",
                             tag="rect1")
    start_x, start_y = event.x, event.y

  # ドラッグ中のイベント
  def rect_drawing(self, event):
    
    if App.__is_out_of_area_mouse_pointer(event.x):
      end_x = 0
    else:
      end_x = min(self.resized_image.width, event.x)

    if App.__is_out_of_area_mouse_pointer(event.y):
      end_y = 0
    else:
      end_y = min(self.resized_image.height, event.y)

    # "rect1"タグの画像を再描画
    self.view_screenshot_canvas.coords("rect1", start_x, start_y, end_x, end_y)

  # ドラッグを離したときのイベント
  def release_action(self, event):
    # "rect1"タグの画像の座標を元の縮尺に戻して取得
    start_x, start_y, end_x, end_y = [
      round(n * App.RESIZE_RETIO) for n in self.view_screenshot_canvas.coords("rect1")
    ]
    width  = end_x - start_x
    height = end_y - start_y
    img = pyautogui.screenshot(region=(start_x, start_y, width, height))
    changed_text = Ocr.image_to_text(img)
    self.view_text_area.delete('1.0', 'end')
    self.view_text_area.insert('1.0', changed_text)

    
  # ドラッグ中のマウスポインタが領域外の場合はtrue
  def __is_out_of_area_mouse_pointer(mouse_pointer):
    return mouse_pointer < 0

  def __view_image_screenshot_canvas(self, image):
    # グローバル変数にしないと、create_imageが使用できないためグローバル変数にする
    global  img_tk
     # tkinterで表示できるように画像変換
    img_tk = ImageTk.PhotoImage(image)

    # Canvasウィジェットの描画
    # すでにウィジェットを配置している場合は削除する
    if hasattr(self, 'view_screenshot_canvas'): self.view_screenshot_canvas.destroy()
    self.view_screenshot_canvas = tkinter.Canvas(self.root,
                                                 bg="green",
                                                 width=image.width,
                                                 height=image.height)
    # Canvasウィジェットに取得した画像を描画
    self.view_screenshot_canvas.create_image(0, 0, image=img_tk, anchor=tkinter.NW)
    self.view_screenshot_canvas.pack()
    self.__set_event_canvas()
  
  def __set_event_canvas(self):
    # Canvasウィジェットを配置し、各種イベントを設定
    self.view_screenshot_canvas.bind("<ButtonPress-1>",   self.get_start_point)
    self.view_screenshot_canvas.bind("<Button1-Motion>",  self.rect_drawing)
    self.view_screenshot_canvas.bind("<ButtonRelease-1>", self.release_action)


if __name__ == "__main__":
  app = App()