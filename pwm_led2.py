# Add your Python code here. E.g.
from microbit import *

hz = 50
pin0.write_analog(0)
pin0.set_analog_period(hz)

while True:
    pin0.write_analog(0)
    sleep(hz * 2)
    pin0.write_analog(256)
    sleep(hz * 2)
    pin0.write_analog(512)
    sleep(hz * 2)
    pin0.write_analog(768)
    sleep(hz * 2)
    pin0.write_analog(1023)
    sleep(hz * 2)
    

