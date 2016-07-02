import pyfirmata

pin = 10
delay = 2
pin2 = 13

port = '/dev/ttyACM0'

board = pyfirmata.Arduino(port)


while True:
    board.digital[pin].write(1)
    board.pass_time(delay)
    board.digital[pin].write(0)
    board.pass_time(delay)
    board.digital[pin2].write(1)
    board.pass_time(delay)
    
