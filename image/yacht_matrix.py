from microbit import *

mat = [
    [0,0,9,0,0],
    [0,0,9,9,9],
    [0,0,9,0,0],
    [9,9,9,9,9],
    [0,9,9,9,0]
]

coord = ""
for vec in mat:
    for v in vec:
        coord += str(v)
    coord += ":"

yacht = Image(coord)
display.show(yacht)
