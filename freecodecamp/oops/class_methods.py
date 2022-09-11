class employee:

    inc_sal=1.5
    no_of_employees=0

    def __init__(self,fname,lname,salary) -> None:
        self.fname=fname
        self.lname=lname
        self.salary=salary
        # self.increment_sal=1.4
       

    def increase_salary(self):
        self.salary=int(self.salary * self.increment_sal)

    @classmethod
    def change_increment(cls,amount):
        cls.increment_sal=amount
   

walter = employee("Walter","White",35000)
jesse = employee("Jesse","Pinkman",30000)

print(walter.salary)
employee.change_increment(3)
walter.increase_salary()
print(walter.salary)




