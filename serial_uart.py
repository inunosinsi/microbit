from microbit import *

while True:
    lv = microphone.sound_level()
    msg = "vol:"+str(lv)
    uart.write(msg.encode())
    uart.write("\r\n".encode())
    sleep(1000)
