# Store Student Marks Using Python Dictionary

# Create a dictionary
student_marks = {"Alice": 85, "Bob": 90,"Charlie": 78}

# Print the dictionary
print("Student Marks:", student_marks)  
#Output: Student Marks: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# Access marks of a student
print("Marks of Bob:", student_marks["Bob"])  
#Output: Marks of Bob: 90

# Update marks
student_marks["Alice"] = 88

# Add a new student
student_marks["David"] = 92

# Delete a student
del student_marks["Charlie"]

print("\nAfter deleting Charlie:")
print(student_marks)                
#Output: {'Alice': 88, 'Bob': 90, 'David': 92}

# Display all students and their marks
print("\nAll Students and Marks:")
for student, marks in student_marks.items():
    print(student, ":", marks)
