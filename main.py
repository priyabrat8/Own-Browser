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

        self.add_space(25,navbar)

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

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        navbar.addWidget(spacer)

        menu_btn = QPushButton("...") 
        menu_btn.setFixedSize(50, 30)
        menu_btn.clicked.connect(self.show_options_menu)
        navbar.addWidget(menu_btn)

        self.add_space(25,navbar)
       
     
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))
    
    def navigate_to(self, url):
        self.browser.setUrl(QUrl(url))
    
    def add_space(self,size,navbar):
        spacer = QWidget()
        spacer.setFixedWidth(size)
        navbar.addWidget(spacer)

    def show_options_menu(self):
        menu = QMenu(self)
        menu.addAction(QIcon(self.icon_path+"explainshell.png"),"Kali Command", lambda: self.navigate_to("https://explainshell.com/"))
        menu.addAction(QIcon(self.icon_path+"metaspliot.png"),"Metasploit", lambda: self.navigate_to("https://www.metasploit.com/"))
        menu.addAction(QIcon(self.icon_path+"hacktricks.png"),"Hacktricks", lambda: self.navigate_to("https://book.hacktricks.xyz/"))

        menu.exec_(QCursor.pos())

app = QApplication(sys.argv)
QApplication.setApplicationName("Flash Browse")
window = MainWindow()

app.exec_()