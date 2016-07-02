from Arduino import Arduino

import time




def Blink(led_pin, baud, port="ttyACM0"):
    """
    Blinks an LED in 1 sec intervals
    """
    board = Arduino(baud, port=port)
    board.pinMode(led_pin, "OUTPUT")
    while True:
        board.digitalWrite(led_pin, "LOW")
        print board.digitalRead(led_pin)  # confirm LOW (0)
        time.sleep(1)
        board.digitalWrite(led_pin, "HIGH")
        print board.digitalRead(led_pin)  # confirm HIGH (1)
        time.sleep(1)
