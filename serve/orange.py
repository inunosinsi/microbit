from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        pin0.write_analog(76)
        sleep(1000)
    elif button_a.is_pressed():
        pin0.write_analog(26)
    elif button_b.is_pressed():
        pin0.write_analog(123)
