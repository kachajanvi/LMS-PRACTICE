#student data organizer
students = []

def add_student():
    print("\n=== Add Student ===")

    Student_id = input("Student ID")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")

    student = {
        "ID": Student_id,
        "Name": name,
        "age": age,
        "Grade": grade

    }

    students.append(student)
    print("Student Added Successfully!")

def show_syudents():
    print("\n=== student records ===")

    if len(students) == 0:
        print("No student record found.")
    else:
        for student in students:
            print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Grade:", student["Grade"])
while True:
    print("\n==== Student Data Organizer ====")
    print("1. Add Student")
    print("2. show Student")
    print("3. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("program closed.")
        break
    else:
        print("Invalid choice!")

        
    

