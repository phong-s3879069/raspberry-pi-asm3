import speech_recognition as sr
import RPi.GPIO as GPIO
import stopwatch
import newmailing

# PIN connected to IN1
relay_pin = 23

# Set mode BCM
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

# Type of PIN - ouput
GPIO.setup(relay_pin, GPIO.OUT)

# Set USB microphone as default input
r = sr.Recognizer()
mic = sr.Microphone(sample_rate = 48000, device_index = 2, chunk_size = 1024)

# List of commands that the user can say to turn on or off the light
onCommand = ["turn on", "on", "turn on the light", "turn on the lights", "on the light", "turn on light", "hello"]
offCommand = ["turn off", "off", "turn off the light", "turn off the lights", "off the light", "turn off light", "bye"]
defCommand = ["yes", "no"]

# Initialize count to calculate the number of times that the user cannot say commands in the list 
count = 0

def listen(r, mic):
    global count
    while True:
        try: 
            with mic as source:
                    print("Pi: Please say something!")
                    r.adjust_for_ambient_noise(source)
                    r.dynamic_energy_threshold = 3000
                    audio = r.listen(source, timeout = 5.0)
                    response = r.recognize_google(audio)
                    print("You: " + response)

                    # Check if the user would like to turn on the light
                    if (response in onCommand):
                        GPIO.output(relay_pin, GPIO.LOW)
                        print("Pi: The light is on")
                        print("Pi: Would you like to set timer for the light?")

                    # Check if the user has set the timer for the light    
                    if (response == "yes"):
                        stopwatch.stop()
                    else:
                        pass

                    # Check if the user would like to turn off the light
                    if (response in offCommand):
                        GPIO.output(relay_pin, GPIO.HIGH)
                        print("Pi: The light is off")
                    
                    # Check if the user says wrong commands
                    if (response not in onCommand and response not in offCommand and response not in defCommand and response != ""):
                        count += 1
                        print(count)
                        if (count == 3):
                            newmailing.send_email()
                            count = 0

                    return response
    
        except sr.WaitTimeoutError:
            pass
   
        except sr.UnknownValueError:
            pass
                    
        except sr.RequestError:
            print("network error")

    GPIO.cleanup()

while True:
    listen(r, mic)



