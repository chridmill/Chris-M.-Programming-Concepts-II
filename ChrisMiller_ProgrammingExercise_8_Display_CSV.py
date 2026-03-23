import csv


def read_grades_from_csv(filename):
    """
    Reads student data from a CSV file.

    Parameters:
        filename (str): The CSV file to read from.

    Returns:
        list: List of dictionaries containing student data.
    """
    students = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students


def display_student_data(student_list):
    """
    Displays student data in a tabular format.

    Parameters:
        student_list (list): List of dictionaries containing student data.

    Returns:
        None
    """
    print("\nStudent Grades Table:")
    print(f"{'First Name':<15}{'Last Name':<15}{'Exam 1':<10}{'Exam 2':<10}{'Exam 3':<10}")
    print("-" * 60)

    for student in student_list:
        print(
            f"{student['First Name']:<15}{student['Last Name']:<15}{student['Exam 1']:<10}{student['Exam 2']:<10}{student['Exam 3']:<10}")


def main():
    """
    Main function to read grades from CSV and display them.
    """
    students = read_grades_from_csv("grades.csv")
    display_student_data(students)


if __name__ == "__main__":
    main()