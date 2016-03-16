import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.IN)
input = GPIO.input(7)
while True:
	if(GPIO.input(7)== False):
		print("every time you push the button you are slowly killing me")
		os.system('clear')
