
# import sys
# # def list_details(lst):
#     #Number of elements that can be stored in the list
#     print("Capacity:",(sys.getsizeof(lst)-64)//8)

#     #Number of Elements in the list
#     print("Size:",len(lst))

#     #Number of elements that can be accomodated in the space left
#     print("Space left:",((sys.getsizeof(lst)-64) - len(lst*8))//8)

    #formula changes based on the system architecture
    #(size-36)/4 for 32 bit machines and
    #(size-64)/8 for 64 bit machines

    # 36, 64 - size of an empty list based on machine
    # 4, 8 - size of a single element in the list based on machine

# mobiles=["Samsung","Mi","LG"]
# print("List Details:")
# list_details(mobiles)

# mobiles.append("HTC")
# print("Updated List:")
# print(mobiles)
# list_details(mobiles)

S=input()
for x in S:
    print(x)
    x+=1
