class Book:
    def __init__(self,pages,price,author,id,title):
        self.pages=pages
        self.price=price
        self.author=author
        self.id=id
        self.title=title
class Bookstore:
    def __init__(self,bstorename,booklist):
        self.bstorename=bstorename
        self.booklist=booklist

    def sortbookbyid(self):
        l = []
        for i in self.booklist:
            l.append(i.id)
            l.sort()
        if(len(l)>0):
            return l
        else:
            return "None"
    def findminimumbookbyid(self):
        x=Bookstore.sortbookbyid(self)
        if x!="None":
            for i in self.booklist:
                if i.id==x[0]:
                  return i

        else:
            return "None"

if __name__=='__main__':
    n=int(input())
    booklist=[]
    for i in range(n):
        pages=int(input())
        price=int(input())
        author=input()
        id=int(input())
        title=input()
        b=Book(pages,price,author,id,title)
        booklist.append(b)
    bs=Bookstore("nareshstore",booklist)
    res=bs.findminimumbookbyid()
    res1=bs.sortbookbyid()
    if res!="None":
        print(res.pages,res.price,res.author,res.id,res.title,sep="\n")
    else:
        print("No data found")
    if res1!="None":
       for i in res1:
           print(i)
    else:
        print("No data found")
