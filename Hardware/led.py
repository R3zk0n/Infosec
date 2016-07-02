import settings
from BreakfastSerial import Led, Arduino, Button
board = Arduino()
led_pin = 12 
led_pins2 = 13
led2 = Led(board, led_pin)

led = Led(board, led_pins2)
led.on()
print "Led %s" % led_pin
led2.on()
print "Led 2 is ON"
