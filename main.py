# importing nessacary libraries

import string
import RPi.GPIO as GPIO
import ephem
import datetime as dt
import time

# global constants for ease of use

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
def stopWorm():
    GPIO.output(wormpin1, False)
    GPIO.output(wormpin2, False)


def stopAct():
    GPIO.output(actPin1, False)
    GPIO.output(actPin2, False)


def toSunset(n):
    GPIO.output(wormpin1, False)
    GPIO.output(wormpin1, True)
    if n <= 38:
        GPIO.output(actPin1, False)
        GPIO.output(actPin1, True)
        time.sleep(wormTime)
        turnUP()
    else:
        GPIO.output(actPin1, True)
        GPIO.output(actPin1, False)
        time.sleep(wormTime)
        turnDown()


def toSunRise():
    GPIO.output(wormpin1, True)
    GPIO.output(wormpin2, False)
    time.sleep(77 * wormTime)
    stopWorm()


def turnDown():
    GPIO.output(actPin1, True)
    GPIO.output(actPin2, False)
    time.sleep(actTime - wormTime)


def turnUP():
    GPIO.output(actPin1, False)
    GPIO.output(actPin2, True)
    time.sleep(actTime - wormTime)


# This function writes text to the log file on a new line
def toLogFile(message):
    with open('solarlog.txt', 'a') as logfile:
        logfile.write(message)
        logfile.write("\n")

# runs once at the start of the program before enteringthe main loop
print ("welcome to the best solar tracker ever!")

# Writes three new lines to the log file between each startup
with open('solarlog.txt', 'a') as logfile:
    logfile.write("\n \n ")

toLogFile("The Program was started at {} \n".format((str(dt.datetime.now()))))


# main loop of the program
while True :
    print("you are now in the main loop")

    # Sets the time for the panels  and calculates the sunset
    panels.date = dt.datetime.now()
    # localtime = dt.datetime.now()
    delta = dt.timedelta(days=1)
    today = dt.datetime.today()
    tomorrow = today + delta

    # Find the time for today's sunrise and sunset as well as tomorrow sunrise
    setTime = panels.previous_setting(sun)
    riseTime = panels.next_rising(sun)
    tomorrowRise = panels.next_rising(sun)

    # Using the dates found above calculate the day length and the delay time for the motors
    dayLength = int((setTime.datetime() - dt.datetime.now()).total_seconds())
    delay = dayLength/77

    # Prints the the info about the day to the console and sends it the log file
    print("today is {}".format(dt.datetime.now()))
    print("today the sun will rise at {} ".format(riseTime))
    print("today the sun will set at {} ".format(setTime))
    print("tomorrow the sun will rise at {} ".format(tomorrowRise))
    print("the panels are going to move every {} seconds ".format(delay))
    toLogFile("today is{} ".format(dt.datetime.now()))
    toLogFile("today the sun will set at {} ".format(riseTime))
    toLogFile("today the sun will set at {} ".format(setTime))
    toLogFile("tomorrow the sun will rise at {} ".format(tomorrowRise))
    toLogFile("the panels are going to move every {} seconds ".format(delay))

    # While the sun is up turn the panels towards the sunset
    turnNumber = 0
    while riseTime.datetime() <= dt.datetime.now():
        print("the panels are in position {} of 77 \n".format(turnNumber + 1))

        toSunset(turnNumber)
        turnNumber += turnNumber

    # Move panels back to the Sun Rise Position
    toSunRise()
    # find the time between sunrises and go to sleep
    sleepTime = int((tomorrowRise - setTime).total_seconds())
    print("The day is over so the panels are going to move to the sunrise position \n ")
    print("The panels are now going to sleep for {} seconds \n".format(sleepTime))
    toLogFile("The is over so now the panels are going to go to sleep for {} Seconds \n".format(sleepTime))







