# OCR Screenshot
範囲選択部分を文字認識してテキストボックスに表示するツール

## 環境
Windows10    
Anaconda3    
Python3.7(3.8以上だとtesseractがinstallできない可能性がある)

## 使い方
OCR Screenshotを起動します    
スクリーンショットボタン(中央黄色いボタン)をクリックするとスクリーンショットが下部に表示されます。    
(このスクリーンショットはメインディスプレイのみ表示されます)
![clickedScreenshotButton](./readme/images/clickedScreenshotButton.PNG)

次に表示されたスクリーンショットから、文字列認識させたい部分をマウスドラッグで範囲指定します。    
(OCR Screenshot内赤枠が選択範囲)    
選択後、選択範囲の文字列をOCR Screenshot内テキストボックスに表示されます。
(サクラエディタのマークなども認識してしまうので、少し余計な文字列も出力されています。。。)
![clickedScreenshotButton](./readme/images/selectArea.png)
範囲選択ですが、範囲選択した部分を文字認識しているわけではなく、  
現在のメインディスプレイから範囲指定された場所を文字認識しています。  
(最初に表示したスクリーンショットはあくまでディスプレイ内の範囲選択のために使用しています。)

## 事前準備
- 必要なライブラリなどをインストールする(anacondaにて実行)

```cmd:anacondaTerminal
pip install pyautogui
pip install Pillow
conda install -c conda-forge tesseract
conda install -c conda-forge pyocr
```

- 起動(anacondaにて実行)

```cmd:anacondaTerminal
cd #プロジェクトフォルダ
python main.py
```

## 注意点
英語しか対応していません