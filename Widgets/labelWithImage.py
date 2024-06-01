import sys
import os
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget

basedir = os.path.dirname(__file__)
print("Current working folder:", os.getcwd())
print("Paths are relative to:", basedir)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("My App")
        
        widget = QLabel()
        pixmap = QPixmap(os.path.join(basedir, "perrito.jpg"))
        #widget.setScaledContents(True)
        widget.setPixmap(pixmap)
        self.setFixedSize(300,200)
        #self.resize(pixmap.width(),pixmap.height())
        self.setCentralWidget(widget) 

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()