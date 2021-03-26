print('Enter current time(hour.min) float')
ct=float(input())
sl=['PANVEL', 'KHANDESHWAR', 'MANSAROVAR', 'KHARGHAR', 'BELAPUR','SEAWOOD', 'NERUL']
print(sl)
print('At which station you are right now? (Choose from above)')
pst=input().upper()
trsttimes=[7.30, 8.2, 12.45, 13.30, 14.44, 15.50, 9.15, 10.20, 23.59, 17.33, 19.20]
traveltime=[0,4,5,3,4,5,3]
for i in range(7):
    if sl[i]==pst:
        count=i
s=0
for i in range(count+1):
    s=s+traveltime[i]
nooftrains=0
remaintime=24.0-ct
for i in range(11):
    totaltime=s+trsttimes[i]
    if totaltime>24:
        nooftrains=nooftrains
    elif totaltime>=remaintime:
        nooftrains+=1
print(nooftrains)

