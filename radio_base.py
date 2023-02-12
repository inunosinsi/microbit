from microbit import *
import radio

display.show(Image.HAPPY)

radio.on()

while True:
    if button_a.is_pressed():
        radio.send('here')
        sleep(1000)
