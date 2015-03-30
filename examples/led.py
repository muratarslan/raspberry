import RPi.GPIO as GPIO
import time

def blink(pin):
	GPIO.output(pin, GPIO.HIGH)
	print "yandi"
	time.sleep(1)
	GPIO.output(pin, GPIO.LOW)
	print "sondu"
	time.sleep(1)
	return

GPIO.setmode(GPIO.BOARD) # to use board pins
GPIO.setup(11, GPIO.OUT) # set 11 output

for i in range(0,50):
	blink(11)
GPIO.cleanup()
