"""
This is to automate cursor movement to keep skypee online

"""

import random
import time
import pyautogui as screen

while True:
    x, y = screen.size()
    x1 = random.randint(0, x)
    y1 = random.randint(0, y)
    if x1 > x:
        x1 = x
    if y1 > y:
        y1 = y
    screen.moveTo(x1, y1)
    # Select a location to move cursor, i choose 700,300 cuz the location was blacnk with no options selections,
    # also, click is required to keep skpyee status online
    screen.click(700, 300, button='left')
    time.sleep(60)





