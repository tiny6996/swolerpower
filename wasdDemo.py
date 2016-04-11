import RPi.GPIO as GPIO
import os
import time

#Defines the raspberry pi
GPIO.setmode(GPIO.BCM)


# setting global constants as the pin
wormpin1 = 23
wormpin2 = 24
actpin1 = 9
actpin2 = 11

# sets all the needed pins as ouputs
GPIO.setup(wormpin1, GPIO.OUT)
GPIO.setup(wormpin2, GPIO.OUT)
GPIO.setup(actpin1, GPIO.OUT)
GPIO.setup(actpin2, GPIO.OUT)


# function that sets all pins to false to the panels stop moving
def stop():
    GPIO.output(wormpin1, False)
    GPIO.output(wormpin2, False)
    GPIO.output(actpin1, False)
    GPIO.output(actpin2, False)
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
    GPIO.output(actpin1, True)
    GPIO.output(actpin2, False)
    print("The panel is turning up")
    os.system('clear')


#functions that turns the panels closer to 0 degrees with the flywheel
def turndown ():
    GPIO.output(actpin1, False)
    GPIO.output(actpin2, True)
    print("the panel is doing down")
    os.system('clear')






# main loop of the program
while True:
    var = input ("pleae input a key")
    if var == "w":
        turnup()
        time.sleep(2)

    elif var == "s":
        turndown()
        time.sleep(2)

    elif var == "a":
        turnleft()
        time.sleep(2)
    elif  == "d":
        turnright()
        time.sleep(2)
    else:
        stop()

    stop()

