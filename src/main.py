import os,sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from datetime import datetime
import requests

from mainui import *
from tray import *

weeks:list[str] = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]

def getFormatTime(_format: str="%H%M%S") -> str:
    h,m,s = str(datetime.now().hour),str(datetime.now().minute),str(datetime.now().second)
    if (len(h) < 2) : h = "0"+h
    if (len(m) < 2) : m = "0"+m
    if (len(s) < 2) : s = "0"+s
    _format = _format.replace("%H",h)
    _format = _format.replace("%M",m)
    _format = _format.replace("%S",s)
    return _format

def getFormatDate(_format: str="%Y%M%D%W") -> str:
    _format = _format.replace("%Y",str(datetime.now().year))
    _format = _format.replace("%M",str(datetime.now().month))
    _format = _format.replace("%D",str(datetime.now().day))
    _format = _format.replace("%W",weeks[datetime.now().weekday()])
    return _format

def getGushi():
    req = requests.get("https://v1.jinrishici.com/all.txt")
    req.encoding = "utf-8"
    return req.text

class Main(MainUI) :
    def __init__(self) -> None:
        super().__init__()
        desktop:QDesktopWidget = QApplication.desktop()
        self.setGeometry(desktop.width()-600,desktop.height()-300,530,250)
        self.trays = Tray(self)

        self.updateTimer.timeout.connect(self.updateTime)
        self.updateTimer.start(500)

        self.gushiLabel.setText(getGushi())

        self.mx:int = None
        self.my:int = None

        self.show()

    def updateTime(self) :
        self.timeLabel.setText(getFormatTime("%H:%M:%S"))
        self.dateLabel.setText(getFormatDate("%Y年 %M月 %D日 %W"))
        self.trays.setToolTip(getFormatTime("%H:%M:%S ")+getFormatDate("%Y年 %M月 %D日 %W"))
    
    def fpos(self) :
        desktop:QDesktopWidget = QApplication.desktop()
        self.setGeometry(desktop.width()-600,desktop.height()-300,530,250)

    def noh(self) :
        self.setHidden(not self.isHidden())
    
    def mousePressEvent(self, event: QMouseEvent) -> None:
        if (event.button() == Qt.LeftButton):
            self.mx = event.pos().x()
            self.my = event.pos().y() 
    
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if (self.mx != None) :
            self.setGeometry(self.x()+event.pos().x()-self.mx,self.y()+event.pos().y()-self.my,self.width(),self.height())
    
    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self.gushiLabel.setText(getGushi())
    
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if (event.button() == Qt.LeftButton):
            self.mx = None
            self.my = None

if (__name__ == "__main__") :
    app:QApplication = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())