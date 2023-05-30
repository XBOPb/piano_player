# Designed for https://yandex.com/games/app/165866 Piano Tiles app
from pyautogui import *
import os
import time
import keyboard
import random
import re
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def main(coords, rgb):
    coord_list = list(coords.values())
    print(f'{coord_list=}')
    while keyboard.is_pressed('q') == False:
        for coord in coord_list:
            if pixel(*coord)[2] in range(50, 71):
                click(*coord)


if __name__ == "__main__":
    time.sleep(2)
    rgb = []
    coords = {}
    path_to_txt = os.path.join(os.path.dirname(__file__), 'coordinates.txt')
    with open(path_to_txt) as f:
        lines = f.readlines()                                   # read txt with coords
        for line_number, line in enumerate(lines):
            if 'color' in line:
                rgb = re.findall(r'\(.*?\)', line)              # take tuple from brackets
                rgb = ''.join(rgb)
                rgb = eval(rgb)                                 # make pythonic
            else:
                coords[line_number] = eval(line)                 # read coords

    main(coords, rgb)