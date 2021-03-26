#regular methods automatically pass (self) instance as first arugumrnt
#class methods automatically pass (cls) instance as first arugumrnt
#static method do not pass instance as first argument
class Employee:
    empcount=0
    raiseA=1.04

    # regular methods automatically pass (self) instance as first arugumrnt
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.empcount+=1

    # regular methods automatically pass (self) instance as first arugumrnt
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # regular methods automatically pass (self) instance as first arugumrnt
    def raiseAm(self):
        self.pay=int(self.pay*Employee.raiseA)
        # return f'raised amount is {self.pay*Employee.raiseA} '
    # class methods automatically pass (cls) instance as first arugumrnt
    @classmethod
    def setnewraise(cls,amount):
        cls.raiseA=amount

    # class methods automatically pass (cls) instance as first arugumrnt
    @classmethod
    def set_String(cls,string):
        first,last,pay=string.split('-')
        return Employee(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
import datetime
myday=datetime.date(2020,5,11)
print(Employee.is_workday(myday))
print(Employee.empcount)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
# print(emp_1.pay)
# print(Employee.raiseAm(emp_1))
# print(emp_1.pay)
# print(Employee.raiseAm(emp_1))
# print(Employee.empcount)
# Employee.setnewraise(1.05)
# print(Employee.raiseA)
emp1='ajay-reddy-48658'
emp2='nare-reddy-400000'
emp3='santosh-reddy-250000'
new_emp1=Employee.set_String(emp1)
print(new_emp1.first)
print(new_emp1.last)