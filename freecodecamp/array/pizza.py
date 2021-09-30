n=int(input('Elements to be stored:'))
A=[]
for i in range(0,n):
    ele=int(input())
    A.append(ele)
A.sort()
for i in range(0,n):
    print(A[i],end='\n')


first_half=A[:len(A)//2]
second_half=A[len(A)//2:] 
print(first_half[1]+second_half[1])



