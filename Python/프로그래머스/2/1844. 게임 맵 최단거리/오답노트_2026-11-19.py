"""
[오답노트] 2026-11-19

문제: 1844 게임 맵 최단거리
유형: 격자 BFS
걸린 시간: (측정 안함, 힌트 2개)
막힌 지점: 아래 진짜 원인에 서술
진짜 원인:

* ① 유형 인식: BFS 큐에 카운트를 그대로 기재하면 되는 걸 DP를 떠올림. 추가 개념에 의존하지 말고 기존 개념에서 변수 각각을 이해하여 처리 방법을 떠올려야 함.
* ② 구현: maps[nr][nc] == 0 검사를 범위 검사보다 먼저 해서 IndexError가 남. 같은 시점의 분기 검사는 한번에 수행해야 함
* ④ 엣지 케이스: 끝 카운트(벽에 도달할 수 없으면 -1)는 예외처리했지만 시작이 0인 케이스를 고려하지 못함

다음에 같은 유형을 만나면: BFS 유형 자체를 손에 더 익히고 시작/끝 엣지케이스를 명확하게 구별할 것.
다시 풀 날짜:

* 아래 코드는 2026-11-19 제출 코드(게임 맵 최단거리.py) 사본.
  BaekjoonHub가 재제출 시 원본을 덮어써도 이 파일은 남는다.
  2026-10-26 첫 풀이는 게임 맵 최단거리_2026-10-26.py에 보존.
"""

from collections import deque

def solution(maps):
    
    W = len(maps)
    H = len(maps[0])
    visited = [[False] * H for _ in range(W)]
    q = deque() # 다음에 방문할 칸 대기줄
    cnt = 0
    
    if maps[0][0] == 0:
        return -1

    q.append((0, 0, 0)) # row, col, 걸음수
    visited[0][0] = True
    
    while q:
        r, c, n = q.popleft()
        
        if r == W-1 and c == H-1:
            cnt = max(n+1, cnt)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc, nn = r + dr, c + dc, n + 1
            if 0 <= nr < W and 0 <= nc < H and not visited[nr][nc] and not maps[nr][nc] == 0:
                visited[nr][nc] = True
                q.append((nr, nc, nn))
        
    if cnt == 0:
        return -1
    
    return cnt
