class Person:
    def __init__(self,n,o):
        print("Hey i am person")
        self.name=n
        self.occ=o

    def getInfo(self):
        print(f"{self.name} is {self.occ}")

a=Person("Harry","Developer")
b=Person("Tom","Tester")
c=Person(1,2,3)
#TypeError: Person.__init__() takes 3 positional arguments but 4 were given
# 4 arguments means it is counting self as well
a.getInfo()