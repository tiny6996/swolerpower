from ics import Calendar, Event
import string
import datetime
#url = "test.ics"
url = "solarcalendar.ics"
c = Calendar(open(url).read().decode('iso-8859-1'))
size = len(c.events)

for index in range(size):
        today = datetime.date.today()
	e = c.events[index]
	test = str(e.name)
	begin = str(e.begin)
	Month = int(begin[5] + begin[6])
	Day = int(begin[8] +begin[9])
	Hours = int(begin[11] + begin[12])
	Minute = int(begin[14] + begin[15])
	Second = int(begin[17] + begin[18])
	Year =  int(begin[0] + begin[1] + begin[2] + begin[3])
	
	print Day
	print today.day
	if test == "Sunrise" and today.day == Day:
		print "the sun will rise at {} on {}".format(begin[11:16],begin[0:10])
		print "{} {} {} {} {} {}".format(Day,Month,Year,Hours,Second,Minute)
	elif test == "Sunset" and today.day == Day:
		print "the sun will set at {} on {}".format(begin[11:16],begin[0:10])
                print "{} {} {} {} {} {}".format(Day,Month,Year,Hours,Second,Minute)
        else:   
                print "fuck her right in the pussy"
                
print size
exit()
