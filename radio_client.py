from microbit import *
import radio

display.show(Image.HAPPY)

radio.on()

while True:
    details = radio.receive_full()
    if details:
        msg, rssi, timestamp = details
        display.scroll(rssi)
