
class Employee:
    empcount=0
    raiseA=1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.empcount+=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def raiseAm(self):
        self.pay=int(self.pay*Employee.raiseA)
        # return f'raised amount is {self.pay*Employee.raiseA} '


print(Employee.empcount)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1.pay)
print(Employee.raiseAm(emp_1))
print(emp_1.pay)
print(Employee.raiseAm(emp_1))
print(Employee.empcount)
