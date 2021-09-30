def enqueue(a,b,c):
    queue.append(a)
    queue.append(b)
    queue.append(c)
    print(queue)
def dequeue():
    queue.pop(0)
    queue.pop(0)
    print(queue)
queue=[]
x=int(input())
y=int(input())
z=int(input())
enqueue(x,y,z)
dequeue()
