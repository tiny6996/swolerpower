from ics import Calendar, Event
import string
import RPi.GPIO as GPIO
from datetime import datetime,date,timedelta
import time
import io
wormTime = float(5.73)
actTime = float(5.73)
#pin numbers for each gear
wormpin1 = 23
wormpin2 = 23
leftact1 = 8 
leftact2 = 7
rightact1 = 9
rightact2 = 11


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
print "the calendar file is being read give it a sec it is a 9000 line file"
calendar = "solarcalendar24.ics"
c = Calendar(open(calendar).read().decode('iso-8859-1'))
size = len(c.events)
e = []

#populates array with the calendar info
for index in range(size):
        print "please wait while the array is being populated"
	e.append(c.events[index])
	if index == size -1:
                print "the array has been populated"

#loop that actually moves the panels	
for index in range(size):
        print "you are now in the main loop"
        #today = datetime.now()
    	test = str(e[index].name)
	begin = str(e[index].begin)
	
	#prevent array from going from going out of bounce by using the sunset from the previous day
	if index == size and test == Sunrise:
                print "warning: you should upload a new calendar since this is the last day in the calendar"
                with open ('solarlog.txt','a') as logfile:
                        logfile.write("warning the calendar is about to expire please append or change the calendar")
                nextEvent = str(e[index - 1].begin)
                tomorrow = str(e[index - 2].begin)
        else:
                print "you are in the middle of the calendar"
                nextEvent = str(e[index + 1].begin)
                tomorrow = str(e[index + 2].begin)

        #parses the next event in the calendar and creates a unix time stamp
        if e[index].name == "Sunrise":
                nextYear =  int(nextEvent[0] + nextEvent[1] + nextEvent[2] + nextEvent[3])
                nextDay = int(nextEvent[8] + nextEvent[9])
                nextMonth = int(nextEvent[5] + nextEvent[6])
                nextHour = int(nextEvent[11] + nextEvent[12]) 
                nextMinute = int(nextEvent[14] + nextEvent[15])
                nextSecond = int(nextEvent[17] + nextEvent[18])
                setTime = datetime(nextYear,nextMonth,nextDay,nextHour,nextMinute,nextSecond)
                print "the sun will set at {}".format(setTime)
                
                

                #parse the tomorrow event so it can be used later
                nextRiseYear =  int(tomorrow[0] + tomorrow[1] + tomorrow[2] + tomorrow[3])
                nextRiseDay = int(tomorrow[8] + tomorrow[9])
                nextRiseMonth = int(tomorrow[5] + tomorrow[6])  
                nextRiseHour = int(tomorrow[11] + tomorrow[12]) 
                nextRiseMinute = int(tomorrow[14] + tomorrow[15])
                nextRiseSecond = int(tomorrow[17] + tomorrow[18])
                tomorrowRise = datetime(nextRiseYear,nextRiseMonth,nextRiseDay,nextRiseHour,nextRiseMinute,nextRiseSecond)
                tomorrowDay = date(nextRiseYear,nextRiseMonth,nextRiseDay)
                #sets the current time 
                currentTime = datetime.now()
                        
                #parses the current event from the calendar and creates a unixtime stamp 
                Month = int(begin[5] + begin[6])
                Day = int(begin[8] +begin[9])
                Hour = int(begin[11] + begin[12]) #timezone offset
                Minute = int(begin[14] + begin[15])
                Second = int(begin[17] + begin[18])
                Year = int(begin[0] + begin[1] + begin[2] + begin[3])
                riseTime = datetime(Year,Month,Day,Hour,Minute,Second)
                riseDate = date(Year,Month,Day)
                        
                print "today the sun will rise at {}".format(riseTime)
                print "today the sun will set at {}".format(setTime)
                print "tomorrow the sun will set at {}".format(tomorrowRise)
                

                
                #inbetween sunrise and sunset
                if riseDate == date.today():
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
                        

                        turnNumber = 0
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
                                
                                #while datetime.now() < start + (turnNumber * wormTime):        
                                #       GPIO.output(23,False)
                                #       GPIO.output(24,False)
                                #       turnNumber = turnNumber + 1
                                #       print "the panels are in position {} of 77".format(turnNumber +1)
                        

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
