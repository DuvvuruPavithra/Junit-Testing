# Find the day of the week for a given date in Python

# import calendar module
import calendar


def day_of_week():
    day = int(input('Enter the value of day:'))
    month = int(input('Enter the value of month:'))
    year = int(input('Enter the value of year:'))

    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    day_of_weeks = calendar.weekday(year, month, day)
    print('Weekday is:', day_name[day_of_weeks])


day_of_week()
