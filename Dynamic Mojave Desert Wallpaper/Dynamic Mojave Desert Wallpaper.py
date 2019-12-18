from time import sleep
import ctypes, os

img = [0, 300, 600, 730, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2400 ]
#      0  111  222  333  444  5555  6666  7777  8888  9999  1010  1111  1212  1313  1414  1515  

for i in range(0, 16):
    img_path = os.path.dirname(os.path.realpath(__file__)) + "\Wallpapers\\" + str(i) + ".jpeg"
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path , 0)
    print(img_path)
    sleep(1)