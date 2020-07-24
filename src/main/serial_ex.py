import serial
serialProtocol = serial.Serial('COM10', 9600, timeout=1)

while 1:
    serialRead = serialProtocol.readline()
    serialDecode = serialRead.decode('utf-8')
    serialArray = serialDecode.split()
    print(serialArray)

