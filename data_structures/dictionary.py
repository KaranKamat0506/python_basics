#dictionary syntax
#dictionaryname={key1:value1,key2:value2}
laptops={"Dell":50000,"HP":60000,"Acer":40000}
print(laptops)
print(laptops["Dell"])
laptops["HP"]=65000 
print(laptops["HP"])

#dictionary2
mobilephones={"Samsung":21000,"Asus":19000,"Motto":12000}
print("\nElements of another dictionary:{}".format(mobilephones))
print(mobilephones["Samsung"])
mobilephones["Motto"]=15000
print(mobilephones["Motto"])

#operations performed on dictionary
print("\nOperations performed on dictionary:")
print(mobilephones.keys())
print(mobilephones.values())
copyofmobilephones=mobilephones.copy()
print(copyofmobilephones)
del copyofmobilephones["Motto"]
print(copyofmobilephones)
copyofmobilephones.clear()
print(copyofmobilephones)
