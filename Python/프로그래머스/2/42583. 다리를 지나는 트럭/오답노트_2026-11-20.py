"""
[42583] 다리를 지나는 트럭 — 오답노트 2026-11-20

- 시간: 24분 (목표 25분)
- 힌트: 0회 / 에러 원인 짚어 줌: 0회
- 원인: ② 구현, ⑤ 단순 실수

막힌 지점
1. 대기 트럭을 앞에서 꺼내는 문법(.pop(0))이 바로 떠오르지 않아 실행해 보며 확인함. → ② 문법 숙지
   대기 트럭도 deque로 두고 popleft()를 쓰면 됨.
2. 종료 조건을 `len(truck_weights) == 0 and len(truck_weights) == 0`으로 잡음
   (같은 조건을 두 번 씀). 트럭이 다 올라가자마자 멈춤. 로그를 찍어서 찾음. → ② 구현
   "대기 트럭 없음 AND 다리 위 무게 0"이어야 함.
3. `now_weight -= n`을 `now_weight =- n`으로 씀(= -n 대입). 값이 이상해서 찾음. → ⑤ 단순 실수

다음에 할 것
- 종료 조건은 "무엇이 모두 비어야 끝나는가"를 주석에 먼저 적고 코딩한다.
- 값이 튀면 -=, += 부호 방향부터 확인한다.
- 앞에서 꺼내는 작업은 처음부터 deque + popleft()로 쓴다.

deque 문법 정리
    from collections import deque
    q = deque()            # 빈 큐
    q = deque([0] * n)     # 길이 n짜리를 0으로 채움
    q.append(x)            # 뒤에 넣기
    q.appendleft(x)        # 앞에 넣기
    q.pop()                # 뒤에서 꺼내기
    q.popleft()            # 앞에서 꺼내기  ← 큐(FIFO)는 append + popleft
    q[0], q[-1]            # 맨 앞/맨 뒤 확인
    q.rotate(1)            # 오른쪽 1칸 회전 (음수면 왼쪽)
    q.extend([4, 5])       # 뒤에 여러 개
- list.pop(0)은 O(n), deque.popleft()는 O(1).
- 스택은 list(append/pop), 큐는 deque(append/popleft).
- deque는 슬라이싱 불가, 중간 인덱싱은 느림.
"""
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


if __name__ == "__main__":
    assert solution(2, 10, [7, 4, 5, 6]) == 8
    assert solution(100, 100, [10]) == 101
    assert solution(100, 100, [10] * 10) == 110
    print("ok")
