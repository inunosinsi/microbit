from microbit import *

mat = [
    [0,0,9,0,0],
    [0,0,9,9,9],
    [0,0,9,0,0],
    [9,9,9,9,9],
    [0,9,9,9,0]
]

icons = []
for i in range(0, len(mat)+1):
    coord = ""
    for vec in mat:
    	for v in vec:
            coord += str(v)
        coord += ":"

    yacht = Image(coord)
    icons.append(yacht)

    for row in range(0, len(mat)):
        for col in range(0, len(mat[0])-1):
            mat[row][col] = mat[row][col+1]
        mat[row][len(mat[0])-1] = 0

display.show(icons, delay=1000)
