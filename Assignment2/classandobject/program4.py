
class Student():
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        
    def display(self):
        return f'Student name {self.name} along with roll number {self.roll_number}'

student=Student("sandeep",7332)
print(student.display())