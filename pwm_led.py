from microbit import *

def convert(per):
    return int(1023 * per / 100)

hz = 20 # 周波数 Hz
set_analog_period(hz)

duty = 1
add = 1
while True:
    pin0.write_analog(convert(duty))
    duty += add
    if duty <= 0 or duty >= 100:
        add *= -1
    
    sleep(hz)

