import imp
try:
	imp.find_module('adafruit_adxl34x')
	stub = False
	import board
	import busio
	import adafruit_adxl34x
	i2c = busio.I2C(board.SCL, board.SDA)
	accel = adafruit_adxl34x.ADXL345(i2c)
except ImportError:
	# If the hardware is not present, we fall back to stub mode.
	print("Hardware not present")


try:
	while True:
		x = accel.acceleration[0]
		y = accel.acceleration[1]
		z = accel.acceleration[2]

		print("x " + str(x) + " y " + str(y) + " z " + str(z))

except KeyboardInterrupt:
	print('interrupted!')