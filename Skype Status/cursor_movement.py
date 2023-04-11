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
    
    # If the generated random number is greater than the screen size, it will throw up an error and interrupt the infinite loop.
    
    if x1 > x:
        x1 = x
    if y1 > y:
        y1 = y
        
    screen.moveTo(x1, y1)
   
    # Repeat the same every 30 seconds
    time.sleep(30)
    
 # I choose 700,300 because the location was blank. 
 # Additionally, clicking is required to keep SKPYE's status online, a new loop to do the same
 # I choose 700,300 because the location was blank. 
 # Additionally, clicking is required to keep SKPYE's status online, a new loop to do the same
    while True:
        screen.click(700, 300, button='left')
        time.sleep(6)




