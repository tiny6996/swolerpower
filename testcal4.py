from ics import Calendar, Event
import string
import datetime
url = "test.ics"
#url = "solarcalendar.ics"
c = Calendar(open(url).read().decode('iso-8859-1'))
size = len(c.events)

for index in range(size):
	e = c.events[index]
	test = str(e.name)
	begin = str(e.begin)
	print test
	print begin 
	if test == "Sunrise":
		print "the sun will rise at {} on".format(begin[11:16],begin[0:10])
	else:
		print "the sun will set at {} on {}".format(begin[11:16],begin[0:10])
#	Month = int(begin[5] + begin[6])
#	Day = int(begin[8] +begin[9])
#	Hours = int(begin[12] + begin[13])
#	Minute = int(begin[16] + begin[17])
#	Second = int(begin[18] + begin[19])
#	Year =  int(begin[0] + begin[1] + begin[2] + begin[3])
#	print "{} {} {} {} {} {}".format(Day,Month,Year,Hours,Seconds, Minutes)
print size
exit()
