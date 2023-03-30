from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
import sys
import cv2
import pyautogui
import numpy as np
import keyboard

def convert_cv_qt(snapshot_array):
    disply_width = 500
    display_height = 500
    
    h, w, ch = snapshot_array.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QtGui.QImage(
    snapshot_array.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    p = convert_to_Qt_format.scaled(
    disply_width, display_height, Qt.KeepAspectRatio)
    print("fish")
    return QPixmap.fromImage(p)


def snapshot_loop():
    while True:
        if keyboard.is_pressed('ctrl+space'):
            snapshot_array = pyautogui.screenshot()
            snapshot_array = cv2.cvtColor(
            np.array(snapshot_array), cv2.COLOR_RGB2BGR)
            convert_cv_qt(snapshot_array)

snapshot_loop()
