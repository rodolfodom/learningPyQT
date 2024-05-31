import sys
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)
window = QPushButton('Hello, World!')
window.show()
app.exec_()