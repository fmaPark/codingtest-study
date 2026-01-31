t = int(input())
arr = [int(input()) for _ in range(0, t)]

result_arr = []
for i in range(0, t):
    if arr[i] == 0:
        result_arr = result_arr[:-1]
        continue
    
    result_arr.append(arr[i])

sum = 0
for result in result_arr:
    sum += result

print(sum)


