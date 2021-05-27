# Write your code here
class parent(object):
    def __init__(self, t):
        self.t = t


class son(parent):
    def __init__(self, t, sp):
        self.sp = sp
        parent.__init__(self, t)

    def son_display(self):
        valu = round(self.t * (sp / 100), 2)
        print(f"Share of Son is {valu} Million.")
        print(f"Total Asset Worth is {self.t} Million.")

    def display(self):
        print(f"Share of Parents is {round((self.t * 0.5), 2)} Million.")


class daughter(parent):
    def __init__(self, t, dp):
        self.dp = dp
        parent.__init__(self, t)

    def daughter_display(self):
        value = round(self.t * (dp / 100), 2)
        print(f"Share of Daughter is {value} Million.")
        print(f"Total Asset Worth is {self.t} Million.")

    def display(self):
        print(f"Share of Parents is {round((self.t * 0.5), 2)} Million.")


if __name__ == '__main__':
    t = int(input())
    sp = int(input())
    dp = int(input())

    obj1 = parent(t)

    obj2 = son(t, sp)
    obj2.son_display()
    obj2.display()

    obj3 = daughter(t, dp)
    obj3.daughter_display()
    obj3.display()

    print(isinstance(obj2, parent))
    print(isinstance(obj3, parent))

    print(isinstance(obj3, son))
    print(isinstance(obj2, daughter))