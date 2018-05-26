# Create a data log comming through the serial
#
# Author: Juan Gallostra
# Date: 25-06-2018

import serial

# Serial parameters
PORT = '/dev/ttyACM0'
BAUDRATE = 115200


# serial communication object
serial_com = serial.Serial(PORT, BAUDRATE)

with open('data_set.txt', 'w') as f:
	while True:
		f.write(serial_com.readline())


