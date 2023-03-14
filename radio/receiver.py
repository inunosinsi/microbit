from microbit import *
import radio

display.show(Image.TARGET)

radio.config(group=1)
radio.on()

while True:
    if button_a.is_pressed():
        msg = radio.receive()
        print(msg)
        sleep(300)
