#Reading a file
emp_details=open("emp.txt","r")
# print(emp_details.read()) 
# print(emp_details.readable())
# print(emp_details.readlines())
print(emp_details.readline())
emp_details.close()

#appending a file
emp_details=open("emp.txt","a")
# emp_details.write("Toby -> HR")
emp_details.close()

#writing a new file
emp_details=open("emp1.txt","w")
emp_details.write("\nNew File created")
emp_details.close()

