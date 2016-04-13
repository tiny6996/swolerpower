import string
import RPi.GPIO as GPIO
import ephem
from datetime import datetime,date,timedelta
import time
import io
wormTime = float(5.73)
actTime = float(5.73)
#pin numbers for each gear
wormpin1 = 23
wormpin2 = 24
leftact1 = 8
leftact2 = 7
rightact1 = 9
rightact2 = 11

#making the panels the observer and the sun the object
panels= ephem.Observer()
sun = ephem._sun()
panels.lat='42.5'
panels.long='90'



#setting up the GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(wormpin1,GPIO.OUT)
GPIO.setup(wormpin2,GPIO.OUT)
GPIO.setup(leftact1,GPIO.OUT)
GPIO.setup(leftact2,GPIO.OUT)
GPIO.setup(rightact1,GPIO.OUT)
GPIO.setup(rightact2,GPIO.OUT)
GPIO.output(leftact1,False)
GPIO.output(leftact2,False)
GPIO.output(rightact1,False)
GPIO.output(rightact2,False)
GPIO.output(wormpin1,False)
GPIO.output(wormpin2,False)
#url = "test.ics"

data = str(datetime.now())
with open('solarlog.txt','a') as logfile:
        logfile.write("\n the program was stated at:")
	logfile.write(data)
	logfile.write("\n")


#imports calendar file and creates an array for it to placed in
print "welcome to the best solar tracker ever made lol XD"




#loop that actually moves the panels
while True:
        print "you are now in the main loop"







        #parses the next event in the calendar and creates a unix time stamp






                #setup for the localtime, risetime and settime that is performed eachday
                panels.date = datetime.now()
                localtime = datetime.now()
                sun.compute()
                riseTime = ephem.localtime(panels.previous_rising(sun))
                setTime = ephem.localtime(panels.next_setting(sun))

                print "today the sun will rise at {}".format(riseTime)
                print "today the sun will set at {}".format(setTime)
                print "tomorrow the sun will set at {}".format(tomorrowRise)




                dayLength = int((setTime - datetime.now()).total_seconds())
                delay = dayLength/77
                today = date.today()
                print "today is {} seconds long and the flywheel will spin every {} seconds".format(dayLength, delay)
                print "riseTime: {}".format(riseTime)
                print "setTime: {}".format(setTime)
                print "current time {}:".format(datetime.now())
                print "is the sun up:{}".format(datetime.now() >= riseTime and datetime.now() <=setTime)

                #adds the turn time, date, and day length to the log file
                with open('solarlog.txt','a') as logfile:
                    logfile.write("today is: ")
                    logfile.write(str(e[index].name))
                    logfile.write("\n")
                    logfile.write("the day the length is:")
                    logfile.write(str(dayLength))
                    logfile.write("\n")
                    logfile.write("the turn Length for today is:")
                    logfile.write(str(delay))
                    logfile.write("\n")
                    logfile.write("current sunsise: ")
                    logfile.write(str(riseTime))
                    logfile.write("\n")
                    logfile.write("current sunset: ")
                    logfile.write(str(setTime))
                    logfile.write("\n")
                    logfile.write("next sunrise: ")
                    logfile.write(str(tomorrowRise))
                    logfile.write("\n")


                TurnNumber = 0
                    while riseTime <= datetime.now() and datetime.now() <= setTime:
                            print "you are in position {} of 77".format(turnNumber + 1)
                            if turnNumber <= 38:
                                    print "it is the first half of the day"
                                    GPIO.output(wormpin1,False)
                                    GPIO.output(wormpin2,True)
                                    GPIO.output(leftact1,True)
                                    GPIO.output(leftact2,False)
                                    GPIO.output(rightact1,True)
                                    GPIO.output(rightact2,False)
                            else:
                                    "it is the second half of the day"
                                    GPIO.output(wormpin1,True)
                                    GPIO.output(wormpin2,False)
                                    GPIO.output(leftact1,True)
                                    GPIO.output(leftact2,False)
                                    GPIO.output(rightact1,True)
                                    GPIO.output(rightact2,False)

                            print "now waiting {} seconds".format(wormTime)
                            time.sleep(wormTime)

                            GPIO.output(wormpin1,False)
                            GPIO.output(wormpin2,False)
                            GPIO.output(leftact1,False)
                            GPIO.output(leftact2,False)
                            GPIO.output(rightact1,False)
                            GPIO.output(rightact2,False)

                            print "now waiting {} seconds".format(delay)
                            turnNumber = turnNumber + 1
                            time.sleep(delay)



                            #move to sunrise fix
                        print "the sun has just set and the solar array is returning to the sunrise position"
                        for index in range(77):
                                GPIO.output(wormpin1,True)
                                GPIO.output(wormpin2,False)
                                GPIO.output(leftact1,True)
                                GPIO.output(leftact2,False)
                                GPIO.output(rightact1,True)
                                GPIO.output(rightact2,False)
                                time.sleep(wormTime)
                                print "the array is in postition {} of 77".format(index + 1)

                        #find the time between sunrises and go to sleep
                        sleepTime = int((tomorrowRise - setTime).total_seconds())
                        print "the array has been moved to the sunrise position and will go to sleep {} seconds".format(sleepTime)
                        print "the next sunrise will occur at {}".format(tomorrowRise)
                        with open('solarlog.txt','a') as logfile:
                                logfile.write("the array has been set back to the sunrise position \n")
                                logfile.write("the program will wait ")
                                logfile.write(str(sleepTime))
                                logfile.write(" seconds until the next sunrise \n")
                        time.sleep(sleepTime)


exit()
