from microbit import *

uart.init(baudrate=9600, bits=8, parity=uart.ODD, stop=1, tx=pin0, rx=pin1)

while True:
    if uart.any():
        display.show(Image.YES)
        b = uart.read()
        if b != None:
            display.scroll(b)
        sleep(1000)
    else:
        display.show(Image.ASLEEP)
