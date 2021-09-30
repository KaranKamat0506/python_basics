#Python program to demonstrate  
# Creation of Array  
  
# importing "array" for array creations
import array as arr

# #Creating an array with integer type
a=arr.array('i',[1,2,3])

# #printing original integer type array
for i in range(0,3):
    print(a[i],end=" ")

# #creating an array with float type
b=arr.array('f',[1.5,2.5,4.5])

# #printing original float type array
for i in range(0,3):
    print(b[i],end=" ")

N=5
A=[]
for i in range(0,N):
    ele=int(input())
    A.append(ele)
A.reverse()
for i in range(0,N):
    print(A[i],end='\n')





