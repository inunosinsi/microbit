from microbit import *

mat = [
    [9,9,0,0,0],
    [0,9,0,0,0],
    [0,9,9,0,9],
    [9,9,9,9,9],
    [9,9,9,9,9]
]

coord = ""
for vec in mat:
    for v in vec:
        coord += str(v)
    coord += ":"

submarine = Image(coord)
display.show(submarine)
