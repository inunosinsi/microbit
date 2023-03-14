from microbit import *

mat = [
    [9,9,0,0,0],
    [0,9,0,0,0],
    [0,9,9,0,9],
    [9,9,9,9,9],
    [9,9,9,9,9]
]

blueprint = ""
for vec in mat:
    for v in vec:
        blueprint += str(v)
    blueprint += ":"

submarine = Image(blueprint)

display.show(submarine)
