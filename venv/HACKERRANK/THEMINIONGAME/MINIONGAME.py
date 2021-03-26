
# print(s)
def calculate(lis):
    score = 0
    kscore = 0
    for i in range(length):
        if lis[i]=="A" or lis[i]=="E" or lis[i]=="I" or lis[i]=="O" or lis[i]=="U":
            score=score+length-i
        if lis[i]!="A" and lis[i]!="E" and lis[i]!="I" and lis[i]!="O" and lis[i]!="U":
            kscore=kscore+length-i

    if score > kscore:
        print("Kevin " + str(score))
    elif score < kscore:
        print("Stuart "+ str(kscore))
    else:
        print("Draw")
s=input()
length=len(s)
calculate(s)


# vowel="AEIOU"
#     length=len(lis)
#     for i in range(length):
#         if lis[i] in vowel:
#             score=score+length-i
#         else:
#             kscore=kscore+length-i
