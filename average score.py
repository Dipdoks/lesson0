grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

studentsSTR = sorted(list(students))
#print(studentsSTR) # Алфавитный порядок для наглядности

A0 = len(grades[0])
#print(str(A0)+' оценок 1-го') # Количество оценок первого ученика!
A = grades[0]
A1 = A[0]
A2 = A[1]
A3 = A[2]
A4 = A[3]
A5 = A[4]
student_A = (A1+A2+A3+A4+A5)/A0 # Средняя оценка первого ученика!
students_Name_A = studentsSTR[0]

B0 = len(grades[1])
#print(str(B0)+' оценок 2-го') # Количество оценок второго ученика!
B = grades[1]
B1 = B[0]
B2 = B[1]
B3 = B[2]
B4 = B[3]
student_B = (B1+B2+B3+B4)/B0 # Средняя оценка второго ученика!
students_Name_B = studentsSTR[1]

C0 = len(grades[2])
#print(str(C0)+' оценок 3-го') # Количество оценок третьего ученика!
С = grades[2]
С1 = С[0]
С2 = С[1]
С3 = С[2]
С4 = С[3]
student_C = (С1+С2+С3+С4)/C0 # Средняя оценка третьего ученика!
students_Name_C = studentsSTR[2]

D0 = len(grades[3])
#print(str(D0)+' оценок 4-го') # Количество оценок четвертого ученика!
D = grades[3]
D1 = D[0]
D2 = D[1]
D3 = D[2]
student_D = (D1+D2+D3)/D0 # Средняя оценка четвертого ученика!
students_Name_D = studentsSTR[3]

E0 = len(grades[4])
#print(str(E0)+' оценок 5-го') # Количество оценок пятого ученика!
E = grades[4]
E1 = E[0]
E2 = E[1]
E3 = E[2]
E4 = E[3]
E5 = E[4]
student_E = (E1+E2+E3+E4+E5)/E0 # Средняя оценка пятого ученика!
students_Name_E = studentsSTR[4]

Dictionary = {students_Name_A: student_A, students_Name_B: student_B, students_Name_C: student_C, students_Name_D: student_D, students_Name_E: student_E}
print(Dictionary)
