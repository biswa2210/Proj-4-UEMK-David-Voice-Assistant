import pyautogui
from time import sleep
x = 0
while True:
    sleep(1)
    pok = pyautogui.position()
    print(pok)
    