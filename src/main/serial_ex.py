import serial
ser = serial.Serial('COM10', 9600, timeout=1)

while 1:
    s = ser.readline()
    sDecode = s.decode('utf-8')
    sArray = sDecode.split()
    print(sArray)

