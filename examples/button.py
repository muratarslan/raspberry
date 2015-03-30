import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)

while True:
    inputState = GPIO.input(18)
    if inputState == False:
        print("Button Pressed")
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.2)
    else:
        GPIO.output(17, GPIO.LOW)

    
