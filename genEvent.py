from ics import Calendar
from ics import Event
c = Calendar
e = Event()
e.name = "fucking bitches"
e.begin = '20160122 00:00:00'
#e.end = '20160122 01:00:00'
#c.events.append(e)
c.events

with open('test.ics','w') as f:
	f.writelines(c)

