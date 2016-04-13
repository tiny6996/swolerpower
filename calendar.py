# importing nessacary libraries

import string
import RPi.GPIO as GPIO
import ephem
from datetime import datetime,date
import io
import os
# global constansts for ease of use

wormTime = float(5.73)
actTime = float(5.73)
wormpin1 = int(23)
wormpin2 = int(24)
actPin1 = int(9)
actPin2 = int(11)

# setting the location of the observer and a sun shortcut

panels = ephem.Observer()
sun = ephem.Sun()
panels.lat = '42.5'
panels.long = '90'

# Setup for the raspberry pi
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(wormpin1, GPIO.OUT)
GPIO.setup(wormpin2, GPIO.OUT)
GPIO.setup(actPin1, GPIO.OUT)
GPIO.setup(actPin2, GPIO.OUT)

# Turning all the motors of by setting them to false
GPIO.setup(wormpin1, False)
GPIO.setup(wormpin2, False)
GPIO.setup(actPin1, False)
GPIO.setup(actPin2, False)

# function that sets all pins to false to the panels stop moving
def stop():
    GPIO.output(wormpin1, False)
    GPIO.output(wormpin2, False)
    GPIO.output(actPin1, False)
    GPIO.output(actPin2, False)
    print("the panels are not moving")
    os.system('clear')


# function that turns the panel right
def turnright ():
    GPIO.output(wormpin1, False)
    GPIO.output(wormpin2, True)
    print("The Panels are turning right")
    os.system('clear')


# function that turns the panels left
def turnleft ():
    GPIO.output(wormpin1, True)
    GPIO.output(wormpin2, False)
    print("The Panel is turning left")
    os.system('clear')


# function that turns the panels towards 90 degrees with the flywheel
def turnup ():
    GPIO.output(actPin1, True)
    GPIO.output(actPin2, False)
    print("The panel is turning up")
    os.system('clear')


#functions that turns the panels closer to 0 degrees with the flywheel
def turndown ():
    GPIO.output(actPin1, False)
    GPIO.output(actPin2, True)
    print("the panel is doing down")
    os.system('clear')







