# li=[4,5,8,9,6,2,12]
# l=sorted(li,reverse=True)
# print("sorted list is ",l)
# li.sort()
# print("sorted list is ",li)
#
# # in tuple there is o sort
# # but you can use sorted
# t=(4,5,2,1,3,6,8)
# ti=sorted(t)
# print("sorted tuple is ",ti)
# # t.sort() throes error
# d={'name':'bade','age':40,'class':'A'}
# di=sorted(d)
# print("sorted dict is ",di)
# sort integers based on abs value
# li=[-6,-5,-4,1,2,3]
# l=sorted(li,key=abs)
# print("sorted li is ",l)
from operator import attrgetter
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __repr__(self):
        return '{},{},${}'.format(self.name,self.age,self.salary)
e1=Employee("naresh",24,10000)
e2=Employee("ajay",25,50000)
e3=Employee("santosh",26,25000)
employees=[e1,e2,e3]
# def e_sort(emp):
#     return emp.age
# x=sorted(employees,key=lambda e: e.name)
x=sorted(employees,key=attrgetter('name'))
# x=sorted(employees,key=getattr(Employee,'name'))
print(x)
