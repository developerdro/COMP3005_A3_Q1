import database
from student_function import getAllStudents, addStudent, updateStudentEmail, deleteStudent

# Prompt the user for database credentials
print("""
========================================
    Connect to Exisiting Database       
========================================
""")

database.DB_HOST = input("Enter host (default: localhost): ") or "localhost"
database.DB_PORT = input("Enter port (default: 5432): ") or "5432"
database.DB_USER = input("Enter PostgreSQL username: ")
database.DB_PASS = input("Enter PostgreSQL password: ")
database.DB_NAME = input("Enter database name: ")


# Loop continuously to display the Student Database menu until the user exits
while True:
    print("""
    ===============================
        STUDENT DATABASE MENU
    ===============================
    1. View all students
    2. Add a new student
    3. Update a student's email
    4. Delete a student
    5. Exit
    """)

    choice = input("Enter your choice (1 to 5): ")

    match choice:
        case "1":
            getAllStudents()

        case "2":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            enrollment_date = input("Enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)

        case "3":
            student_id = input("Student ID: ")
            new_email = input("New email: ")
            updateStudentEmail(student_id, new_email)

        case "4":
            student_id = input("Student ID to delete: ")
            deleteStudent(student_id)

        case "5":
            print("Exiting program...")
            break