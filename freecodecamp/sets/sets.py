# set=> If you want to represent a grp of unique value then set is suitable options
# Insertion Order => 40,30,20,10 
# is this preserved? Ans] You cannot preserve the order in sets but we can sort the elements.
# Heterogenous elements can be stored.
# Content of sets are mutable. The elements can be changed 
# Syntax => { }
# can apply union, intersection, difference?
set={10,20,30,40}
print(set)

#insertion order is not preserved
s={10,20,30,40}
print(type(s))
# shows set

# s1=set()
# print(type(s1))

s={10,20,30,40}
s.add(100)
print(s)