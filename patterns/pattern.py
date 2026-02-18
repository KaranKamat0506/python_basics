# floyds triangle

# 1
# 2  3
# 4  5  6
# 7  8  9  10

n=int(input("Enter the no. of rows:"))
num=1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num=num+1
    print()