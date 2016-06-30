import settings
from BreakfastSerial import Led, Arduino, Button, Servo
import time
from time import sleep


board = Arduino()
LED_PIN = 10
LED_PIN2 = 13
timeout = time.time() + 60

# Setting up...
led2 = Led(board, LED_PIN2)
led = Led(board, LED_PIN)
print "Turning on!"
led.on()

while True:
    Te = 0
    if Te == 1 or time.time() > timeout:
        print "DEAD"
        led.off()
        print "NEXT LEVEL!!"
        led2.on()
        sleep(5)
        break
