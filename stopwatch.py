import time
import RPi.GPIO as GPIO

# Declare the second variable and initiialize it
second = 0

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
        second += 1
        # Set timer so that when it reaches to the given second, the light bulb will turn off
        # All time will be converted into second
        if (second == 60):
            second = 0 # After second reaches the given timer, second will be reset
            GPIO.output(relay_pin, GPIO.LOW)
            break
    
        
