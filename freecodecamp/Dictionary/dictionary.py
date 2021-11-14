# Dictionary is nothing but key value pairs
#Key is always immutable a number or a string
#But values can be of the form list,tiple or dictionary
d1={}
print(type(d1))
d2={"Jim":"Sales","Pam":"Office Admin","Kevin":"Accounts"}
#Keys = Jim,Pam,Kevin
#Values=Sales,Office Admin, Accounts
print(d2)
print(d2["Jim"])

#dictionary in dictionary
d2={"Jim":"Sales","Pam":"Office Admin","Kevin":"Accounts","Micheal":{"A":"Sales executive","B":"Regional Manager"}}
print(d2["Micheal"])
#now if you want to print "Regional Manager"
print(d2["Micheal"]["B"])

#updating the dictionary
d2["Angela"]="Accounts"
d2["Creed"]="QA"
d2["Jim"]="Associate Regional Manager" #Changng value of jim
print(d2)

#deleting Creed from dictionary
del d2["Creed"]
print(d2)

#d3 is just referencing to d2
#so if an element is deleted from d3 then the changes are reflected in d2 also
# d3=d2
# del d3["Angela"]
# print(d2)

#so to avoid the above situation we use copy function to create a shallow copy
d3=d2.copy()
del d3["Angela"]
print(d3)

#get function
print(d2.get("Jim"))

#to print the keys
print(d2.keys())

#to print items
print(d2.items())