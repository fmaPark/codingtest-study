import math

def solution(progresses, speeds):
    # 각 기능이 완료되기까지 필요한 날수 계산
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    result = []
    i = 0
    
    while i < len(days):
        # 현재 기준 기능의 완료일
        deadline = days[i]
        count = 0
        
        # deadline 안에 같이 완료되는 기능 묶기
        while i < len(days) and days[i] <= deadline:
            count += 1
            i += 1
        
        result.append(count)
    
    return result