import datetime
current_weight=220
goal_weight=180
avg_wt_lose_week=1.5
start_date=datetime.date.today()
end_date=start_date
while current_weight>goal_weight:
    end_date+=datetime.timedelta(days=7)
    current_weight-=avg_wt_lose_week
print(end_date)
print(f"goal reached in {(end_date-start_date)//7} weeks")
