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
        self.pay=int(self.pay*self.raiseA)
        # return f'raised amount is {self.pay*Employee.raiseA} '
class Developer(Employee):
    raiseA=2.10
    def __init__(self,first,last,pay,prglang):
        #if u use super no need self
        super().__init__(first,last,pay)
        #you can use employee but use self
        # Employee.__init__(self,first,last,pay)
        self.prglang=prglang
class manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())

# print(Employee.empcount)
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)
dev_1 = Developer('Corey', 'Schafer', 50000,'python')
dev_2 = Developer('Test', 'Employee', 60000,'java')
mgr_1=manager('sue','sureddy',6000,[dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.rem_emp(dev_1)
mgr_1.print_emp()
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,manager))
print(isinstance(mgr_1,Developer))
# print(isinstance(dev_1,manager))
print(issubclass(Developer,Employee))
print(issubclass(manager,Employee))
print(issubclass(manager,Developer))
# print(dev_1.first)
# print(dev_2.first)
# print(help(Developer))
# print(dev_1.pay)
# dev_1.raiseAm()
# print(dev_1.pay)
# print(emp_1.pay)
# emp_1.raiseAm()
# print(emp_1.pay)
print(dev_1.first)
print(dev_1.prglang)

