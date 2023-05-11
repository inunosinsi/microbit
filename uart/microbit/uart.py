from microbit import *

uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=pin0, rx=pin1)

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        msg = b'uart'
        uart.write(msg)
        sleep(1000)
    else:
        display.show(Image.SAD)
    
