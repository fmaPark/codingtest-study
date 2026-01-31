t = int(input())
students = input().split()

line = []
for i in range(0, t):
    pos = int(students[i])
    if (pos == 0):
        line.append(i+1)
    else:
        line.insert(-pos, i+1)

print(*line)