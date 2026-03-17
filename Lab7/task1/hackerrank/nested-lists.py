students = []
lowest_score = float('inf')
second_lowest = float('inf')

for _ in range(int(input())):
    name = input()
    score = float(input())
    if score < lowest_score:
        lowest_score = score
    students.append([name, score])

for i in students:
    if i[1] == lowest_score:
        continue
    else:
        if i[1] < second_lowest:
            second_lowest = i[1]

print("\n".join([i[0] for i in students if i[1] == second_lowest]))