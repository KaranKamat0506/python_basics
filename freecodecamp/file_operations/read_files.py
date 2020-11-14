emp_details=open("employee.txt","r")
# print(emp_details.read())
# print(emp_details.readline())
# print(emp_details.readlines())
# print(emp_details.readable())
for employee in emp_details.readlines():
    print(employee)

emp_details.close()