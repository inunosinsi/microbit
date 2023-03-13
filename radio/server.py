from microbit import *
import radio

radio.config(group=1)
radio.on

while True:
	radio.send("a")
	sleep(1000)
