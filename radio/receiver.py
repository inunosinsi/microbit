from microbit import *
import radio

display.show(Image.HEART)

radio.config(group=1)
radio.on()

i = 0
while True:
    if button_a.is_pressed():
        msg = radio.receive()
        print(msg)
        sleep(300)
