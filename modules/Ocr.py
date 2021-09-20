from PIL import Image
import sys

import pyocr
import pyocr.builders


def get_text(image):
  print(pyocr.get_available_tools())
  tool = pyocr.get_available_tools()[0]
  txt = tool.image_to_string(
      image,
      lang="eng",
      builder=pyocr.builders.TextBuilder(tesseract_layout=6)
  )
  print( txt )