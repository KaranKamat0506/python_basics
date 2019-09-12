#_name ---> #Its a way of telling developers that it is supposed to be pvt variable or pvt property
#__name ---> Name mangling So when you put two underscores before the name of a method or an attribute Python will behind the scenes
#mangle the name change the name of that attribute and to see what it actually looks like.
#__name__

class Person():
    def __init__(self):
        self.name="Toni"
        self._secret="Hi!"
        self.__msg="I like turtles"
        self.__lol="HAHAHAHAHA"

p=Person()

print(p.name)
print(p._secret)
print(dir(p)) 
print(p._Person__msg)
print(p._Person__lol)

