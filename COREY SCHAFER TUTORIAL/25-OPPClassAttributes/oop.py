class Employee:
    #class variables are variables that are shared a,omong all instancs of a class
#instance variables are unique for each instance
    def __init__(self, first, last, pay):
        #instance variables
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1.fullname())
print(Employee.fullname(emp_2))


