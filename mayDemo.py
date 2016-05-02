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
    delay = int(dayLength/77)

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
    while riseTime <= dt.datetime.now():
        print("the panels are in position {} of 77 \n".format(turnNumber + 1))

        toSunset(turnNumber)
        turnNumber += turnNumber
        time.sleep(delay)
        turnNumber += 1
    # Move panels back to the Sun Rise Position
    toSunRise()
    # find the time between sunrises and go to sleep
    sleepTime = int((tomorrowRise - setTime)).total_seconds()
    print("The day is over so the panels are going to move to the sunrise position \n ")
    print("The panels are now going to sleep for {} seconds \n".format(sleepTime))
    toLogFile("The is over so now the panels are going to go to sleep for {} Seconds \n".format(sleepTime))







