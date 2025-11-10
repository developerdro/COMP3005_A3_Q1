from database import get_db_connection

# Retrieves and displays all records from the students table
def getAllStudents():

    # Connect to an exisiting database 
    conn = get_db_connection()

    try:
        # Open a cursor to perform database operations 
        cursor = conn.cursor()

        # Execute a command: this selects all from students table 
        cursor.execute("SELECT * FROM students ORDER BY student_id;")

        # Retrieve all records from the executed query as a list of tuples
        students = cursor.fetchall()

        if not students:
            print("No students found in the database.")
            return
            
        # Display header
        print("\n{:<12} {:<15} {:<15} {:<30} {:<15}".format(
            "Student ID", "First Name", "Last Name", "Email", "Enrollment Date"
        ))

        # Display each student
        for student in students:
            print(f"{student[0]:<12} {student[1]:<15} {student[2]:<15} {student[3]:<30} {str(student[4]):<15}")
        print()

    except Exception as e:
        print(f"Error retrieving and displaying all records: {e}")

    finally: 
        # Close communication with the database
        cursor.close()
        conn.close()

# Inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):

    # Connect to an exisiting database 
    conn = get_db_connection()

    try:
        # Open a cursor to perform database operations 
        cursor = conn.cursor()

        # Execute a command: this inserts a student into the students table 
        cursor.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
             VALUES (%s, %s, %s, %s);""",
            (first_name, last_name, email, enrollment_date)
        )
        conn.commit()
    
    except Exception as e:
        print(f"Error inserting a new student record: {e}")
    
    finally:
        # Close communication with the database 
        cursor.close()
        conn.close()

# Updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    
    # Connect to an exisiting database 
    conn = get_db_connection()
    
    try:
        # Open a cursor to perform database operations 
        cursor = conn.cursor()

        # Execute a command: this updates a student's email 
        cursor.execute(
            "UPDATE students SET email = %s WHERE student_id = %s", 
            (new_email, student_id)
        )
        conn.commit()
    
    except Exception as e:
        print(f"Error updating student email: {e}")
    
    finally:
        # Close communication with the database
        cursor.close()
        conn.close()

# Deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    
    # Connect to an exisiting database 
    conn = get_db_connection()

    try:
        # Open a cursor to perform database operations 
        cursor = conn.cursor()

        # Execute a command: this deletes a student 
        cursor.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )
        conn.commit()
    
    except Exception as e:
        print(f"Error deleting student: {e}")
    
    finally:
        # Close communication with the database
        cursor.close()
        conn.close()