class employee:
    def __init__(self,fname,lname,salary) -> None:
        self.fname=fname
        self.lname=lname
        self.salary=salary

    def increase_salary(self):
        self.salary=int(self.salary * self.increment_sal)

    @classmethod
    def change_increment(cls,amount):
        cls.increment_sal=amount

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls(fname,lname,salary)

    @staticmethod
    def is_open(day):
        if day=="sunday" or day=="saturday":
            return False
        else:
            return True

print(employee.is_open("monday"))
print(employee.is_open("tuesday"))
print(employee.is_open("wednesday"))
print(employee.is_open("thursday"))
print(employee.is_open("friday"))
print(employee.is_open("saturday"))
print(employee.is_open("sunday"))

# walter = employee("Walter","White",35000)

# gus = employee.from_str("Gus-Fring-40000")

# jesse = employee("Jesse","Pinkman",30000)

# print(gus.fname,gus.lname,gus.salary)

# print(walter.salary)
# employee.change_increment(3)
# walter.increase_salary()
# print(walter.salary)