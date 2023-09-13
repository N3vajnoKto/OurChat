from PyQt6.QtWidgets import QWidget, QPlainTextEdit
from PyQt6.QtCore import QObject, Qt
from PyQt6.QtGui import QColorConstants, QResizeEvent

from ...Boxes.ScrollStack import ScrollStack
from .MessageBox import MessageBox
from .MessageBox import MessageInfo

class MessageList(ScrollStack):
    def __init__(self, parent: QObject | None = None):
        ScrollStack.__init__(self, parent)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.Gray)
        self.setPalette(pal)

        self.lastMessage: MessageBox = None

        self.box.layout().setContentsMargins(0, 7, 0, 7)
        self.box.setFixedHeight(14)

        for i in range(10):
            info = MessageInfo("dljlsdn skjc kasdfb kasldf gvldrkg knkdrlr gnelsk gnrbrg k")
            self.addWidget(info)

        self.scrollTo(self.max)

    def maxWidth(self):
        return min(450, int(0.7 * self.width()))

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.box.resize(event.size().width(), self.box.height())
        self.max = self.height() - self.box.height()
        self.min = max(0, self.height() - self.box.height())

        totalH: int = 14

        for w in self.widgetList:
            w.message.setMaximumWidth(self.maxWidth())
            w.message.format()
            w.messageFrame.updateSize()
            w.arrange()
            totalH += w.height()

        if (totalH != self.box.height()):
            self.box.setFixedHeight(totalH)
            self.max = self.height() - self.box.height()
            self.min = max(0, self.height() - self.box.height())


        y = self.box.y()

        if not self.max <= y <= self.min:
            if abs(y - self.max) < abs(y - self.min):
                self.scrollTo(self.max)
            else:
                self.scrollTo(self.max)

    def addWidget(self, info: MessageInfo):
        w = MessageBox(info, self)
        w.message.setMaximumWidth(self.maxWidth())
        w.message.format()
        w.arrange()
        if self.lastMessage is not None:
            prevInfo = self.lastMessage.message.info
            if info.suits(prevInfo):
                w.connectMessage(self.lastMessage)

        self.lastMessage = w

        ScrollStack.addWidget(self, w)
        self.max = self.height() - self.box.height()
        self.min = max(0, self.height() - self.box.height())

        if abs(self.max - self.box.y()) < 100:
            self.scrollTo(self.max)


