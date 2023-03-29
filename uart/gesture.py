from microbit import *

# uartの標準設定を用いる 
uart.init()

while True:
    x, y, z = accelerometer.get_values()
    print("x:"+str(x))
    print("y:"+str(y))
    print("z:"+str(z))
    sleep(1000)
