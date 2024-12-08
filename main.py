from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        home_icon = QIcon("./img/house.png")
        home_btn = QAction(home_icon,'Go to Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        back_icon = QIcon("./img/back.png")
        back_btn = QAction(back_icon,'Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        reload_icon = QIcon("./img/reload.png")
        reload_btn = QAction(reload_icon,'reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        forward_icon = QIcon("./img/forward.png")
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
QApplication.setApplicationName("Hi")
window = MainWindow()

app.exec_()