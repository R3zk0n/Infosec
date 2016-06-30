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

# Start reporting for defined pins
for pin in An_PINS:
    board.analog[pin].enable_reporting()

# Loop for reading the input. Duration approx. 10 s
for i in range(1, 100):
    print "\nValues after %i second(s)" % i
    board.digital[Led_Pin].write(1)
    board.pass_time(pin)
    board.digital[Led_Pin].write(0)
    board.pass_time(pin)
    board.digital[Led_Pin].write(1)
    board.pass_time(pin)
    for pin in An_PINS:
        print "Pin %i : %s" % (pin, board.analog[pin].read())
    board.pass_time(1)
