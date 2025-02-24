# List to hold student records
students = []

# Function to display the menu
def display_menu():
    print("\nStudent Record Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

# Function to add a student
def add_student():
    name = input("Enter student's name: ")
    roll_no = input("Enter student's roll number: ")
    age = input("Enter student's age: ")
    
    # Add student to the list (as a dictionary)
    students.append({
        'name': name,
        'roll_no': roll_no,
        'age': age
    })
    print(f"Student {name} added successfully.")

# Function to view all students
def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records:")
        for student in students:
            print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Age: {student['age']}")

# Function to search for a student by name
def search_student():
    name = input("Enter the name of the student to search: ")
    found = False
    for student in students:
        if student['name'].lower() == name.lower():
            print(f"Found Student - Name: {student['name']}, Roll No: {student['roll_no']}, Age: {student['age']}")
            found = True
            break
    if not found:
        print("Student not found.")

# Function to update student details
def update_student():
    roll_no = input("Enter the roll number of the student to update: ")
    found = False
    for student in students:
        if student['roll_no'] == roll_no:
            new_name = input(f"Enter new name for {student['name']} (Leave blank to keep the current name): ")
            new_age = input(f"Enter new age for {student['age']} (Leave blank to keep the current age): ")
            
            if new_name:
                student['name'] = new_name
            if new_age:
                student['age'] = new_age
                
            print(f"Student {roll_no}'s record updated successfully.")
            found = True
            break
    if not found:
        print("Student not found.")

# Function to delete a student record
def delete_student():
    roll_no = input("Enter the roll number of the student to delete: ")
    global students
    students = [student for student in students if student['roll_no'] != roll_no]
    print(f"Student with roll number {roll_no} deleted successfully.")

# Main program loop
def student_record_system():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
student_record_system()
