from microbit import *

# PWMを50Hz
pin0.set_analog_period(50)

# デューティ比 7.5%が90度に相当
duty = 7.5
pin0.write_analog(duty)
sleep(1000)

while True:
	# デューティ比が12%(225度に相当)を超えたら繰り返しを抜ける
	if duty > 12:
		break
	duty += 0.1	# デューティ比を徐々に上げる
	pin0.write_analog(duty)
	sleep(500)

duty = 7.5
pin0.write_analog(duty)