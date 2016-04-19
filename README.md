# Swolerpower


## About

This project is designed to enable solar panels to track the sun. Swolerpower is the codename for one of the Loras College Engineering capstone projects for the 2016 class. it as designed by Mathias, Alex, Nik, and Joe.

The panels are controled by a raspberry pi model b running Raspbian lite. On boot a python script that runs that moves the panels for brief period and has controled delays that change based on the daylength.

The frame was custom designed using various steel parts, a flywheel from a 2009 F350 flywheel, and an aluminum bearing.

## Electrical Hardware
* A raspberry pi model B 
* A L298N H bridge
* 4 solar 20V solar panels wired in parallel 
* 2 8 inch linear actuators 
* 1 12V motor to the rotation of the worm gear 

## Software 
* OS: Raspbian lite 
* All programs written in python 2 
* Main program uses the ephem library to calculate the sunset times 


### WasdDemo
This code was designed to show off the project off at the loras college Legacy Symposium. It moves the panels up, down, left, or right based on user input and can be exited by typing exit 

### main
This code is desinged to calculate the day length at the beginning of each day using the ephem library. After the day length is cut into small chucks based on the day length. For every chunk of the day it pulses the motors so it follows the sun. At the end of the day the panels move back to the sun rise position. Then the panels will remain in the same position until the next sunrise.  


## Wiring 
* to be filled in by team members that know what they are doing 

## Frame design and hardware
* Custom worm gear made by Morrison Brother's Engineering
* Rest of design made by 

## Thanks 
* Dr. Danial Neebel
* Loras College 
* Morrison Brother's Engineering 

