import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = ['My First App', 'Second App', 'Third App', 'Fourth App', 'Fifth App', 'Something went wrong']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Oneshot Button App')
        
        self.button = QPushButton('Press Me')
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)
        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        print('Clicked')
        new_window_title = choice(window_titles)
        print('setting title: %s' % new_window_title)
        self.setWindowTitle(new_window_title)
    
    def the_window_title_changed(self, window_title):
        print('Window title changed to: %s' % window_title)
        
        if(window_title == 'Something went wrong'):
            self.button.setEnabled(False)
            self.button.setText('Something went wrong')     
    
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()