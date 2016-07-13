import pyfirmata

import sys

Led_Pin = 13
Delay = 0.5

PORT = '/dev/ttyACM0'

board = pyfirmata.Arduino(PORT)

print "Setting up the board interface..."
it = pyfirmata.util.Iterator(board)
it.start()

board.digital[Led_Pin].write(1)
board.pass_time(Delay)
board.digital[Led_Pin].write(0)
board.pass_time(Delay)
