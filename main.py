from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread, QSize
import sys
import cv2
import pyautogui
import numpy as np
import keyboard

# Unused as of now, will eventually be the magnified window object
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WEH")

        self.disply_width = 640
        self.display_height = 480

        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)

        self.setLayout(vbox)
        grey = QPixmap(self.disply_width, self.display_height)
        grey.fill(QColor('darkGray'))
        self.image_label.setPixmap(grey)


class EditMode(QWidget):
    def __init__(self, snapshot_array):
        super().__init__()
        self.initUI(snapshot_array)
        self.showMaximized()
        self.setWindowTitle("Screenview")
        flags = Qt.WindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        
    def initUI(self, snapshot_array):
        
        # Need to make this dynamically adjust to user's resolution depending on focused monitor
        self.disply_width = 1920
        self.display_height = 1080
        
        self.image_label = QLabel(self)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.setContentsMargins(0,0,0,0)
        self.setLayout(vbox)
        
        qt_image = self.convert_cv_qt(snapshot_array)
        self.image_label.setPixmap(qt_image)
    
    def convert_cv_qt(self, snapshot_array):
        rgb_image = cv2.cvtColor(snapshot_array, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(
        rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(
        self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)
    



def snapshot_loop():
    while True:
        if keyboard.is_pressed('ctrl+space'):
            snapshot_array = pyautogui.screenshot() # Modify this method to detect which monitor to screenshot
            snapshot_array = cv2.cvtColor(np.array(snapshot_array), cv2.COLOR_RGB2BGR)
            app = QApplication(sys.argv)
            a = EditMode(snapshot_array)
            a.showFullScreen()
            sys.exit(app.exec_())

        if keyboard.is_pressed('ctrl+q'):
            break


if __name__ == "__main__":
    snapshot_loop()

