import numpy as np

def load_grades(filename: str = "student_grades.csv") -> np.ndarray:
    """
    Load student grades from CSV into a NumPy array (skipping Name column).

    Returns
    -------
    np.ndarray
        2D array of grades (rows = students, columns = exams)
    """
    # Skip the Name column (column 0), load only numeric grades
    data = np.genfromtxt(filename, delimiter=',', skip_header=1, usecols=(1, 2, 3, 4, 5))
    return data


def print_basic_info(data: np.ndarray):
    """Print first few rows and shape of the dataset."""
    print("=== Dataset Overview ===")
    print(f"Shape: {data.shape} (Students x Exams)")
    print(f"First 5 rows:\n{data[:5]}\n")


def calculate_exam_statistics(data: np.ndarray):
    """Calculate and print statistics for each exam."""
    exams = ["Exam 1", "Exam 2", "Exam 3", "Exam 4", "Final"]

    print("=== Statistics by Exam ===")
    for i, exam_name in enumerate(exams):
        col = data[:, i]
        print(f"\n{exam_name}:")
        print(f"  Mean          : {np.mean(col):.2f}")
        print(f"  Median        : {np.median(col):.2f}")
        print(f"  Std Dev       : {np.std(col):.2f}")
        print(f"  Minimum       : {np.min(col):.2f}")
        print(f"  Maximum       : {np.max(col):.2f}")


def calculate_overall_statistics(data: np.ndarray):
    """Calculate overall statistics across all grades."""
    all_grades = data.flatten()

    print("\n=== Overall Statistics (All Exams Combined) ===")
    print(f"Total Grades     : {len(all_grades)}")
    print(f"Mean             : {np.mean(all_grades):.2f}")
    print(f"Median           : {np.median(all_grades):.2f}")
    print(f"Std Dev          : {np.std(all_grades):.2f}")
    print(f"Minimum          : {np.min(all_grades):.2f}")
    print(f"Maximum          : {np.max(all_grades):.2f}")


def calculate_pass_fail(data: np.ndarray):
    """Calculate pass/fail counts per exam (60+ = Pass)."""
    exams = ["Exam 1", "Exam 2", "Exam 3", "Exam 4", "Final"]
    print("\n=== Pass/Fail by Exam ===")

    total_pass = 0
    total_students = data.shape[0]

    for i, exam_name in enumerate(exams):
        col = data[:, i]
        passed = np.sum(col >= 60)
        failed = np.sum(col < 60)
        total_pass += passed
        print(f"{exam_name:8}: Passed = {passed:2} | Failed = {failed:2} | Pass Rate = {passed/total_students*100:5.1f}%")

    return total_pass, total_students * data.shape[1]   # for overall percentage


def main():
    """Main function to run the complete grade analysis."""
    print("=== Student Grades Analysis using NumPy ===\n")

    # Load data
    grades = load_grades()

    # Step 3: Show basic info
    print_basic_info(grades)

    # Step 4: Per-exam statistics
    calculate_exam_statistics(grades)

    # Step 5: Overall statistics
    calculate_overall_statistics(grades)

    # Step 6 & 7: Pass/Fail analysis
    total_passed, total_grades = calculate_pass_fail(grades)
    overall_pass_rate = (total_passed / total_grades) * 100
    print(f"\nOverall Pass Percentage (all exams): {overall_pass_rate:.1f}%")

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()