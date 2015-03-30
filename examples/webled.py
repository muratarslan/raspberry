import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,True)

# sudo /etc/init.d/webiopi start
# sudo /etc/init.d/webiopi status
# www.raspi.gen.tr/2014/02/21/webiopi-ile-web-arayuzunden-gpio-kontrolu