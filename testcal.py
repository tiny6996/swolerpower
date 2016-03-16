from ics import Calendar, Event
import string
#url = "test.ics"
url = "solarcalendar.ics"
c = Calendar(open(url).read().decode('iso-8859-1'))
e = c.events[0]
test = str(e.name)
print test 
if test == "Sunrise":
	print "the sun will rise"
else:
	print "you is a bitch"
exit()
