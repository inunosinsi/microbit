from microbit import *

# uartの標準設定を用いる 
uart.init()

while True:
    x, y, z = accelerometer.get_values()
    uart.write("x:"+str(x))
    uart.write("\r\n")
    uart.write("y:"+str(y))
    uart.write("\r\n")
    uart.write("z:"+str(z))
    uart.write("\r\n")
    sleep(1000)
