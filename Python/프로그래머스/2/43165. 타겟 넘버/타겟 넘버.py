def solution(numbers, target):
    # numbers에 대한 모든 +, - 경우의 수 탐색
    # target number랑 같으면 카운트
    
    q = []
    
    def f(i, nc, a, cnt):
        nc = nc + numbers[i]*a
        if i == len(numbers)-1:
            if nc == target:
                q.append(nc)
            return
        # 지금이 몇번째인지, 현재 숫자, -1인지 +1인지, 현재 카운트
        
        f(i+1, nc, 1, cnt)
        f(i+1, nc, -1, cnt)
        
        return 0
        
    f(0, 0, 1, 0)
    f(0, 0, -1, 0)
    
    return len(q)
