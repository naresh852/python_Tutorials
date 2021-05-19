class Subject:
    def __init__(self,code,name,credit,teacher,subavg):
        self.code=code
        self.name=name
        self.credit=credit
        self.teacher=teacher
        self.subavg=subavg

class Grade:
    def __init__(self,grade,subjectlist):
        self.grade=grade
        self.subjectlist=subjectlist

    def sortsubjectbysubavg(self):
        x=sorted(self.subjectlist,key=lambda x:x.subavg)
        if(len(x)>0):
            return x
        else:
            return "NONE"
    def findmaximumsubjectbycredit(self):
        if len(self.subjectlist)>0:
               y=max(self.subjectlist,key=lambda x:x.credit)
               return y
        else:
            return "NONE"
if __name__=='__main__':
    n=int(input())
    subjectlist=[]
    for i in range(n):
        code=input()
        name=input()
        credit=int(input())
        teacher=input()
        subavg=float(input())
        s=Subject(code,name,credit,teacher,subavg)
        subjectlist.append(s)
    g=Grade("A",subjectlist)
    res=g.findmaximumsubjectbycredit()
    res1=g.sortsubjectbysubavg()
    if(res!="NONE"):
        print(res.code,res.name,res.credit,res.teacher,res.subavg,sep="\n")
    else:
        print("No Data Found")
    if(res1!="NONE"):
        for i in res1:
            print(i.subavg)
    else:
        print("No Data Found")

