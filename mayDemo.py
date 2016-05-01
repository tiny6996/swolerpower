# importing nessacary libraries

import string
import ephem
import datetime as dt
import time



# setting the location of the observer and a sun shortcut

panels = ephem.Observer()
nextPanels = ephem.Observer()
sun = ephem.Sun()
panels.lat = '42.5'
panels.long = '90'
nextPanels.lat = '42.6'
nextPanels.long = '90'





# function that sets all pins to false to the panels stop moving
def stopWorm():
    print " I am stopping this shit from the worm gear "


def stopAct():
    print "I am stopping this shit from the actuators "


def toSunset(n):
    GPIO.output(wormpin1, False)
    GPIO.output(wormpin1, True)
    if n <= 38:
        print "this is the AM turn function"
    else:
        print "this is the PM turn function"


def toSunRise():
    print "the panels are returning to their full and upright position"
def turnDown():
    print "the panels are doing down like a bunch of bitches "


def turnUP():
    print "the panels are doing up"


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
    delta = dt.timedelta(days=1)
    today = dt.datetime.today()
    tomorrow = today + delta
    nextPanels.date = tomorrow
    panels.date = dt.datetime.today()

    # Find the time for today's sunrise and sunset as well as tomorrow sunrise
    setTime = panels.next_setting(ephem.Sun())
    riseTime = panels.previous_rising(ephem.Sun())
    tomorrowRise = panels.next_rising(ephem.Sun())

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







