from datetime import datetime
from time import sleep
import ctypes
import os

current_wallpaper = ' '
img = [0, 300, 600, 730, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2400 ]
#      0  111  222  333  444  5555  6666  7777  8888  9999  1010  1111  1212  1313  1414  1515      

while __name__ == '__main__':
    time = (datetime.now().hour*100) + datetime.now().minute
    for i in range(0, 16):
        if time in range(img[i], img[i+1]):
            img_path = os.path.dirname(os.path.realpath(__file__)) + "\Wallpapers\\" + str(i) + ".jpeg"
            if not current_wallpaper == img_path:
                ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path , 0)
    sleep(5)