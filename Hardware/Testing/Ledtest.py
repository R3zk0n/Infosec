import settings
from time import sleep
from BreakfastSerial import Led, Arduino, Button

board = Arduino()
LED_PIN = 9
LED_GREEN = 12
BUTTON_PIN = 2
led = Led(board, LED_PIN)
led_green = Led(board, LED_GREEN)
button = Button(board, BUTTON_PIN)

def hold_cb():
	print "Holding..."
	led.on()
	sleep(2)
	led.off()


def down_cb():
	led_green.on()

def up_cb():
	print "Up \n"


button.down(down_cb)
button.up(up_cb)
button.hold(hold_cb)


import code
code.InteractiveConsole(locals=globals()).interact()