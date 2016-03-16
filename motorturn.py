import os
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.output(23,False)
GPIO.output(24,False)        
input = GPIO.input(7)
while True:
	if(GPIO.input(7)== False):
		print("you are turning me on at the push of a button ;)")
		os.system('clear')
		GPIO.output(23,True)
		GPIO.output(24,False)
        else:
                GPIO.output(23,False)
		GPIO.output(24,False)
