
class Vechile():
    def __init__(self,name):
        self.name=name
        
    def display(self):
        print(f"It is a Vechile  {self.name}")
    
class Car(Vechile):
    def __init__(self,name):
        super().__init__(name)
        
    def display(self):
        print(f"It is a car {self.name}")
        
class Bike(Vechile):
    def __init__(self,name):
        super().__init__(name)
        
    def display(self):
        print(f"It is a bike {self.name}")
        
class Electriccar(Car):
    def __init__(self,name):
        super().__init__(name)
        
    def display(self):
        print(f"It is an electric car {self.name}")

vechile=Vechile("Vechile")
car=Car("Tata")
bike=Bike("Honda")
electriccar=Electriccar("Tata Electric")

vechile.display()
car.display()
bike.display()
electriccar.display()