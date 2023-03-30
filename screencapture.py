import cv2 as cv
import pyautogui
import sys
import numpy as np

from mss import mss

from PIL import Image

from time import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


test_dim = {'top': 100, 'left': 200, 'width': 1600, 'height': 1024}
sct = mss()

while 1:
    sct_img = sct.grab(test_dim)
    img = Image.frombytes(
        'RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    cv.imshow('test', np.array(img))
    if cv.waitKey(25) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break
