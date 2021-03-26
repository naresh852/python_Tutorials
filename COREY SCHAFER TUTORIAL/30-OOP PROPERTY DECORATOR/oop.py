class Employee:
    def __init__(self,first,last):
        self.first=first
        self.last=last


    #usind property decorator
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    #using setters
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last
    #deleter to delete values
    @fullname.deleter
    def fullname(self):
        print("Deleted all!")
        self.first=None
        self.last=None


emp_1=Employee('sim','reddy')
emp_1.fullname="nare reddy"
print(emp_1.first)                                                                     # print()
# print(emp_1.fullname())
print(emp_1.fullname) #for property decorator no need ()
print(emp_1.email)
del emp_1.fullname