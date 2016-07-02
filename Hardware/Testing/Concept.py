import settings
from BreakfastSerial import Led, Arduino, Button, Servo, Sensor
import time
from time import sleep

print '''PUT ASCII ART HERE BECAUSE ASCII!!!
         '''
User = raw_input("Please select a function to test: \n")

if User == 1:
    Led()
if User == 2:
    loop()
if User == 3:
    servo()


board = Arduino()
sensor = Sensor(board, "A0")

def loop():
    value = sensor.value or 1
    value = value / 2

    print value

    sensor.on()



def servo():
servo.set_position(180)
sleep(2)
servo.move(-135)
sleep(2)
servo.center()
sleep(2)
servo.reset()

#timeout = time.time() + 60
def Led():
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
        print "
        led2.on()
        sleep(5)
        break


import code
code.InteractiveConsole(locals=globals()).interact()
