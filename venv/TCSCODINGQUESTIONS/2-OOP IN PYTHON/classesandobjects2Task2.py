class rectangle():
    def display(self):
        print("This is a Rectangle")

    def area(self, a, b):
        self.a = a
        self.b = b
        self.are = self.a * self.b
        print(f"Area of Rectangle is  {self.are}")


class square():
    def display(self):
        print("This is a Square")

    def area(self, x):
        self.x = x
        self.ar = self.x * self.x
        print(f"Area of square is  {self.ar}")


if __name__ == '__main__':
    l = int(input())
    b = int(input())
    s = int(input())

    obj1 = rectangle()
    obj1.display()
    obj1.area(l, b)

    obj2 = square()
    obj2.display()
    obj2.area(s)