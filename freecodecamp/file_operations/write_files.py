#Appending a line to a file
#To append a line to a file use "a" mode
emp_details=open("employee.txt","a") 
# emp_details.write("Toby -> HR") 
emp_details.write("\nKelly -> Customer Service") #writes on new line
emp_details.close()

#Overwrite a file
# To overwrite a file use "w" mode 
#emp_details=open("employee.txt","w")
emp_details=open("employee1.txt","w") #creates a new file 
emp_details.write("\nFile contents have been overwritten completely")
emp_details.close()