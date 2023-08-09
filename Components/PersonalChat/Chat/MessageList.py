from PyQt6.QtWidgets import QWidget, QPlainTextEdit
from PyQt6.QtCore import QObject, Qt
from PyQt6.QtGui import QColorConstants, QResizeEvent

from ...Boxes.ScrollStack import ScrollStack
from .MessageBox import MessageBox

class MessageList(ScrollStack):
    def __init__(self, parent: QObject = None):
        ScrollStack.__init__(self, parent)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.Gray)
        self.setPalette(pal)

        self.box.layout().setContentsMargins(0, 5, 0, 5)
        self.box.setFixedHeight(10)

        for i in range(20):
            self.addWidget(MessageBox("dkg ldkgdof gkmrmdo jdfk jvdbfgk jdbk jf", False, self) )

        self.addWidget(MessageBox("dfg ojfgv djkg skdjfg kdfj vkdsjxfcnb kvjdfngkv jdfxn bkvjdfng k", True, self))
        self.addWidget(MessageBox("dfg ojfgv djkg skdjfg kdfj vkdsjxfcnb kvjdfngkv jdfxn bkvjdfng k", True, self))

        print(self.max)
        self.go(self.max)





    def resizeEvent(self, event: QResizeEvent) -> None:
        self.box.resize(event.size().width(), self.box.height())
        self.max = self.height() - self.box.height()
        self.min = max(0, self.height() - self.box.height())

        y = self.box.y()

        if not self.max <= y <= self.min:
            if abs(y - self.max) < abs(y - self.min):
                self.go(self.max)
            else:
                self.go(self.min)

    def addWidget(self, w: QWidget):
        if self.max == self.box.y():
            ScrollStack.addWidget(self, w)
            self.go(self.max)
        else:
            ScrollStack.addWidget(self, w)

        self.max = self.height() - self.box.height()
        self.min = max(0, self.height() - self.box.height())
