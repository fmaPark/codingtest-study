def solution(n, words):
    answer = [0,0]
    
    # 중복 검사
    is_duplication = True if len(words) != len(set(words)) else False
    
    last_word = words[0]
    cnt = 0
    for i in range(0, len(words)):
        if i % n == 0:
            cnt += 1
        
        # 한 글자 단어를 말했을 경우
        if len(words[i]) == 1 :
            answer = [i%n+1, cnt]
            break
        
        if i != 0:
            # 앞사람이 말한 단어의 마지막 문자로 시작하지 않았을 경우
            if words[i][0] != last_word[-1]:
                answer = [i%n+1, cnt]
                break
                
            # 이전에 등장했던 단어가 등장한 경우
            if is_duplication:
                if words[i] in words[:i]:
                    answer = [i%n+1, cnt]
                    break
            
        last_word = words[i]

    return answer