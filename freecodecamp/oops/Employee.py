class Employee:
    def __init__(self) -> None:
        self.name="Jim"
        self.age=20
        self.salary=30000
    def display(self):
        print("Name:{}\nAge:{}\nSalary:{}".format(self.name,self.age,self.salary))
e1=Employee()
e1.display()