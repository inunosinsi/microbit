from microbit import *
import radio

display.show(Image.ASLEEP)

radio.config(group=1)
radio.on()

i = 0
while True:
    display.show(Image.YES)
    sleep(500)
    radio.send(str(i))
    i += 1
    display.show(Image.ASLEEP)
    sleep(500)
