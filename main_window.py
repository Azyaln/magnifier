import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

# GUI Class
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # MainWindow Properties
        self.initUI()
        self.setWindowTitle("GUI Dimensions!")
        self.showMaximized()
        flags = QtCore.Qt.WindowFlags(
            QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        
    def initUI(self):
        self.label = QLabel(self)
        self.label.setText("Text")
        self.label.move(50,50)
        
        self.b1 = QPushButton(self)
        self.b1.setText("Button")
        self.b1.clicked.connect(self.pressed)
        
    def pressed(self):
        self.b1.setText("Pressed!")
        
# MainWindow Initialization
def MainWindowInit():
    app = QApplication(sys.argv)
    win = MainWindow()
    
    win.show()
    sys.exit(app.exec_())

# Run Code
if __name__ == '__main__':
    MainWindowInit()