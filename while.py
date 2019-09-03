temperature=77
while temperature>=68 and temperature<=77:
    print("Room temperature is maintained at {} degree fahrenheit".format(temperature))
    temperature=temperature-1

#Print even no. from the range of 1 to 100 using while loop
x=100
while x>=1 and x<=100 :
    if x%2==0:
       print("{} is an even number".format(x))
    x=x-1

#Infinite loop
while True:
    print("This is an infinite loop")
