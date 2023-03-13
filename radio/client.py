##############################################################################
# queueを1にした時にradio.receice_full()でmsg、rssiとtimestampの値を取得できるか？ #
# 下記のコードからmsg、rssiとtimestampを合わせて一つのqueueとするということがわかった。#
##############################################################################

from microbit import *
import radio

radio.config(queue=1, group=1)
radio.on()

while True:
    details = radio.receive_full()
    if details:
        msg, rssi, timestamp = details
        print("message:"+str(msg))
        print("rssi:"+str(rssi))
        print("timestamp:"+str(timestamp))