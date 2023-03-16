from datetime import datetime
# import calendar

# get today's datetime
input_dt = datetime.today()
print('Datetime is:', input_dt)

res = input_dt.replace(day=1)
print('First day of a month:', res)

# print only date
print('Only date:', res.date())
print(res.strftime("%a %b %d %Y"))
#Wed Mar 01 2023

# print(calendar.day_name[res.weekday()])