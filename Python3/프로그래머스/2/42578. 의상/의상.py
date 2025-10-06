def solution(clothes):
    clothes_dict = {}
    
    for c in clothes:
        if c[1] in clothes_dict:
            clothes_dict[c[1]] = clothes_dict[c[1]] + [c[0]]
        else:
            clothes_dict[c[1]] = [c[0]]
    
    answer = 1
    
    for clothes in clothes_dict.values():
        # 각 의상 수 + 안 입는 경우
        answer *= (len(clothes) + 1) 
    
    return answer - 1