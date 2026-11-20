from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 1초마다
    # 이미 올라와있는 트럭들은 한 칸씩 이동
    # 마지막 칸에 있다면 나가기
    # 다음 트럭이 다리의 남은 weight보다 작다면 다리에 올리기
    
    q = deque() # 다리
    now_weight = 0 # 다리 현재 무게
    t = 0 # 시간
    
    while True : 
        # 트럭도 다 출발했고 다리에도 아무것도 없으면 멈추기
        if len(truck_weights) == 0 and now_weight == 0:
            break
        
        t += 1
        
        
        # 마지막 칸에 있다면 나가기
        if len(q) == bridge_length:
            n = q.popleft()
            now_weight -= n
        
        # 트럭 넣을 수 있으면 넣기
        if len(truck_weights) != 0 and truck_weights[0] <= (weight - now_weight):
            q.append(truck_weights[0])
            now_weight += truck_weights[0]
            truck_weights.pop(0)
        
        # 트럭 못 넣으면 0 넣기
        else:
            q.append(0)
        
    return t