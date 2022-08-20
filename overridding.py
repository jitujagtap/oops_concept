class Polygon():
    def area(self):
        print("Area of Polygon")
    def perimeter(self):
        print("Perimeter of Polygon")

class Triangle(Polygon):
    def area(self):
        print("Area of Triangle")
    def perimeter(self):
        print("Perimeter of Triangle")

class Square(Polygon):
    def area(self):
        print("Area of Square")
    def perimeter(self):
        print("Perimeter of Square")

s = Square()
s.area()

t = Triangle()
t.perimeter()