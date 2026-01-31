a = input()
b = input()
c = input()

num_str = str(int(a)*int(b)*int(c))
count_list = [0,0,0,0,0,0,0,0,0,0]

for i in range(0, len(num_str)):
    count_list[int(num_str[i])] = count_list[int(num_str[i])] + 1

for c in count_list:
    print(c)