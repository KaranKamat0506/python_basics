# To check whether a number is multiple of 3 and 7
num=int(input("Enter the number"))
if num % 3 is 0 and num % 7 is 0:
    print("Number is divisible by 3 and 7")
elif num % 3 != 0 and num % 7 is 0:
    print("Number is not divisible by 3 but divisible by 7")
elif num % 3 == 0 and num % 7 != 0:
    print("Number is divisible by 3 but not7")
else:
    print("Number is not divisible by 3 and 7")