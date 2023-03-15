from microbit import *

mat = [
    [9,9,0,0,0],
    [0,9,0,0,0],
    [0,9,9,0,9],
    [9,9,9,9,9],
    [9,9,9,9,9]
]

for i in range(0, 6):
    coord = ""
    for vec in mat:
        for v in vec:
            coord += str(v)
        coord += ":"

    submarine = Image(coord)
    display.show(submarine)
    sleep(1000)

    # リスト内の行を下にシフト
    for j in range(4, 0, -1):
        mat[j] = mat[j-1]
    mat[0] = [0,0,0,0,0]
