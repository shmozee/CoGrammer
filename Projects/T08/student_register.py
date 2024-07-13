
# Task 8 - Practical Task 2

no_of_students = int(input("Number of students: "))

# Get student ids
student_ids = []
for i in range(no_of_students):
    student_id = input(f"Enter student ID of student {i+1}: ")
    student_ids.append(student_id)
       
# Write the file
with open('reg_form.txt', 'w+') as file:
    file.write("\n\nStudent Register")
    file.write("\n=======================")
    for i in range(0, len(student_ids)):
        file.write("\nStudent ID: " + student_ids[i]) 
        file.write("\n........................")
        
# Read the file
with open("reg_form.txt", 'r') as file:
    print(file.read())
