# | Feature    | List   | Tuple   | Set  |
# | ---------- | -------| -----   | ---- |
# | Mutable    | ✅     | ❌     | ✅   |
# | Ordered    | ✅     | ✅     | ❌   |
# | Duplicates | ✅     | ✅     | ❌   |


number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(number[3])
number.remove(3)
number.remove(number[3])
print(number)
number[0] = 100
print(number)

tuple1=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,14)
#tuple1[0]=100 # 'tuple' object does not support item assignment
print(tuple1)

my_set={1,2,3,4,5,6,7,8,9,10,11,12,13,14}
print("Set:" , my_set)
my_set.add(4) # Doesn't repeat elements
my_set.add(100) # Adds new element mutable
print(my_set)
#print(my_set[0]) #TypeError: 'set' object is not subscriptable






