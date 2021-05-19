class Team:
    def __init__(self,owner,value,id,name):
        self.owner=owner
        self.value=value
        self.id=id
        self.name=name
class League:
    def __init__(self,leaguename,teamlist):
        self.leaguename=leaguename
        self.teamlist=teamlist
    def sortteambyid(self):
        l=[]
        for i in self.teamlist:
            l.append(i.id)
        l.sort()
        if len(l)!=0:
            return l
        else:
            return "NONE"
    def findminimumteambyid(self):
        x=League.sortteambyid(self)
        for i in self.teamlist:
            if i.id==x[0]:
                return i
        return "NONE"
if __name__=='__main__':
    n=int(input())
    teamlist=[]
    for i in range(n):
        owner=input()
        value=int(input())
        id=int(input())
        name=input()
        T=Team(owner,value,id,name)
        teamlist.append(T)
    L=League("Naresh team",teamlist)
    res=L.findminimumteambyid()
    res1=L.sortteambyid()
    if res!="NONE":
        print(res.owner,float(res.value),res.id,res.name,sep="\n")
    else:
        print("No Data Found")
    if res1!="NONE":
        print(*res1)
    else:
        print("No Data Found")