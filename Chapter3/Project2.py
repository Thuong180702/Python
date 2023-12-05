import serial
arduinoData = serial.Serial('COM3',9600)
while True:
    print("The distance of the object is: ")
    x = arduinoData.readline()
    print(str(x.decode().strip()))