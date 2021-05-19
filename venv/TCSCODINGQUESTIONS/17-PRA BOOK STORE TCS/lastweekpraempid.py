class Employee:
    def __init__(self,id,name,depart,salary,role):
        self.id=id
        self.name=name
        self.depart=depart
        self.salary=salary
        self.role=role
    def calincentive(self,roleincentiveper,rolepass,emplist):
        # self.roleincentiveper=roleincentiveper
         l=[]
         for i in emplist:
             if i.role.lower==rolepass.lower:
                 incentive=i.salary*(roleincentiveper[rolepass]/100)
                 l.append(incentive)
         if l:
             return l
         else:
             return "None"


def calempsalbyrole(self,rolepass,emplist,roleincentiveper,ci):
    if ci!="None":
        newlist=[]
        for j in range(len(ci)):
            for i in emplist:
                if i.role.lower()==rolepass.lower():
                   i.salary+=ci[j]
                   newlist.append(i)
        return newlist

    else:
        return "None"

n=int(input())
roleincentiveper={}
emplist=[]
for i in range(n):
    rolename=input()
    incentiveper=int(input())
    roleincentiveper[rolename]=incentiveper
ne=int(input())
for i in range(ne):
    id=int(input())
    name=input()
    depart=input()
    salary=int(input())
    role=input()
    e=Employee(id,name,depart,salary,role)
    emplist.append(e)
rolenamepas=input()
# calempsalbyrole(rolenamepas,emplist,)
for i in emplist:
     ci=i.calincentive(roleincentiveper,rolenamepas,emplist)
     if ci!="None":
        print(ci[0])
     else:
        print("Employee Not Found")
esbrole=calempsalbyrole(rolenamepas,emplist,roleincentiveper,ci)
if esbrole!="None":
    for i in esbrole:
        print(i.id,i.name,i.salary)
else:
    print("Employee Not Found")