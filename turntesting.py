import RPi.GPIO as GPIO
import time as time
turnTime = float(5.74)
#pin numbers for each gear
wormpin1 = 23
wormpin2 = 24
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
print "I am ready"
time.sleep(2)

while True:
    #Turn all the motors one way
    print "Imma go this way"
    GPIO.output(leftact1,True)
    GPIO.output(leftact2,False)
    GPIO.output(rightact1,True)
    GPIO.output(rightact2,False)
    GPIO.output(wormpin1,True)
    GPIO.output(wormpin2,False)
    time.sleep(turnTime)

    #stop
    print "Imma Stop"
    GPIO.output(leftact1,False)
    GPIO.output(leftact2,False)
    GPIO.output(rightact1,False)
    GPIO.output(rightact2,False)
    GPIO.output(wormpin1,False)
    GPIO.output(wormpin2,False)
    time.sleep(turnTime)

    #Then the other
    print "Imma go the other way"
    GPIO.output(leftact1,False)
    GPIO.output(leftact2,True)
    GPIO.output(rightact1,False)
    GPIO.output(rightact2,True)
    GPIO.output(wormpin1,False)
    GPIO.output(wormpin2,True)
    time.sleep(turnTime)




