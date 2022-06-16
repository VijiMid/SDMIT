
import calendar

htmlcal = calendar.HTMLCalendar(calendar.MONDAY)
print(htmlcal.formatmonth(int(input("Enter Year : ")), int(input("Enter Month : "))))
