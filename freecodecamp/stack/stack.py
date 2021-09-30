def push_op(a,b):
    stack.append(a)
    stack.append(b)
def pop_op():
    stack.pop()
    print(stack)
stack=[]  
x=int(input("Enter 1st element:"))
y=int(input("Enter 2nd element:"))
push_op(x,y)
pop_op()