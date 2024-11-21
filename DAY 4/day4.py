x = int(input("Enter number of schools: "))
y = int(input("Enter number of students in each school: "))
z = int(input("Enter number of students who passed the exams: "))

total_students = x * y

pass_percent = (z / total_students) * 100

if (pass_percent > 50):
    print("YES")
else:
    print("NO")