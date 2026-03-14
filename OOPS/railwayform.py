class railwayform:
    name="Tom"
    age=18
    board="Mumbai"
    drop="Chennai"
    def getInfo(self):
        print(f"{self.name} is {self.age} years old and traveling from {self.board} to {self.drop}")

a=railwayform()
b=railwayform()
print(a.name)
b.name="Harry"
b.age=18
b.board="Pune"
b.drop="Mumbai"
b.getInfo()