# README
範囲選択部分を文字認識してテキストボックスに表示する機能ーーーー

## 環境
Windows10 
Anaconda3 
Python3.7(3.8以上だとtesseractがinstallできない可能性がある)

## 事前準備
必要なライブラリなどをインストールする

```cmd:anacondaTerminal
pip install pyautogui
pip install Pillow
conda install -c conda-forge tesseract
conda install -c conda-forge pyocr
```

## 注意点
英語しか対応していません