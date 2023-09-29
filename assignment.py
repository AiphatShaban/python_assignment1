print("Enter student details")
student_details ={}
size = int(input("Enter the size of the dictionary:"))
for i in range(size):
    name = str(input("Enter the student's name: "))
    registration_number = str(input("Enter the student's registration number: "))
    age = int(input("enter the student's age: "))
    program =str(input("Enter the student's program: "))
    year_of_study = int(input("Enter the student's year of study: "))
    subjects = {}
    for i in range(1):
        subject1 = str(input("enter the first subject:"))
        subject2 = str(input("Enter the second subject: "))
        subject3 = str(input("Enter the third subject:"))
        subjects['subject1'] = subject1
        subjects['subject2'] = subject2
        subjects['subject3'] = subject3
    scores = {} 
    for i in range(1):
        marks1 = int(input("Enter the marks for subject1:"))
        marks2 = int(input("Enter the marks for subject2:"))   
        marks3 = int(input("Enter the marks for subject3:"))   
        scores['marks1'] = marks1
        scores['marks2'] = marks2
        scores['marks3'] = marks3
    grades = {}
    for i in range(1):
        grade1 = str(input("enter the grade for subject1:"))
        grade2 = str(input("Enter the grade  for subject2: "))
        grade3 = str(input("Enter the grade for subject3:"))
        grades['grade1'] = grade1
        grades['grade2'] = grade2
        grades['grade3'] = grade3
        student_details[registration_number] = {
            ' name': name,
            'age': age,
            'program': program,
            'subjects' : subjects,
            'scores': scores,
            'grade':grades,
        }
# Initialize variables to store the highest and lowest grades and corresponding student names
highest_grade = str('-inf')  # Initialize as negative infinity
lowest_grade = str('inf')    # Initialize as positive infinity
student_with_highest_grade = None
student_with_lowest_grade = None

# Iterate through the dictionary to find the highest and lowest grades
for student, grade in grades.items():
    if grade > highest_grade:
        highest_grade = grade
        student_with_highest_grade = student
    if grade < lowest_grade:
        lowest_grade = grade
        student_with_lowest_grade = student

# Print the results
print(f"Student with the highest grade: {student_with_highest_grade} (Grade: {highest_grade})")
print(f"Student with the lowest grade: {student_with_lowest_grade} (Grade: {lowest_grade})")








    