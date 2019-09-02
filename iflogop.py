marks=int(input("Enter the marks obtained by the student:"))
attendence=int(input("Enter the attendance percentage:"))
if marks>=45 and attendence>=75:
    print("The student can sit for examnation.")
elif marks>=45 and attendence<=75:
    print("Attendance should be more than 75%")
elif marks<=45 and attendence>=75:
    print("Marks should be more than 45%")
else:
    print("The student can sit for examnation.")