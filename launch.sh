#!/bin/bash
#This script can be added as a cron job so it starts on boot 
#move to pythondirectory and start the python sript cal.py on boot

cd /home/pi/python
python cal.py
cd /

