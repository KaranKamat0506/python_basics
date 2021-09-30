s={10,20,30,40}
# s.add(40,50)
# print(s) TypeError: add() takes exactly one argument (2 given)
v=[40,50,60,70]
s.update(v,range(5))
print(s)

#using add you can add one element at a time. it can add element at any place in set
# using update you can add multiple elements
s={10,20,30,40}
s1=s.copy()
print(s1)

s={10,20,30,40,50}
print(s)
print(s.pop())
print(s)

s={10,20,30,40,50}
print(s.remove(30))

s1={10,20,30,40}
s2={30,40,50,60}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))

