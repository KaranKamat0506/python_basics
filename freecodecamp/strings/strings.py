
str1="Dank memer"
str2="Normie"
print(str1.upper())
print(str1.lower())
print(str1.upper().isupper())
print(str1.lower().islower())
print("Are u "+ str1+" or a "+str2+" ?")

print(len(str1))
print(str1[2])
print(str1.index("k"))
print(str1.index("meme"))

#To replace a word or character in a string
print(str1.replace("Dank","Normie"))

#Slicing 
#To print the characters within a given range
#Get the characters from position 2 to position 6 (not included):
print(str1[2:6])

#Negative Indexing
# Get the characters from position 5 to position 1 (not included), starting the count from the end of the string:
print(str1[-5:-2])

#Strip() to remove white spaces from the beginning and the end
str3=" Dank Normie "
print(str3.strip())

#Split a string
print(str1.split(":"))

# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
txt = "The rain in Spain stays mainly in the plain"
x="ain" in txt
print(x)

name=input("Enter your name:")
print(name)
