from typing import Optional

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QObject, pyqtSignal, QEvent, QPointF
from PyQt6.QtGui import QPalette, QFontMetrics, QColor, QColorConstants, QResizeEvent, QPainter, QFont, QMouseEvent, \
    QCursor


class TextLine(QLabel):
    def __init__(self, *args):
        if len(args) > 0 and type(args[0]) is str:
            self.text: str = args[0]
        else:
            self.text: str = ""
        QLabel.__init__(self, *args)

        self.calc()
        self.correct()

    def calc(self):
        metric = QFontMetrics(self.font())
        self.pref: list[int] = [0] * len(self.text)

        for i in range(len(self.text)):
            cw = metric.tightBoundingRect(self.text[i]).width()
            if i == 0:
                self.pref[i] = cw
            else:
                self.pref[i] = cw + self.pref[i - 1]

    def correct(self):
        # metric = QFontMetrics(self.font())
        # w = self.width()
        # l = 0
        # r = len(self.text)
        #
        # while r - l > 1:
        #     sr = (l + r) // 2
        #     if self.pref[sr] <= w:
        #         l = sr
        #     else:
        #         r = sr
        #
        # print(self.pref[-1], w, metric.horizontalAdvance(self.text))
        #
        # if l < len(self.text) - 1:
        #     while l > 0 and self.pref[l] + metric.tightBoundingRect("...").width() > w:
        #         l -= 1
        #
        #     QLabel.setText(self, self.text[:l + 1] + "...")
        # else:
            QLabel.setText(self, self.text)

    def setText(self, a0: str) -> None:
        self.text = a0
        self.calc()
        self.correct()

    def setFont(self, a0: QFont) -> None:
        QLabel.setFont(self, a0)
        self.calc()
        self.correct()

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.correct()