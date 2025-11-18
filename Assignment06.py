# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Mike Luke, 11/17/2025, Modified Script
# ------------------------------------------------------------------------------------------ #
import json
import io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
students: list = []  # a table of student data
menu_choice = ''

# Create Functions
# Presentation
class FileProcessor:
    # Read from File
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    # Save data to file
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):

        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages("Please check that the data is JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
            if file.closed == False:
                file.close()

class IO:
    pass

# Error exception message
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    # Input Menu for user
    @staticmethod
    def input_menu_choice(menu_choice: str):
        try:
            menu_choice = input("What would you like to do: ")
            if menu_choice not in ("1", "2", "3", "4"):
                raise Exception ("Please, Choose only 1, 2, or 3")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return menu_choice

    # Show Menu
    @staticmethod
    def output_menu(menu: str):
        print()
        print(menu)
        print()
        return menu

    # User Input
    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name}"
                  f" {student_last_name} for {course_name}.")

        except ValueError as e:
            IO.output_error_messages(
                "That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return students

    # Show list contents
    @staticmethod
    def output_student_courses(student_data:list):
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in'
                  f' {student["CourseName"]}')
        print("-" * 50)

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,
                                             student_data=students)

# Present and Process the data

while (True):
    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice(menu_choice=menu_choice)

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME,
                                         student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")