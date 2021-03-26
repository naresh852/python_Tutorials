import datetime
import math
current_subs=10000
goal_subs=85000
subs_to_go=goal_subs-current_subs
avg_subs_day=200
days_to_go=math.ceil(subs_to_go/avg_subs_day)
today=datetime.date.today()
print(today+datetime.timedelta(days=days_to_go))