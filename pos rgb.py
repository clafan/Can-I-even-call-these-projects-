# Prints mouse postion+rgb value

import pyautogui,time,keyboard
while keyboard.is_pressed('q') != True:
    time.sleep(.5)
    ix,iy = pyautogui.position()
    rgb = pyautogui.screenshot().getpixel((ix,iy))
    print(f'X={ix}, Y={iy}',rgb)