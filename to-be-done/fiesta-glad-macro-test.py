from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con


# time.sleep(5)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def press(key):
    pyautogui.keyDown(key)
    time.sleep(0.1)
    pyautogui.keyUp(key)

def vitality():
    if keyboard.is_pressed('y')==True:
            press('num1')
            press('num2')
            press('num3')
            press('num4')
            press('num7')
            press('num8')
            press('num9')
        
def slash():
    if keyboard.is_pressed('u')==True:
            press('num5')
            press('num6')
            press('2')
            press('num7')
            press('num8')

def immobilize():
     if keyboard.is_pressed('j')==True:
            press('left')
            press('down')
            press('right')
            press('3')
            press('num7')
            press('num8')
            press('num9')

# pyautogui.displayMousePosition()
# if pyautogui.pixel(818,1011)[0]==232 :

print('Script Starting ...')
while keyboard.is_pressed('f12')==False:
    vitality()
    slash()
    immobilize()

print('Script ends ...')