from PyQt6.QtWidgets import QWidget, QStackedLayout
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent, QMouseEvent
from PyQt6.QtCore import QObject, Qt, pyqtSignal

from ...Back_End import ApplicationController
from .AccountInfoBox import *

class SideBar(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)

        self.accountInfoBox = AccountInfoBox(self)
        self.accountInfoBox.setFixedHeight(150)

        self.accountScroll = VerticalScrollArea(self)
        self.accountList = AccountList()

        for acc in ApplicationController.Application.Accounts():
            if ApplicationController.Application.currentAccount() == acc:
                continue
            self.accountList.addAccount(acc)

        add = addNewAccountButton()

        add.setFixedHeight(UiController.DefaultLineHeight)

        add.clicked.connect(UiController.Chat.focusEnterence)

        self.accountList.addWidget(add)

        self.accountScroll.setWidget(self.accountList)

        self.accountInfoBox.accountListOpenButton.clicked.connect(self.manageAccountList)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        lay.addWidget(self.accountInfoBox)
        lay.addWidget(self.accountScroll)

        lay.setAlignment(self.accountInfoBox, Qt.AlignmentFlag.AlignTop)
        lay.setAlignment(self.accountScroll, Qt.AlignmentFlag.AlignTop)
        lay.addStretch()

        self.setLayout(lay)
        self.manageAccountList(False)


    def manageAccountList(self, check: bool):
        if check:
            if self.accountScroll.widget is not None:
                self.accountScroll.setMinimumSize(self.width(), min(self.accountScroll.widget.height(), 200))
            else:
                self.accountScroll.setFixedSize(0, 0)
        else:
            self.accountScroll.setFixedSize(0, 0)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        event.accept()

    def open(self):
        self.setEnabled(True)
        self.show()

    def remove(self):
        self.setEnabled(False)
        self.hide()
        self.manageAccountList(False)