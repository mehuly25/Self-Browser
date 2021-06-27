from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com')) #can be anything else
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #Setting up the navigation bar
        navbar=QToolBar()
        self.addToolBar(navbar)
        back_btn=QAction('<-',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        forward_btn=QAction('->',self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        reload_btn=QAction('Reload',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def update_url(self, q):
        self.url_bar.setText(q.toString())


    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com')) #Can be anything

    def navigate_to_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
QApplication.setApplicationName('Mehuly Edge')
window=MainWindow()
app.exec_()


