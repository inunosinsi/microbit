from microbit import *
import radio

display.show(Image.TARGET)

radio.config(group=1)
radio.on()

while True:
    msg = ""
    while True:
        tmp = radio.receive()
        if tmp == None:
            break
        msg = tmp
    print(msg)
    sleep(3000)
