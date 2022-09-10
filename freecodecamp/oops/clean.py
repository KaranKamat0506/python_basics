class employee:
    def __init__(self,fname,lname,age) -> None:
        self.fname=fname
        self.lname=lname
        self.age=age

walter=employee("Walter","White",52)
jesse=employee("Jesse","Pinkman",30)

print(walter.fname,jesse.age)