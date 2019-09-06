#function syntax
#def functionName():
#      block-of-code

def helloWorld():  #function declaration
    print("Hello World")

helloWorld()       #function call

#function with parameters
lengthOne=20
widthOne=3
def areaofRectangle(length,width):
    area=length*width
    print(area)

areaofRectangle(lengthOne,widthOne)

#function with return values
def areaofRectangle2(length,width):
    area=length*width
    return area

area2=areaofRectangle2(lengthOne,widthOne)
print(area2)

#function with parameters
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd NUmber:"))
def addition(one,two):
    a=x+y
    print(a)

addition(x,y)

#function with return values
def subtraction(first,second):
    a=x-y
    return a
diff=subtraction(x,y)
print(diff)
