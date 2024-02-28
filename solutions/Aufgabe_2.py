# Komplexe Listenmanipulation und Funktionen
students = [
    {'name': 'Tatjana', 'student_id': 1, 'grades': [2, 1, 2]},
    {'name': 'Johnny', 'student_id': 2, 'grades': [1, 2, 1]}
]

def calculate_average_grades(students_list):
    student_averages = []
    for student in students_list:
        avg_grade = sum(student['grades']) / len(student['grades'])
        student_averages.append({'name': student['name'], 'student_id': student['student_id'], 'average_grade': avg_grade})
    return sorted(student_averages, key=lambda x: x['average_grade'], reverse=True)

print(calculate_average_grades(students))