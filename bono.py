# Creates a random 10 character string (letters a-z and nr 0-9) and clicks on certain screen coords
# I never finished it as Bono app is very buggy with keyboard support and they dont have a desktop version for it
# Maybe ill come back to it one day

import random
import pyautogui
import keyboard
import time
litera = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',1,2,3,4,5,6,7,8,9,0]

 
time.sleep(2)

while keyboard.is_pressed('q') != True:
    pyautogui.mouseDown(1288,500)
    time.sleep(.5)
    pyautogui.mouseUp(1288,500)
    time.sleep(.5)
    rnd = random.choice(litera)
    keyboard.press_and_release(rnd)
    time.sleep(.4)
    rnd1 = random.choice(litera)
    keyboard.press_and_release(rnd1)
    time.sleep(.4)
    rnd2 = random.choice(litera)
    keyboard.press_and_release(rnd2)
    time.sleep(.4)
    rnd3 = random.choice(litera)
    keyboard.press_and_release(rnd3)
    time.sleep(.4)
    rnd4 = random.choice(litera)
    keyboard.press_and_release(rnd4)
    time.sleep(.4)
    rnd5 = random.choice(litera)
    keyboard.press_and_release(rnd5)
    time.sleep(.4)
    rnd6 = random.choice(litera)
    keyboard.press_and_release(rnd5)
    time.sleep(.4)
    rnd7 = random.choice(litera)
    keyboard.press_and_release(rnd7)
    time.sleep(.4)
    rnd8 = random.choice(litera)
    keyboard.press_and_release(rnd8)
    time.sleep(.4)
    rnd9 = random.choice(litera)
    keyboard.press_and_release(rnd9)
    time.sleep(.4)
    rnd10 = random.choice(litera)
    keyboard.press_and_release(rnd10)
    time.sleep(.4)
    all= [rnd,rnd1,rnd2,rnd3,rnd4,rnd5,rnd6,rnd7,rnd8,rnd9,rnd10]
    #all2 = [rnd6,rnd7,rnd8,rnd9,rnd10]
    #keyboard.press_and_release(all)
    #time.sleep(.9)
    #keyboard.press_and_release(all)
    #time.sleep(.9)
    #keyboard.press_and_release('enter')
    time.sleep(.9)
    pyautogui.mouseDown(1389,850)
    time.sleep(.2)
    pyautogui.mouseUp(1389,850)
    time.sleep(.9)
    pyautogui.mouseDown(1335,780)
    time.sleep(.5)
    pyautogui.mouseUp(1335,780)
    result = ''.join(str(x) for x in all)
    print('Tested the combination: ',result)
    time.sleep(1)