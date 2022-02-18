# Variável = {nova_chave:novo_valor for item in lista if teste}
# Variável = {nova_chave:novo_valor for (chave, valor) in dict.items() if teste}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

# passed_students = {student: students_scores[student] for student in students_scores if students_scores[student] >= 60}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
