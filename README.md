README - COMP3005B ASSIGNMENT 3 QUESTION 1
======================================

VIDEO DEMONSTRATION:
https://youtu.be/DS6RecsVues

------------------------------------------------------------
OVERVIEW
------------------------------------------------------------
This project is a simple command-line Student Database Management System built using Python and PostgreSQL.

It allows users to:
1. View all students
2. Add a new student
3. Update a student’s email
4. Delete a student
5. Exit the program


------------------------------------------------------------
PART 1: CREATE THE DATABASE IN PGADMIN
------------------------------------------------------------

Step 1: Ensure the following are installed
------------------------------------------
- PostgreSQL and pgAdmin 

------------------------------------------------------------
Step 2: Download the SQL File
------------------------------------------------------------
1. Navigate to the provided GitHub repository link:
    https://github.com/developerdro/COMP3005_A3_Q1
2. Locate and download the file named create_and_init.sql
3. Save it in a known location, such as your Downloads or Desktop folder.

------------------------------------------------------------
Step 3: Create the "University" Database
------------------------------------------------------------
1. Launch pgAdmin.
2. In the Browser panel, right-click on "Databases".
3. Select Create > Database.
4. Name the new database "University".
5. Click Save.

------------------------------------------------------------
Step 4: Run the SQL Script
------------------------------------------------------------
1. In pgAdmin, click on the "University" database.
2. Right-click and select "Query Tool".
3. Click the "Open File" icon (the folder icon).
4. Navigate to where you saved create_and_init.sql.
5. Open it and verify the contents appear in the editor.
6. Click the green "Run" button to execute the SQL commands.

This script creates the "students" table and inserts initial records.


------------------------------------------------------------
PART 2: SET UP THE PYTHON ENVIRONMENT
------------------------------------------------------------

Step 1: Install Required Library
--------------------------------
Ensure you have Python 3.x installed. Then open your terminal or command prompt and type:

pip install psycopg2


Step 2: Download the Project Files
----------------------------------
Download the following files individually from the same GitHub repository:

- main.py ............. Handles the user interface and program menu
- database.py ......... Manages the PostgreSQL connection
- student_function.py . Contains the functions that handle CRUD operations
- create_and_init.sql . SQL script used to create and populate the database

Save these files somewhere accessible, such as your Desktop.


Step 3: Prepare Your Database Credentials
-----------------------------------------
Before running the program, have the following information ready:

Host:
Port: 
PostgreSQL Username:
PostgreSQL Password:
Database Name:


------------------------------------------------------------
PART 3: RUNNING THE PROGRAM
------------------------------------------------------------

Step 1: Open folder containing project files in Command Line
------------------------------------------
Navigate to the directory where you placed the project flies.

Example:
cd Desktop/A3


Step 2: Run the Application
----------------------------
Type the following command:

python main.py
or
py main.py

You will be asked to enter your database credentials:
- Host
- Port
- Username
- Password
- Database name

Once connected, the program menu will appear.


Step 3: Choose from the Menu Options
------------------------------------
The program displays:

===============================
    STUDENT DATABASE MENU
===============================
1. View all students
2. Add a new student
3. Update a student's email
4. Delete a student
5. Exit

Enter a number (1 to 5) to choose an option.


------------------------------------------------------------
EXAMPLES
------------------------------------------------------------

Example 1: View All Students
----------------------------
Enter your choice (1 to 5): 1

This will display all student records from the "students" table.


Example 2: Add a New Student
----------------------------
Enter your choice (1 to 5): 2
First name: Chonker
Last name: Groundhog
Email: chonker.Groundhog@example.com
Enrollment date (YYYY-MM-DD): 2025-09-01

This will insert a new student record into the database.


Example 3: Update a Student’s Email
-----------------------------------
Enter your choice (1 to 5): 3
Student ID: 3
New email: jim.beam@carleton.ca

This will update the email for the student with ID 3.


Example 4: Delete a Student
---------------------------
Enter your choice (1 to 5): 4
Student ID to delete: 5

This will permanently remove the student record with ID 5.


Example 5: Exit the Program
---------------------------
Enter your choice (1 to 5): 5
Exiting program...
