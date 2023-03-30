import serial
import pygame
from pygame.locals import *
import sys

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser.close()
ser.open()

pygame.init()
screen = pygame.display.set_mode((400, 300))
px=200
py=150
m = 10
while True:
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(10,10,10),(px,py),10)
    pygame.display.update()

    # serial
    line = ser.readline().strip().decode('UTF-8')
    if len(line) > 0:
        # x:100から x(ini)と数字(v)に分ける
        ini = line[0]
        v = int(line[2:])
        
        if ini == "x":
            if v > 0:
                px += m
            else:
                px -= m
        elif ini == "y":
            if v > 0:
                py += m
            else:
                py -= m
        #else:
            # 何もしない
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
