# Calculate how many Fridays there are in a month

import calendar
from datetime import datetime
from datetime import date

today = datetime.now()
cal = calendar.TextCalendar(calendar.SUNDAY)

fridays = 0
for i in cal.itermonthdays(today.year, today.month):
	if (i > 0):
		temp = today.replace(day = i)
		wd = temp.weekday()
		if (wd == 4):
			print(temp.strftime("%A, %B %d"))
			fridays += 1
	else:
		continue

print("There are %d Fridays this month" % fridays)