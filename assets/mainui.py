from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainUI(QWidget) :
    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint| Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.SplashScreen)  
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground,True)

        windowPalette:QPalette = QPalette()
        windowPalette.setBrush(QPalette.Active,QPalette.WindowText,QColor(255,255,255,255))
        windowPalette.setBrush(QPalette.Inactive,QPalette.WindowText,QColor(255,255,255,255))
        self.setPalette(windowPalette)

        font1:QFont = QFont()
        font1.setBold(True)
        font1.setFamily("Arial")
        font1.setPixelSize(100)

        font2:QFont = QFont()
        font2.setFamily("Arial")
        font2.setPixelSize(40)

        font3:QFont = QFont()
        font3.setFamily("Arial")
        font3.setPixelSize(25)

        self.background:QLabel = QLabel(self)
        self.background.setPixmap(QPixmap("assets/background.png"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0,0,1024,1024)

        self.timeLabel:QLabel = QLabel(self)
        self.timeLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.timeLabel.setGeometry(10,10,530,250)
        self.timeLabel.setFont(font1)

        self.dateLabel:QLabel = QLabel(self)
        self.dateLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.dateLabel.setGeometry(10,130,1024,1024)
        self.dateLabel.setFont(font2)

        self.gushiLabel:QLabel = QLabel(self)
        self.gushiLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.gushiLabel.setGeometry(10,190,1024,1024)
        self.gushiLabel.setFont(font3)

        self.updateTimer:QTimer = QTimer(self)
        