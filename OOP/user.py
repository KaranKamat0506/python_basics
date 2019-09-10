#program to define a class
class User:
    def __init__(self,first,last):
        self.first=first
        self.last=last


user1=User("Jon","Matt")
user2=User("Pat","Strout")
user3=User("Jesse","Pinkman")
print(user1.first,user1.last)
print(user2.first,user2.last)
