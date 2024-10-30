def calculate_grade(score):
    """
    Calculate letter grade based on numerical score.

    Args:
        score (float): Numerical score between 0 and 100

    Returns:
        str: Letter grade and any additional remarks
    """
    if not isinstance(score, (int, float)):
        return "Error: Please enter a valid number"

    if score < 0 or score > 100:
        return "Error: Score must be between 0 and 100"

    if score >= 90:
        grade = 'A'
        remark = "Excellent!"
    elif score >= 80:
        grade = 'B'
        remark = "Good job!"
    elif score >= 70:
        grade = 'C'
        remark = "Satisfactory"
    elif score >= 60:
        grade = 'D'
        remark = "Needs improvement"
    else:
        grade = 'F'
        remark = "Failed - please seek help"

    return f"Grade: {grade} ({score}%) - {remark}"


def process_student_grades(students_data):
    """
    Process grades for multiple students.

    Args:
        students_data (dict): Dictionary with student names and their scores

    Returns:
        dict: Dictionary with student names and their grade information
    """
    results = {}
    class_total = 0

    for student, score in students_data.items():
        results[student] = calculate_grade(score)
        class_total += score

    # Calculate class average
    class_average = class_total / len(students_data)
    results['Class Average'] = f"{class_average:.2f}%"

    return results


# Example usage:
students = {
    "John Smith": 92,
    "Emma Johnson": 85,
    "Michael Brown": 78,
    "Sarah Davis": 95,
    "David Wilson": 65
}

# Process individual grade
individual_grade = calculate_grade(88)
print("Individual grade:", individual_grade)

# Process multiple students
class_results = process_student_grades(students)
print("\nClass Results:")
for student, result in class_results.items():
    print(f"{student}: {result}")