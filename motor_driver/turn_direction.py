# Imports go at the top
from microbit import *

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.is_pressed():
        pin12.write_digital(1)
        pin8.write_digital(0)
    elif button_b.is_pressed():
        pin12.write_digital(0)
        pin8.write_digital(1)
