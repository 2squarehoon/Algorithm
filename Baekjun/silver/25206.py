# S5 너의 평점은
grades = 0.0
scores = 0.0
for _ in range(20):
    lecture = input().split()
    grade, score = float(lecture[1]), lecture[2]
    grades += grade
    if score == "A+":
        scores += 4.5*grade
    elif score == "A0":
        scores += 4.0 * grade
    elif score == "B+":
        scores += 3.5 * grade
    elif score == "B0":
        scores += 3.0 * grade
    elif score == "C+":
        scores += 2.5 * grade
    elif score == "C0":
        scores += 2.0 * grade
    elif score == "D+":
        scores += 1.5 * grade
    elif score == "D0":
        scores += 1.0 * grade
    elif score == "F":
        pass
    else:
        grades -= grade
print(scores/grades)