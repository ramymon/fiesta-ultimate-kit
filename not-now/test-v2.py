
import keyboard 
from pyautogui import *
import pyautogui
import time 
import subprocess
import ctypes

shell32 = ctypes.windll.shell32
params = None
directory = None
show_command = 1  # SW_SHOWNORMAL

def press_button_via_ahk(x):
    executable = r"C:\Users\MONCEF\Desktop\fiesta-ultimate-kit\click-" + x
    result = shell32.ShellExecuteW(None, "runas", executable, params, directory, show_command)

def press(key):
    pyautogui.keyDown(key)
    time.sleep(0.1)
    pyautogui.keyUp(key)

while keyboard.is_pressed('f12')==False:

    if keyboard.is_pressed('n'):
        press_button_via_ahk("q")
        time.sleep(0.5)

    
time.sleep(0.5)
    


    
   


