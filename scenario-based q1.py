"""
Student Management System
--------------------------
Demonstrates core OOP ideas:
  - Class & Object      : Student and College are blueprints; the actual
                           Student(...) and College(...) calls create objects.
  - Encapsulation       : Each Student object bundles its own data
                           (roll_number, name, marks, grade) together.
  - Composition ("has-a"): A College object HAS a list of Student objects.
                           The college doesn't inherit from Student, it just
                           holds/manages them.
"""


class Student:
    """Represents one student's record."""

    def __init__(self, roll_number, name, marks):
        # These are called instance attributes / data members.
        # 'self' refers to THIS particular student object being created.
        self.roll_number = roll_number
        self.name = name
        self.marks = marks
        self.grade = self._calculate_grade()  # grade is derived, so we compute it here

    def _calculate_grade(self):
        """Grade is assigned purely based on marks."""
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'F'

    def display(self):
        """Prints this single student's details in a readable row."""
        print(f"{self.roll_number:<10}{self.name:<15}{self.marks:<10}{self.grade:<5}")


class College:
    """Manages a collection of Student objects."""

    def __init__(self, name):
        self.name = name
        self.students = []  # College "has-a" list of students (composition)

    def add_student(self, student):
        """Adds a Student object to the college's records."""
        self.students.append(student)

    def display_all_students(self):
        """Loops through every stored Student object and displays it."""
        print(f"\n=== {self.name} : Student Records ===")
        print(f"{'Roll No':<10}{'Name':<15}{'Marks':<10}{'Grade':<5}")
        print("-" * 40)
        for student in self.students:
            student.display()  # notice: College doesn't know HOW to display
                                # a student, it just asks the Student object
                                # to display itself. That's OOP delegation.


# ---------------- Driver code ----------------
if __name__ == "__main__":
    college = College("MIT ADT University")

    # Creating Student objects and adding them to the college
    college.add_student(Student(101, "Aarav Sharma", 95))
    college.add_student(Student(102, "Priya Nair", 82))
    college.add_student(Student(103, "Rohan Verma", 65))
    college.add_student(Student(104, "Sneha Iyer", 40))

    # Display everything at once
    college.display_all_students()
