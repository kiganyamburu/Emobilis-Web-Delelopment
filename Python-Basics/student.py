class Student:
    def __init__(self, name, mark1, mark2, mark3):
        """
        Initialize a student with their name and marks for three subjects

        Parameters:
        name (str): Name of the student
        mark1 (float): Mark for first subject
        mark2 (float): Mark for second subject
        mark3 (float): Mark for third subject
        """
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calculate_average(self):
        """
        Calculate the average of the three subject marks

        Returns:
        float: Average mark rounded to 2 decimal places
        """
        return round((self.mark1 + self.mark2 + self.mark3) / 3, 2)

    def determine_grade(self):
        """
        Determine the grade based on the average mark

        Returns:
        str: Grade corresponding to the average mark
        """
        average = self.calculate_average()

        if average >= 90:
            return 'A+'
        elif average >= 80:
            return 'A'
        elif average >= 70:
            return 'B+'
        elif average >= 60:
            return 'B'
        elif average >= 50:
            return 'C'
        elif average >= 40:
            return 'D'
        else:
            return 'F'

    def get_student_info(self):
        """
        Get a summary of the student's performance

        Returns:
        str: Formatted string with student name, marks, average, and grade
        """
        return (f"Name: {self.name}\n"
                f"Marks: {self.mark1}, {self.mark2}, {self.mark3}\n"
                f"Average: {self.calculate_average()}\n"
                f"Grade: {self.determine_grade()}")


# Example usage
def main():
    # Create student objects
    student1 = Student("John Doe", 85, 92, 78)
    student2 = Student("Jane Smith", 45, 55, 60)

    # Print student information
    print(student1.get_student_info())
    print("\n")
    print(student2.get_student_info())


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()