import serial

ser = serial.Serial("COM1", 9600)
def SerialWrite(s):
     ser.write(s.encode())
while True:
    s = str(input())
    SerialWrite(s)

