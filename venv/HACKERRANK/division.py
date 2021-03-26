# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(int(a/b))
#     print(a/b)
l=[]
lowernams=[]
scores=set()
for _ in range(int(input())):
    name=input()
    score=float(input())
    l.append([name,score])
    scores.add(score)
lowerscore=sorted(scores)[1]
for name,score in l:
    if score==lowerscore:
        lowernams.append(name)

for name in sorted(lowernams):
    print(name)


