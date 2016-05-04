# importing nessacary libraries

import string
import RPi.GPIO as GPIO
import datetime as dt
import time

# global constants for pin numbers and turn times
wormTime = float(5.73)
actTime = float(5.73)
wormpin1 = int(23)
wormpin2 = int(24)
actPin1 = int(9)
actPin2 = int(11)



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


    #This is going to be a really long & messy if else statement to get the date to that updates the sunrise and sunset times every 10 days
    # this is based on the US central timezone and accounts for DST on march 13 and november
    # I should shove this in a function later
    if dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 1, 10):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 7, 34)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 16, 41)
        tomorrowRise = dt.datetime(dt.datetime.now().year,dt.datetime.now().month, dt.datetime.now().day, 7, 34)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 1, 20):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 7, 27)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 17, 02)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 7, 29)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 1, 31):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 7, 23)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 17, 02)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 7, 22)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 2, 10):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 7, 9)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 17, 23)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 7, 5)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 2, 20):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 6, 55)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 17, 36)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 6, 55)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 2, 29):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 6, 45)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 17, 47)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 7, 5)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 3, 10):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 7, 13)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 19, 15)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 7, 10)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 3, 20):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 7, 00)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 19, 19)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 7, 00)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 3, 31):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 6, 52)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 19, 25)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 6, 50)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 4, 10):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 6, 40)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 19, 32)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 6, 35)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 4, 20):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 6, 20)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 19, 45)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 6, 15)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 4, 30):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 6, 05)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 19, 57)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 6, 0)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 5, 10):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 5, 55)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 20, 05)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 5, 55)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 5, 20):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 5, 35)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 20, 28)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 5, 30)

    elif dt.datetime.now() <= dt.datetime(dt.datetime.now().year, 5, 31):
        riseTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 5, 30)
        setTime = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day, 20, 35)
        tomorrowRise = dt.datetime(dt.datetime.now().year, dt.datetime.now().month, dt.datetime.now().day + 1, 5, 25)


    # Using the dates found above calculate the day length and the delay time for the motors
    dayLength = int((setTime - dt.datetime.now()).total_seconds())
    delay = int(dayLength/7700)

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
    while riseTime <= dt.datetime.now() and turnNumber < 77:
        print("the panels are in position {} of 77 \n".format(turnNumber + 1))

        toSunset(turnNumber)
        time.sleep(delay)
        turnNumber += 1



    # Move panels back to the Sun Rise Position
    print("The day is over so the panels are going to move to the sunrise position \n ")
    toSunRise()

    # find the time between sunrises and go to sleep
    sleepTime = (tomorrowRise - setTime).total_seconds()
    print("The panels are now going to sleep for {} seconds \n".format(sleepTime))
    toLogFile("The is over so now the panels are going to go to sleep for {} Seconds \n".format(sleepTime))
    time.sleep(sleepTime)






