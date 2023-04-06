from microbit import *

value = 0
add = 1

while True:
    value += add
    if value <= 0 or 1023 <= value:
        add *= -1
    
    pin0.write_analog(value)
    sleep(1)
