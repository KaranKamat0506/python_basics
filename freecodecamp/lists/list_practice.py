list1=["Element1","Element2","Element3","Element4","Element5"]
print(list1[1])

#print list from index 1 element onwards
print(list1[1:])

#print list from a certain element to a particular element
print(list1[1:4])

#reverse index
print(list1[-1])

list1[1]="Element8"
print(list1)

list1[1]="Element2"
print(list1)

#List Functions
list2=["Element6","Element7","Element8","Element9","Element10"]
#extend function
list1.extend(list2)
print(list1)

#append fucntion
list1.append("Element11")
print(list1)

#sort function
list1.sort()
print(list1)

#reverse function
list1.reverse()
print(list1)

#insert function
list1.insert(4,"Element5")
print(list1)

#index function
print(list1.index("Element1"))

#count function
print(list1.count("Element5"))

#pop function
list1.pop()
print(list1)

#copy function
list3=list1.copy()
print(list3)

#remove function
list3.remove("Element4")
print(list3)

#clear function
list3.clear()
print(list3)




