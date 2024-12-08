from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.icon_path="./img/"

        self.browser = QWebEngineView()
        self.setWindowIcon(QIcon(self.icon_path+"flashbrowse.png"))
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        home_icon = QIcon(self.icon_path+"house.png")
        home_btn = QAction(home_icon,'Go to Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        spacer = QWidget()
        spacer.setFixedWidth(25)
        navbar.addWidget(spacer)

        back_icon = QIcon(self.icon_path+"back.png")
        back_btn = QAction(back_icon,'Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        reload_icon = QIcon(self.icon_path+"reload.png")
        reload_btn = QAction(reload_icon,'Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        forward_icon = QIcon(self.icon_path+"forward.png")
        forward_btn = QAction(forward_icon,'Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        

        # self.url_bar = QLineEdit()
        # self.url_bar.returnPressed.connect(self.navigate_to_url)
        # navbar.addWidget(self.url_bar)
     
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))
    
    # def navigate_to_url(self):
    #     url = self.url_bar.text()
    #     self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
QApplication.setApplicationName("Flash Browse")
window = MainWindow()

app.exec_()