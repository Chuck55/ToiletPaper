 import serial
ser = serial.Serial(
	port = '/dev/ttyACM0', 
	baudrate = 1200,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 0
    )  
print(ser.name)        
while True:
    c = ser.readline()
    c = int(c)
    if c > 0:
	else if
        

