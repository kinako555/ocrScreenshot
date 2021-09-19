import sys
from PySide2.QtWidgets import (QWidget, QApplication)
from PySide2.QtGui import (QPixmap, QPainter, QPainterPath, QColor, QBrush)
from PySide2.QtCore import (Qt, QRect)


class ScreenShot(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        # 現在の画面をキャプチャー
        screen = QApplication.primaryScreen()
        self.originalPixmap = screen.grabWindow(QApplication.desktop().winId())

        self.endpos = None
        self.stpos = None

    def paintEvent(self, event):

        p = QPainter()
        p.begin(self)
        p.setPen(Qt.NoPen)

        rectSize = QApplication.desktop().screenGeometry()
        p.drawPixmap(rectSize, self.originalPixmap)

        if self.endpos and self.stpos:

            pp = QPainterPath()
            pp.addRect(rectSize)
            pp.addRoundRect(QRect(self.stpos, self.endpos), 0, 0)
            p.setBrush(QBrush(QColor(0, 0, 100, 100)))
            p.drawPath(pp)

        p.end()

    def mouseMoveEvent(self, event):

        self.endpos = event.pos()
        # マウスが動いたときに、再度描画処理を実行する
        self.repaint()

    def mousePressEvent(self, event):

        self.stpos = event.pos()

    def mouseReleaseEvent(self, event):

        self.endpos = event.pos()
        self.screenShot()

    def screenShot(self):

        # 切り取り処理をして保存後、ツールを終了する
        pmap = self.originalPixmap.copy(QRect(self.stpos, self.endpos))
        pmap.save("E:/test.jpg")
        self.close()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    wid = ScreenShot()
    wid.showFullScreen()
    sys.exit(app.exec_())