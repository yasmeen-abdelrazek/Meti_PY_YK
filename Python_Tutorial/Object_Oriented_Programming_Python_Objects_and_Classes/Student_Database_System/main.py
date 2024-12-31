class Student:
    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        avg_grade = self.calculate_average()
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {avg_grade:.2f}")

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grades=None):
        new_student = Student(name, age, grades)
        self.students.append(new_student)

    def display_all_students(self):
        if not self.students:
            print("No students in the database.")
            return
        for student in self.students:
            student.display_info()
            print("-" * 40)


# Create new database
db = StudentDatabase()

# Add new students
db.add_student("Alice", 20, [90, 85, 88])
db.add_student("Bob", 22, [70, 75, 80, 72])

# Add grade for an existing student
db.students[0].add_grade(92)

# Display information about all students in the database
db.display_all_students()
