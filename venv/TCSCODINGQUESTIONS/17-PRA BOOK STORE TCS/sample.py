class Book:
    def __init__(self,pages,price,author,id,title):
        self.pages = pages
        self.price = price
        self.author = author
        self.title = title
        self.id = id


class BookStore:
    def __init__(self, bookStoreName, BookList):
        self.bookStoreName = bookStoreName
        self.BookList = BookList

    def findMinimumBookByid(self):
        if len(self.BookList) > 0:
            fmin = min(self.BookList, key=lambda x: x.id)
            return fmin
        else:
            return None

    def sortBookByid(self):
        L=[]
        if len(self.BookList) > 0:
              x=sorted(self.BookList, key=lambda x: x.id)
              # for i in self.BookList:
              #     L.append(i.id)
              #     L.sort()
              return x
        else:
            return None




if __name__== '__main__':
    n = int(input())
    BookList = []
    for i in range(n):
        pages = int(input())
        price = int(input())
        author = input()
        id = int(input())
        title = input()
        BookList.append(Book(pages,price,author,id,title))
    re = BookStore('urstorename', BookList)

    result1 = re.findMinimumBookByid()
    if result1:
        print(result1.pages)
        print(result1.price)
        print(result1.author)
        print(result1.id)
        print(result1.title)
    else:
        print("No data found")

    result2 = re.sortBookByid()
    if result2:
        for i in result2:
            print(i.id)
    else:
        print("No data found")