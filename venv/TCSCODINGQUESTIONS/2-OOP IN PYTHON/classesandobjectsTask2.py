class comp:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def add(self, o):
        self.rea = self.real + o.real
        self.im = self.img + o.img
        if self.im >= 0:
            print(f"Sum of the two Complex numbers :{self.rea}+{self.im}i")
        else:
            print(f"Sum of the two Complex numbers :{self.rea}{self.im}i")

    def sub(self, ob):
        self.real = self.real - ob.real
        self.img = self.img - ob.img
        if self.img >= 0:
            print(f"Subtraction of the two Complex numbers :{self.real}+{self.img}i")
        else:
            print(f"Subtraction of the two Complex numbers :{self.real}{self.img}i")


if __name__ == '__main__':
    real1 = int(input().strip())
    img1 = int(input().strip())

    real2 = int(input().strip())
    img2 = int(input().strip())

    p1 = comp(real1, img1)
    p2 = comp(real2, img2)

    p1.add(p2)
    p1.sub(p2)