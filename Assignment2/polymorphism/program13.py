
class Shape():
    def area(self):
        pass
    
class Square(Shape):
    def __init__(self,side):
        self.side=side
        
    def area(self):
        return self.side**2
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
        
    def area(self):
        return 0.5*self.base*self.height
    
side=float(input("enter side of square: "))
base=float(input("enter base of triangle: "))
height=float(input("Enter height of the triangle: "))

square=Square(side)
triangle=Triangle(base,height)
print(square.area())
print(triangle.area())
