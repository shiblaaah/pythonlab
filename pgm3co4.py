class Rectangle:
    def __init__(self, l, w):
        self.__l = l
        self.__w = w

    def area(self):
        return self.__l * self.__w

    def __lt__(self, other):
        return self.area() < other.area()


l1 = float(input("Enter length of Rectangle 1: "))
w1 = float(input("Enter width of Rectangle 1: "))
l2 = float(input("Enter length of Rectangle 2: "))
w2 = float(input("Enter width of Rectangle 2: "))

r1 = Rectangle(l1, w1)
r2 = Rectangle(l2, w2)

if r1 < r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 has smaller area")
