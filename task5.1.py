# Assignment from Module6, Task1
# Creating a Dictionary of Student Marks...

students_marks = {
    "Alice" : 85,
    "Mike"   : 92,
    "Nick"  : 90,
    "Jenny" : 86,
    "Lina"  : 98,
}

student_name = input("Enter the Student's Name: ")

if student_name in students_marks:
    print(f"{student_name}'s Marks: {students_marks[student_name]}")

else:
    print("Student not found.")