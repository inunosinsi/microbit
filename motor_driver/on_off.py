# Imports go at the top
from microbit import *

while True:
    if button_a.is_pressed():
        pin12.write_digital(1)
    elif button_b.is_pressed():
        pin12.write_digital(0)
