from microbit import *

while True:
    lv = microphone.sound_level()
    msg = "vol:"+str(lv)
    print(msg)
    sleep(1000)
