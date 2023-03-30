import serial

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser.close()
ser.open()

while True:
    line = ser.readline().strip().decode('UTF-8')

    if len(line) > 0:
        print(line)
