def solution(s):
    answer = ''
    num_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    i = 0
    while i < len(s):
        if (s[i].isdigit()):
            answer += s[i]
            i += 1
        else:
            for j in range(0, len(num_list)):
                if s[i:].startswith(num_list[j]):
                    answer += str(j)
                    i += len(num_list[j])
                    continue
    return int(answer)