str = input('')

apb_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

p = 0
total = 0

while p < len(str):
    is_in_list = 0
    for apb in apb_list:
        if str[p:].startswith(apb):
            p = p + len(apb)
            total = total + 1
            is_in_list = 1
            break
    if (is_in_list == 0):
        p = p + 1
        total = total + 1

print(total)