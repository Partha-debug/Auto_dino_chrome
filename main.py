import pyautogui
from PIL import Image, ImageGrab
import time

def isColideWithCactus(data):
    for i in range(250, 420):
        for j in range(410, 470):
            if data[i, j] > 100:
                return True
    return False

def isColideWithBird(data):
    for i in range(250, 420):
        for j in range(350, 400):
            if data[i, j] > 100:
                return True
    return False

time.sleep(1)

while True:
    image = ImageGrab.grab().convert('L')
    data = image.load()
    if isColideWithCactus(data):
        pyautogui.press('up')
    if isColideWithBird(data):
        pyautogui.keyDown('down')
    else:
        pyautogui.keyUp('down')
        