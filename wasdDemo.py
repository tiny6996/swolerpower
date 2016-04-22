import RPi.GPIO as GPIO
import os
import time

#Defines the raspberry pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# setting global constants as the pin
wormpin1 = 8
wormpin2 = 7
actpin1 = 11
actpin2 = 9

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
def turnright():
    GPIO.output(wormpin1, False)
    GPIO.output(wormpin2, True)
    print("The Panels are turning right")
    time.sleep(5)
    os.system('clear')


# function that turns the panels left
def turnleft():
    GPIO.output(wormpin1, True)
    GPIO.output(wormpin2, False)
    print("The Panel is turning left")
    time.sleep(5)
    os.system('clear')


# function that turns the panels towards 90 degrees with the flywheel
def turnup():
    GPIO.output(actpin1, True)
    GPIO.output(actpin2, False)
    print("The panel is turning up")
    time.sleep(5)
    os.system('clear')


#functions that turns the panels closer to 0 degrees with the flywheel
def turndown():
    GPIO.output(actpin1, False)
    GPIO.output(actpin2, True)
    print("the panel is doing down")
    time.sleep(5)
    os.system('clear')


# main loop of the program

# stops the motors before starting the program
stop()


while True:
    var = raw_input("pleae input up, down, left, or right: ")

    if var == "up":
        turnup()

    elif var == "down":
        turndown()

    elif var == "left":
        turnleft()

    elif var == "right":
        turnright()

    elif var == "exit":
        stop()
        exit()
    else:
        stop()

    stop()

