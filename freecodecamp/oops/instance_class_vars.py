class employee:

    increment=1.5 #class variable
    no_of_employees=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4 #object variable 
        employee.no_of_employees +=1

    def increase_salary(self):
        self.salary=int(self.salary*employee.increment)


print(employee.no_of_employees)
walter=employee("Walter","White",35000)
jesse=employee("Jesse","Pinkman",30000)
print(employee.no_of_employees)

print(walter.salary) 
walter.increase_salary()
print(walter.salary)
print(walter.__dict__)