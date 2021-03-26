import calendar
month,day,year=map(int,input().split())
# day_r=calendar.weekday(year,month,day)
# print(calendar.day_name[day])
day_r=calendar.day_name[calendar.weekday(year,month,day)].upper()
print(day_r)
