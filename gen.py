# CALENDARDAY,CALENDARYEAR,CALENDARWEEK,PLANNINGMONTH
# 1990-01-01,1990,199001,199001
# 1990-01-02,1990,199001,199001
# 1990-01-03,1990,199001,199001

import datetime as dt
import itertools
from dateutil.rrule import rrule, DAILY

first = dt.datetime.strptime("1990-01-01", '%Y-%m-%d')
last = dt.datetime.strptime("2029-12-31", '%Y-%m-%d')



months52weeks = [
    [1] * 4,
    [2] * 4,
    [3] * 5,
    [4] * 4,
    [5] * 4,
    [6] * 5,
    [7] * 4,
    [8] * 4,
    [9] * 5,
    [10] * 4,
    [11] * 4,
    [12] * 5,
]
months53weeks = [
    [1] * 4,
    [2] * 4,
    [3] * 5,
    [4] * 4,
    [5] * 4,
    [6] * 5,
    [7] * 4,
    [8] * 4,
    [9] * 5,
    [10] * 4,
    [11] * 5,
    [12] * 5,
]
months52weeks = list(itertools.chain(*months52weeks))
months53weeks = list(itertools.chain(*months53weeks))

print("CALENDARDAY,CALENDARYEAR,CALENDARWEEK,PLANNINGMONTH")
for day in rrule(DAILY, dtstart=first, until=last):

    date_year = day.strftime("%Y")
    date_month = day.strftime("%m")

    # years from weeks are different from years from date
    # as week 01 is sometimes in prev year, also
    # w53 in next
    week_year, week_week, week_day = day.isocalendar()

    # Jan 4th is always week one. With same logic
    # Dec 28th is always the last week (52 or 53)
    # note it is based on week_year not date_year
    last_week = (dt.date(int(week_year), 12, 28)).isocalendar()[1]
    if last_week == 53:
        months = months53weeks
    else:
        months = months52weeks
    print(f'{day.strftime("%Y-%m-%d")},{date_year},{week_year}{week_week:02d},{week_year}{months[week_week-1]:02d}')
