# 1 <i<100
# avg>=70
# avg round
import math

try:
    L = []

    for i in range(9):
        L.append(int(input()))
        assert 1 < L[i] < 100
    avgA = round((L[0] + L[3] + L[6]) / 3)
    avgB = round((L[1] + L[4] + L[7]) / 3)
    avgC = round((L[2] + L[5] + L[8]) / 3)
    if avgA < 70 or avgB < 70 or avgC < 70:
        print("All trainees are unfit")
    else:
        maxavg = []
        maxavg.append(avgA)
        maxavg.append(avgB)
        maxavg.append(avgC)
        ma = max(maxavg)
        maxavg.sort(reverse=True)

        if ma == avgA:
            print('Trainee Number 1',avgA)
        if ma == avgB:
            print('Trainee Number 2',avgB)
        if ma == avgC:
            print('Trainee Number 3',avgC)
except:
    print("INVALID INPUT")






