# Ques - 1
marks = int(input("Enter the marks obtained in the exam: "))
if(marks >= 90):
    print("Grade: A")
elif(marks >= 80):
    print("Grade: B")
elif(marks >= 70):
    print("Grade: C")
elif(marks >= 60):
    print("Grade: D")
else:
    print("Grade: F")

# Ques - 2
dict = {}
print("Enter the key-value pairs (type 'done' to finish):")
while True:
    entry = input("Enter key and value separated by space: ")
    if entry.lower() == 'done':
        break
    try:
        key, value = entry.split()
        dict[key] = value
    except ValueError:
        print("Invalid input. Please enter a key and a value separated by space.")  

print("Do you want to modify grade for student? (yes/no)")
if(input().lower() == 'yes'):
    student_name = input("Enter the student's name: ")
    if student_name in dict:
        new_grade = input("Enter the new grade: ")
        dict[student_name] = new_grade
    else:
        print("Student not found.")

print("Updated dictionary:", dict)

# Ques - 3
text = input("Enter the text you want to write: ")
with open('textfile.txt', 'w') as file:
    file.write(text)

# Ques - 4
with open('textfile.txt', 'r') as file:
    print("Here is text from the file:")
    content = file.read()
    print(content)
