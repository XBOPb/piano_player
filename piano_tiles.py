# Designed for https://yandex.com/games/app/165866 Piano Tiles app
from pyautogui import pixel, locateOnScreen
import os
import re
import time
import keyboard
import re
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def main(coords):
    coord_list = list(coords.values())
    while keyboard.is_pressed('q') == False:
        popup = locateOnScreen('popup.png', region=(1600, 200, 200, 200), grayscale=True, confidence = 0.9)
        if popup != None:
            close_popup = re.findall(r'\d+', str(popup))
            click(int(close_popup[0]) + 1, int(close_popup[1]) + 1)
        for coord in coord_list:
            if pixel(*coord)[2] in range(50, 120) and pixel(*coord)[0] in range(50, 120):
                print(f'{pixel(*coord)=}')
                click(*coord)


if __name__ == "__main__":
    time.sleep(2)  
    coords = {}
    path_to_txt = os.path.join(os.path.dirname(__file__), 'coordinates.txt')
    with open(path_to_txt, 'r') as f:
        lines = f.readlines()                                   # read txt with coords
        for line_number, line in enumerate(lines):
            coords[line_number] = eval(line)                    # read coords

    main(coords)