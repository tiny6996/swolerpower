from ics import Calendar, Event
import string
#url = "test.ics"
url = "solarcalendar.ics"
c = Calendar(open(url).read().decode('iso-8859-1'))
e = c.events[0]
#test = str(e.name)
size = len(c.events)
print size
#for index in range(size):
#	test = str(e.name)
#	print test 
#	if test == "Sunrise":
#		print "hello"
#	else:
#		print "goodbye"
exit()
