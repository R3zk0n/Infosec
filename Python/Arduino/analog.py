import pyfirmata

PORT = '/dev/ttyACM0'

# Definition of the analog pin
An_PINS = (0, 1, 2, 3)
Led_Pin = 13
# Creates a new board
board = pyfirmata.Arduino(PORT)
print "Setting up the connection to the board ..."
it = pyfirmata.util.Iterator(board)
it.start()

user = raw_input('''Please enter a function to go to
                    1. Light Function \n
                    2. Led Function \n
                    3. Servo Function \n''')

if user == 1:
    print "Light Function \n"
    LightFunc()

def LightFunc():
    for pin in An_PINS:
        board.analog[pin].enable_reporting()
     for i in range(1, 100):
        print "\nValues after %i second(s)" % i
        for pin in An_PINS:
            print "Pin %i : %s" % (pin, board.analog[pin].read())
    board.pass_time(1)
