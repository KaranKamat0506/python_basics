emp_details=open("employee.txt","r")
# print(emp_details.read()) #Reads the contents of whole file
# print(emp_details.readline()) #Reads the first line
#print(emp_details.readable()) #returns a bollean value if file is readable or not
print(emp_details.readlines()) #returns a list of values

emp_details.close()
