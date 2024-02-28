# Grundlagen der Objektorientierten Programmierung
class Student:
    def __init__(self, name, student_id, grades=[]):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic, grades=[]):
        super().__init__(name, student_id, grades)
        self.thesis_topic = thesis_topic

    def calculate_average(self):  # Strengere Kriterien können hier implementiert werden
        return super().calculate_average()  # Beispielhaft die Basisimplementierung

def print_student_details(student):
    if isinstance(student, GraduateStudent):
        print(f"Graduate Student: {student.name}, Thesis: {student.thesis_topic}, Average Grade: {student.calculate_average()}")
    else:
        print(f"Student: {student.name}, Average Grade: {student.calculate_average()}")

student = Student('Anna', 1, [3, 4, 2])
graduate_student = GraduateStudent('Bernd', 2, 'Deep Learning', [1, 2, 1])

print_student_details(student)
print_student_details(graduate_student)
