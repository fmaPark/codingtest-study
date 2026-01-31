t = input()
lines = [list(map(int, input().split())) for _ in range(0, int(t))]

paper = [[0]*100 for _ in range(100)]

for line in lines:
    for i in range(0, 10):
        for j in range(0, 10):
            paper[line[0]+i][line[1]+j] = 1

sum = 0
for i in range(0, 100):
    for j in range(0, 100):
        if paper[i][j] == 1:
            sum = sum + 1

print(sum)