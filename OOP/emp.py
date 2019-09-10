class Employee:
    def __init__(self):   
        #without self keyword
        print("\nEnter the name of Employee:")
        emp_name=input()
        print("\nEnter the Salary of Employee:")
        emp_sal=int(input())
        print("\nName of the Employee: {}".format(emp_name))
        print("\nSalary of the Employee: {}".format(emp_sal))

emp1=Employee()
emp2=Employee()


#using self keyword
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

e1=employee("John",240000)
e2=employee("Pat",450000)
print("\n",e1.name,"\n",e1.salary)
print("\n",e2.name,"\n",e2.salary)


