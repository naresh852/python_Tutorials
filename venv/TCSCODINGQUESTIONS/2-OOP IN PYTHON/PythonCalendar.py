import calendar
import datetime


def usingcalendar(datetuple):
    # def checklpyr(a):
    #     if a%1==0 and a%100 !=0:
    #         return True
    #     elif a%100==0:
    #         return False
    #     elif a%400==0:
    #         return True
    #     else:
    #         return False
    r = calendar.isleap(datetuple[0])
    nt = []
    if r:
        nt.append(datetuple[0])
        nt.append(2)
        nt.append(datetuple[2])
    else:
        nt = list(datetuple)
    print(calendar.month(nt[0], nt[1]))
    obj = calendar.Calendar()
    md = []
    for i in obj.itermonthdates(nt[0], nt[1]):
        md.append(i)
    l = len(md)
    print(md[l - 7:l:1])
    # print(md)
    obj1 = calendar.Calendar()
    md1 = []
    for i in obj1.itermonthdays2(nt[0], nt[1]):
        md1.append(i)
    # print(md1)

    # print(md1)
    dic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in md1:
       if i[0] != 0:
            dic[i[1]] += 1
    for j in md1:
        if j[0]!=0:
            ss=j[1]
            break
    # print(ss)
    # print(dic.items())
    maxi = max(dic.values())
    co=0
    nl=[]
    for i in range(7):
        if dic[i] == maxi:
            result = i
            nl.append(result)
            co+=1
    # print(result)
    d={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    if co>1:
        for j in nl:
            if j==ss:
                result=j

    print(d[result])

if __name__ == '__main__':
    qw1 = []

    for _ in range(3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    tup = tuple(qw1)

    usingcalendar(tup)