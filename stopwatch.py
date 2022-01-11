import time
import RPi.GPIO as GPIO

second = 0
minute = 0

# PIN connected to IN1
relay_pin = 23

# Set mode BCM
GPIO.setmode(GPIO.BCM) 

# Type of PIN - ouput
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setwarnings(False)

def stop():
    global second
    global minute
    while True:
        print('\t\t\t\t %d : %d '%(minute,second))
        time.sleep(1)
        second+=1
        if (second == 10):
            second = 0
            minute+=1
            GPIO.output(relay_pin, GPIO.HIGH)
            break
    
        
