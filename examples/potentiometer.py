import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BCM)

aPin = 18
bPin = 23

def discharge():
    GPIO.setup(aPin, GPIO.IN)
    GPIO.setup(bPin, GPIO.OUT)
    GPIO.output(bPin, False)
    time.sleep(0.005)

def chargeTime():
    GPIO.setup(bPin, GPIO.IN)
    GPIO.setup(aPin, GPIO.OUT)
    count = 0
    GPIO.output(aPin, True)
    while not GPIO.input(bPin):
        count = count + 1
    return count

def analogRead():
    discharge()
    return chargeTime()

while True:
    print(analogRead())
    time.sleep(1)
    
