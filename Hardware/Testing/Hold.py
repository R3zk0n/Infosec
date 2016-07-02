import settings
import alsaaudio
from time import sleep
from BreakfastSerial import Led, Arduino, Button

board = Arduino()
LED_PIN = 9
LED_3 = 8
LED_2 = 11
BUTTON_PIN = 2
m = alsaaudio.Mixer()
led = Led(board, LED_PIN)
LED_2 = Led(board, LED_2)
LED_3 = Led(board, LED_3)
button = Button(board, BUTTON_PIN)
def hold_cb():
	print "Full Volume"
	led.on()
	m.setvolume(100)
	LED_2.off()
	LED_3.off()
def down_cb():
	LED_2.on()
	LED_3.on()
	print "Setting!"
	m.setvolume(20)
	led.off()
def up_cb():
  print "button up"

button.down(down_cb)
button.up(up_cb)
button.hold(hold_cb)
# Run an interactive shell so you can play (not required)
import code
code.InteractiveConsole(locals=globals()).interact()