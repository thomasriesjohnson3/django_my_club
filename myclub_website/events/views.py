from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

def home(request, year, month):
	name = "Tom"
	month = month.capitalize()
	# Convert month form name to number
	month_number = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# create a calendar
	cal = HTMLCalendar().formatmonth(
		year, 
		month_number)

	#get currnet year
	now = datetime.now()
	current_year = now.year
	#get current time
	time = now.strftime('%I:%M:%S %p')
	return render(request, 
		'home.html', {
		'name': name,
		'year': year,
		'month': month,
		'month_number': month_number,
		'cal': cal,
		'current_year': current_year,
		'time': time
		})
