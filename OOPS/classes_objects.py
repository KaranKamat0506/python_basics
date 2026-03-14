class Person:
    name = "Harry"
    age=20
    occupation="Software Engineer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person() #Here a is an object and Person is class
c=Person()
print(a.name)
print(a.age)
print(a.occupation)
a.name="Tom" # Assigned a new value to property name
print(a.name)
a.info()
c.info() #The default values of the class will get printed.
"""
Harry is a Software Engineer
"""
