from PIL import Image
import sys

import pyocr
import pyocr.builders

# image内の画像の文字列を読み取り返す
def image_to_text(image):
  if len(pyocr.get_available_tools()) == 0: print("OCRが正しく設定されていません")
  tool = pyocr.get_available_tools()[0]
  txt = tool.image_to_string(
      image,
      lang="eng",
      builder=pyocr.builders.TextBuilder(tesseract_layout=6)
  )
  return txt