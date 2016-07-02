import serial #import the serial library
arduinoSerialPort = serial.Serial("ttyACM0", 9600)
arduinoSerialPort.write('b')