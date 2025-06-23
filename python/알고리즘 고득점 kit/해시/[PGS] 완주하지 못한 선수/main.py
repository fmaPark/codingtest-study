def solution(participant, completion):
    participant.sort()
    completion.sort()

    
    for i in range(0, len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[-1]

# 다른 풀이 : hash 함수 사용
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        print('hash(part): ', hash(part))
        temp += hash(part)
    for com in completion:
        temp -= hash(com)
        
    answer = dic[temp]
    return answer

# 다른 풀이 : counter 사용
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    
    return list(answer.keys())[0]
    


# Learned
# 반복문 횟수를 줄이는 게 핵심인 듯함
# - 처음에 completion 돌면서 participant remove하려는 시도는 시간 초과로 실패

# hash 함수 새로 알게 됨

# list.sort() 사용법 :
# example_list = [1, 2, 3, 4]
# sorted_list = example_list.sort() 가 아니라
# example_list.sort() 로 쓰고 추구 example_list를 그대로 사용