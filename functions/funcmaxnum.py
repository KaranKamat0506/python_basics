#Program to find greatest number among two numbers 
def compare(first,second):
    if a > b:
        print("{} is greater than {}".format(a,b))
    elif a < b:
        print("{} is greater than {}".format(b,a))
    else:
        print("Both are equal")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
compare(a,b)

