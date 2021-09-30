import sys

def list_details(lst):
    print("Capacity: ",(sys.getsizeof(lst)-64)//8)
    print("Size:",len(lst))
    print("Space Left:",((sys.getsizeof(lst)-64) - len(lst*8))//8)

marias_lst=[]
print("List is empty")
list_details(marias_lst)

marias_lst.append("Sugar")
print("Marias list after adding sugar:")
print(marias_lst)
print("List details:")
list_details(marias_lst)

marias_lst.append("Tea Bags")
marias_lst.append("Milk")
marias_lst.append("Biscuit")
print(marias_lst)
print("List Details:")
list_details(marias_lst)

marias_lst.insert(1,"Salt")
print(marias_lst)
print("List Details:")
list_details(marias_lst)

marias_lst.insert(1,"Honey")
print(marias_lst)
print("List Details:")
list_details(marias_lst)

marias_lst.pop(1)
print(marias_lst)
print("List Details:")
list_details(marias_lst)
