import serial
import time

serial1 = serial.Serial("COM11", 9600)

while True:
    serial1.write(b"1")
    time.sleep(2)
    serial1.write(b"0")
