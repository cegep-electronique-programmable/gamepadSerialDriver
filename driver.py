import pyautogui
import serial

ser=serial.Serial(port='COM26',baudrate=115200)

while True:
    s=ser.read(1) #lir eune caractère
    print(s.decode())

    if s.decode() == '0':
        pyautogui.press('s')
    elif s.decode() == '1':
        pyautogui.press('w')
    elif s.decode() == '2':
        pyautogui.press('a')
    elif s.decode() == '3':
        pyautogui.press('d')
    elif s.decode() == '4':
        pyautogui.press('space')
    elif s.decode() == '5':
        pyautogui.press('enter')

ser.close()