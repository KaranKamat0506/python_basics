numbers=[10,20,30,40,50]
laptops = ["Dell" , "HP" , "Acer", "Legion" , "Macbook"]

#extend function appends another list
laptops.extend(numbers)
print(laptops)

#append function used to append a specific element
laptops.append("Asus")
print(laptops)

#insert function takes two parameters (index,Element)
#All other values will be pushed off to the right
laptops.insert(5,60)
print(laptops)

#remove function removes a particular element
laptops.remove(60)
print(laptops)

#pop function removes the last element of the list
laptops.pop()
print(laptops)

#clear list
laptops.clear()
print(laptops)

laptops = ["Dell" , "HP" , "Acer", "Legion" , "Macbook","Macbook"]

#to check the index position of the element
print(laptops.index("HP"))

#to count the no .of times element occuring in the list
print(laptops.count("Macbook"))

#sorting ascending order
laptops.sort()
print(laptops)

#sorting reverse order
laptops.reverse()
print(laptops)

#copy list
laptops2 = laptops.copy()
print(laptops2)


