import os,sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Tray(QSystemTrayIcon):
    def __init__(self,parent:QWidget) :
        super().__init__(QIcon("assets/logo.ico"))
        self.memu = QMenu()
        action = QAction("换一首古诗", self, triggered=parent.mouseDoubleClickEvent)
        self.memu.addAction(action)
        action = QAction("归位",self,triggered=parent.fpos)
        self.memu.addAction(action)
        action = QAction("隐藏/显示", self, triggered=parent.noh)
        self.memu.addAction(action)
        action = QAction("退出", self, triggered=sys.exit)
        self.memu.addAction(action)
        self.setContextMenu(self.memu)
        self.show()