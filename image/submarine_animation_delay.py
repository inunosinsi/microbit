from microbit import *

mat = [
    [9,9,0,0,0],
    [0,9,0,0,0],
    [0,9,9,0,9],
    [9,9,9,9,9],
    [9,9,9,9,9]
]

submarines = []
for i in range(0, 6):
    if i > 0:
        for j in range(4, 0, -1):
            mat[j] = mat[j-1]
        mat[0] = [0,0,0,0,0]
    
    blueprint = ""
    for vec in mat:
        for v in vec:
            blueprint += str(v)
        blueprint += ":"

    submarines.append(Image(blueprint))

display.show(submarines, delay=1000)
