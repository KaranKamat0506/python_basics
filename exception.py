#Division by zero
try:
    length=10
    width=0
    print(length/width)
except Exception:  #ZeroDivisionError 
        print("Division by zero is invalid kindly change the input")

#Variable not defined
del(width)
try:
    length/width
    print(length/width)
except Exception: #NameError
    print("Variable not defined")

#Division by zero with class name "ZeroDivisionError"
try:
    length=10
    width=0
    print(length/width)
except ZeroDivisionError:
    print("Division by zero is invalid")

#Variable not defined with class name "NameError"
try:
    del(width)
    print(length/width)
except NameError:
    print("Variable not defined")