# Exponent Function using for loop
def exp(base_num,pow_num):
    result=1
    for index in range(pow_num):
        result=result*base_num
    print(result)
base=int(input("Enter the Base Number: "))
power=int(input("Enter the Power Number: "))
exp(base,power)

#Exponent 
print(2**3)