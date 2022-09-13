class employee:
    increment_sal=2
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

'''
    Inheritance
    class base class:
        functions

    class dervied class(base class):
        functions

    object=derived class(arguments)

'''

# class Programmer(employee):  
#     def __init__(self, fname, lname, salary) -> None:
#         super().__init__(fname, lname, salary)

class Programmer(employee):
    def __init__(self, fname, lname, salary, proglang, exp) -> None:
        super().__init__(fname, lname, salary)
        self.proglang=proglang
        self.exp=exp

    def increase_salary(self):
        self.salary=int(self.salary * (self.increment_sal + 0.2))
        return self.salary
    # @classmethod
    # def change_increment(cls,amount):
    #     cls.increment_sal=amount
    

gus=Programmer("Gus","Fring",40000,"Python",1)
print(gus.increase_salary())


# print(employee.is_open("monday"))
# print(employee.is_open("tuesday"))
# print(employee.is_open("wednesday"))
# print(employee.is_open("thursday"))
# print(employee.is_open("friday"))
# print(employee.is_open("saturday"))
# print(employee.is_open("sunday"))

# walter = employee("Walter","White",35000)

# gus = employee.from_str("Gus-Fring-40000")

# jesse = employee("Jesse","Pinkman",30000)

# print(gus.fname,gus.lname,gus.salary)

# print(walter.salary)
# employee.change_increment(3)
# walter.increase_salary()
# print(walter.salary)