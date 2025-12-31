from abc import ABC, abstractmethod


# class Account(ABC):
#     def displaydepositlimit(self):
#         pass

#     @abstractmethod
#     def displayWithdrawlimit(self):
#         pass


# class Current(Account):
#     def displaydepositlimit(self):
#         print("dep lmt 1000000")

#     def displayWithdrawlimit(self):
#         print("wthdrw limt 1000000")


# class Savings(Account):
#     def displaydepositlimit(self):
#         print("dep 1000000")

#     def displayWithdrawlimit(self):
#         print("wthdrw lmt 500")


# x = Current()
# x.displaydepositlimit()
# x.displayWithdrawlimit()

# y = Savings()
# y.displaydepositlimit
# y.displayWithdrawlimit()


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    r = float(input("Enter radius of circle : "))
    def area(self, r=r):
        print(f"Area of circle : {3.14*r*r}\n")

    def perimeter(self, r=r):
        print(f"Perimeter of circle : {2*3.14*r}\n")


class Triangle(Shape):
    a = float(input("Enter side 1 (BASE) : "))
    b = float(input("Enter side 2 : "))
    c = float(input("Enter side 3 : "))
    p = float(input("Enter perpendicular : "))

    def area(self, a=a, p=p):
        print(f"Area of triangle : {0.5*a*p}\n")
    def perimeter(self,a=a,b=b,c=c):
        print(f"Perimeter of triangle : {a+b+c}\n")

class Square(Shape):
    s = int(input("Enter size of square : "))

    def perimeter(self, side=s):
        print(f"Perimeter (sq.): {4*side}\n")

    def area(self, side=s):
        print(f"Area (sq) : {side * side}\n")

c = Circle()
c.area()
c.perimeter()

s = Square()
s.area()
s.perimeter()

t = Triangle()
t.area()
t.perimeter()