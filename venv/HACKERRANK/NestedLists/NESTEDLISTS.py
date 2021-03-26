friends=[]
scores=[]
names=[]
rang = int(input())
for _ in range(rang):
    name = input()
    score = float(input())
    col=[]
    col.append(name)
    col.append(score)
    friends.append(col)
for index in range(rang):
    names.append(friends[index][0])
    scores.append(friends[index][1])
scores.sort()
minx=scores[1]
if minx ==scores[0]:
    minx=scores[2]
if minx == scores[0] and minx == scores[2]:
    minx=scores[3]
dups=1
if scores.count(minx)>1:
        dups=dups+1
else:
        dups=0

print(dups)
new=[]
if dups>=2:
    for index in range(rang):
        if minx==friends[index][1]:
            new.append(friends[index][0])
elif dups==0:
    for index in range(rang):
        if minx==friends[index][1]:
            new.append(friends[index][0])
new.sort()
for index in range(len(new)):
        print(new[index])













