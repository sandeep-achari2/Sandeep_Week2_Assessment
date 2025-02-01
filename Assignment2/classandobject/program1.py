class Employee():
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
        
employee1=Employee("sandeep",7332,"AIML")
employee2=Employee("Harish",6612,"CSM")
print(f" 1. Employee details {employee1.name}, {employee1.id}, {employee1.department}")
print(f" 2. Employee details {employee2.name}, {employee2.id}, {employee2.department}")

