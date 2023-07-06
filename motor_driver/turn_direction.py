# Imports go at the top
from microbit import *

while True:
    if button_a.is_pressed():
        pin12.write_analog(512)
        pin8.write_digital(0)
    elif button_b.is_pressed():
        pin8.write_analog(512)
        pin12.write_digital(0)
