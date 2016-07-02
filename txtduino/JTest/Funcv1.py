# Starting..
#UPDATED... (Slightly.)
import pyfirmata
import sys
#Defining Port Details

An_PINS = (0, 1, 2, 3)
Led_Pin = 10
Led_PinGreen = 13
Delay = 1

PORT = '/dev/ttyACM0'
print "Would you like to use default pins(10, 13) Or Manually set?\n"
Man = input(" 1. Manually. 2. Default\n")



#Functions!!  (SON!)
def Func_Led():
    print '''Welcome to the LED Functions \n
            What function would you like to use?\n
           1. Blink\n
           2. Color Blink\n'''

    LedChoice = input()

    print "Led On: %s" % Led_Pin
    if LedChoice == 1:
        while True:
            board.digital[Led_Pin].write(1)
            board.pass_time(Delay)
            board.digital[Led_Pin].write(0)
            board.pass_time(Delay)
    if LedChoice == 2:
        while True:
            board.digital[Led_Pin].write(1)
            print "Led on: %s" % Led_Pin
            board.pass_time(Delay)
            board.digital[Led_Pin].write(0)
            board.pass_time(Delay)
            print "Led Off: %s" % Led_Pin
            print "Led on: %s" % Led_PinGreen
            board.digital[Led_PinGreen].write(1)
            board.pass_time(Delay)
            board.digital[Led_PinGreen].write(0)
            board.pass_time(Delay)
            print "Led Off: %s " % Led_PinGreen

def Func_Light():
    print "Welcome to the Light Function \n"
    for pin in An_PINS:
        board.analog[pin].enable_reporting()
    for i in range(1, 100):
        print "\n Values after %i Seconds(s)" % i
        for pin in An_PINS:
            print "Pin %i :: %s " % (pin, board.analog[pin].read())
    board.pass_time(1)
#Testing........
# Manully Selection..

if Man == 1:
    try:
        Led_Pin=input("Enter a Number to use:\n")
        Led_PinGreen=input("Second Pin: \n")
    except SyntaxError:
        print "Using defaults..(10/13) as nothing was entered."
        Led_Pin = 10
        Led_PinGreen = 13
if Man == 2 or 1:
    user = input('''
    Please enter a function to access.. \n
    1. Light function.
    ===================\n
    2. Led Function
    ===================\n
    3. Servo Function
    ===================\n
    4. Exit
    ===================\n''')
if Man > 3:
    print '''
    Please select
    =======================\n
    1. Selection Pin Input.\n
    2 Default Pins (10/13) \n
    =======================\n'''

# Exiting..
if user == 4:
    sys.exit(0)

# Creates the Board
print "Setup...\n"
board = pyfirmata.Arduino(PORT)
print "Setting up the connection to: %s \n" % board
it = pyfirmata.util.Iterator(board)
it.start()


# Menu Selection functions..


#User selection..
if user == 1:
    Func_Light()
if user == 2:
    Func_Led()
if user == 3:
    Serv_Fuct()
