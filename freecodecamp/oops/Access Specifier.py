# _protected
#__private

class Test:
    x=10 #public
    _y=20 #protected
    __z=30 #private
    def method(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)
t=Test()
t.method()
print(Test.x)
print(Test._y)
print(t._Test__z)
# print(Test.__z)
# Attribute error 
#object reference._classname__variablename = you can access private 

