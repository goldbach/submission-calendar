# CALENDARDAY,CALENDARYEAR,CALENDARWEEK,PLANNINGMONTH
# 1990-01-01,1990,199001,199001
# 1990-01-02,1990,199001,199001
# 1990-01-03,1990,199001,199001

import datetime as dt
from dateutil.rrule import rrule, DAILY
from collections import defaultdict

first = dt.date(1990, 1, 1)
last = dt.date(2029, 12, 31)


def cal2month(week_str):
    # translate above into week index array -> month
    arr = []
    for month, elem in enumerate(map(int, week_str), start=1):
        for _ in range(elem):
            arr.append(month)
    return arr


q4_445 = cal2month("445445445445")
q4_446 = cal2month("445445445446")
q4_455 = cal2month("445445445455")


calendarsbyyear = defaultdict(lambda: q4_445)  # default 52 weeks
calendarsbyyear.update({
    1992: q4_455,
    1998: q4_455,
    2004: q4_446,
    2009: q4_455,
    2015: q4_455,
    2020: q4_455,
    2026: q4_455,
    # 2032: ??,
})


print("CALENDARDAY,CALENDARYEAR,CALENDARWEEK,PLANNINGMONTH")
for day in rrule(DAILY, dtstart=first, until=last):

    date_year = day.strftime("%Y")
    date_month = day.strftime("%m")
    date = day.strftime("%Y-%m-%d")
    # years from weeks are different from years from date
    # as week 01 is sometimes in prev year, also
    # w53 in next
    week_year, week_week, week_day = day.isocalendar()

    months = calendarsbyyear[week_year]
    try:
        print(f'{date},{date_year},{week_year}{week_week:02d},{week_year}{months[week_week-1]:02d}')
    except IndexError:
        print(f"{week_year} is a w53 year -- please add Q4 weeks to config")
        raise
