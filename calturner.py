import gdata.calendar.service
import gdat.service
import atom.service
import gdata.calendar
import gdata.calendar
import atom
import getopt
import sys
import string
import time

import xe
from feed.date.rfc3339 import tf_from_timestamp
from datetime import datetime
from apscheduler.scheduler import Schedule

calendar_service = gdata.claendar.service.CaendarService()
email = 'loras.solar@gmail.com'
password = '1slick1!'
calendar_service.source ='John Cena'
calendar_service.ProgrammaticLoogin()

def FulltextQuery(calendarsetvice, text_query = 'sunrise'
	print 'full text query for events on Primary Calendar: \'%s\'' %(text_query,)
	query = gdata.calendar.service.CalendarEventQuery('default','private','full',text_query)
	feed = calendar_service.CalendarQuery(query)
