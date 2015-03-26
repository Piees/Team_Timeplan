import struct
def checkbyte(value, file):
	f = open(file, 'rb')
	for x in range(1, value + 1):
		if x == value:
			bin = struct.unpack('B', f.read(1))[0]
			print bin
		else:
			bin = struct.unpack('B', f.read(1))[0]
