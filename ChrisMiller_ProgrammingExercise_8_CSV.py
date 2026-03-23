import csv


def get_student_data():
    """
    Prompts the instructor to enter student data including first name, last name, and three exam grades.

    Returns:
        list: A list of dictionaries where each dictionary contains a student's information.
    """
    students = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        print(f"\nEntering data for student {i + 1}:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        exam1 = int(input("Exam 1 grade: "))
        exam2 = int(input("Exam 2 grade: "))
        exam3 = int(input("Exam 3 grade: "))

        student = {
            "First Name": first_name,
            "Last Name": last_name,
            "Exam 1": exam1,
            "Exam 2": exam2,
            "Exam 3": exam3
        }
        students.append(student)

    return students


def write_grades_to_csv(filename, student_list):
    """
    Writes the student data to a CSV file with headers.

    Parameters:
        filename (str): Name of the CSV file to write.
        student_list (list): List of student dictionaries to write to the file.

    Returns:
        None
    """
    with open(filename, mode='w', newline='') as file:
        fieldnames = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for student in student_list:
            writer.writerow(student)
    print(f"\nData successfully written to {filename}!")


def main():
    """
    Main function to execute the student grades input and writing process.
    """
    students = get_student_data()
    write_grades_to_csv("grades.csv", students)


if __name__ == "__main__":
    main()