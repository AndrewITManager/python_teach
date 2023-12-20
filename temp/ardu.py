import pyfirmata
import time


board = pyfirmata.Arduino('COM4')

while True:
    text = input('On or OFF')
    if text == 'on':
        board.digital[13].write(1)
    
    elif text == 'off':
        board.digital[13].write(0)
    
