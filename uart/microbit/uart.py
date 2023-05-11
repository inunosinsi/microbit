from microbit import *

uart.init(baudrate=9600, bits=8, parity=uart.ODD, stop=1, tx=pin0, rx=pin1)

while True:
    if button_a.is_pressed():
        display.show(Image.YES)
        uart.write(b'0')
        sleep(1000)
    elif button_b.is_pressed():
        display.show(Image.YES)
        uart.write(b'1')
        sleep(1000)
    else:
        display.show(Image.ASLEEP)
