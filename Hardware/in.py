import time
timeout = time.time() + 30
Led_Time = 0
while True:

    Led_Time+=1
    print Led_Time
    if Led_Time == 30:
        print "Ending!"
        break
