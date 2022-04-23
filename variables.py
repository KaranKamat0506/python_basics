'''
Variables, Datatypes and Typecasting
'''

var1="Hello World" #String Variable
var2=30 # Integer Variable
var3=30.5 #Float variable
var4="37" #Int variable but stored as string 
var5="47" #int variable but stored as string

print(var1)
print(var2+var3) # Output would be in floating no.

print(type(var1),type(var2),type(var3))

print(var4+var5) # 37 47 would be printed. 
print(int(var4)+int(var5)) #84 will be printed

print(100 * "Hello World\n") 

'''
 add two no.
'''

n1=int(input("Enter first no:"))
n2=int(input("Enter second no:"))
print("Addition:",n1+n2)