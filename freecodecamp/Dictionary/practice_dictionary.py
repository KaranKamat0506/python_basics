d2={"Jim": "Salesman"}
#updating
d2["Jim"]="Co manager"
print(d2)

#clear the dictionary
d2.clear()
print(d2)

d3={"Micheal":"Regional Manager",
    "Pam":"Receptionist",
    "Ryan":"Intern",
    "Kelly":"Customer Representative"
    }
print(d3["Pam"])
print(d3["Micheal"])

#update pams job description
d3["Pam"]="Sales"
print(d3["Pam"])

#delete kellys record
d3.pop("Kelly")
print(d3)

# The update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
d1={"1":"one","2":"two"}
d1_up={"3":"three"}
d1.update(d1_up)
print(d1)

#print values
print(d3.values())

#get
print(d3.get("Pam"))