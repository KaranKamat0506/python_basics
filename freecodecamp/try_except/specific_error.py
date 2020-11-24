try:
    value=10/0
except ZeroDivisionError as err:
    print(err)


try:
    num=int(input("Enter the Number:"))
    print(num)
except ValueError as val_err :
    print(val_err)




  

    