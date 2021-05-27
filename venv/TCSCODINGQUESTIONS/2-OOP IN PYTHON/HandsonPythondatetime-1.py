import datetime


def dateandtime(val, tup):
    # Write your code here
    x=[]
    if val == 1:
        y=datetime.date(*tup)
        x.append(datetime.date(*tup))
        x.append(y.strftime("%d/%m/%Y"))
        return x
    elif val == 2:
        x.append(datetime.date.fromtimestamp(*tup))
        return x
    elif val==3:
        y=datetime.time(*tup)
        x.append(y)
        x.append(y.strftime("%I"))
        return x
    elif val==4:
        y=datetime.date(*tup)
        li=[]
        x.append(y.strftime("%A"))
        x.append(y.strftime("%B"))
        x.append(y.strftime("%j"))
        return x
    else:
        y=datetime.datetime(*tup)
        x.append(y)
        return x




if __name__ == '__main__':
    val = int(input().strip())

    if val == 1 or val == 4 or val == 3:
        qw1_count = 3
    if val == 2:
        qw1_count = 1
    if val == 5:
        qw1_count = 6
    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    tup = tuple(qw1)

    ans = dateandtime(val, tup)

    print(ans)