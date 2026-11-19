"""
[오답노트] 프로그래머스 159993 미로 탈출 (Lv2) — 2026-11-19

- 걸린 시간: 26분 (목표 25분)
- 힌트: 1회
- 유형: 격자 BFS를 두 번 (S→L, L→E). 둘 중 하나라도 못 가면 -1

- 막힌 지점:
  nc = r + dc  ← c 자리에 r을 씀 (오타)
  첫 칸이 (0,0)이라 r == c여서 첫 턴에는 정상처럼 보였음

- 원인: ⑤ 단순 실수 (좌표 옮겨 쓰다 오타)

- 다음에 할 것:
  1. 같은 BFS를 두 번 쓰면 복붙하지 말고 bfs(start, target) 함수 하나로 묶기
     → 오타가 생겨도 한 군데에서만 남
  2. 출력이 이상하면 r != c인 칸 하나를 손으로 따라가 보기
  3. nr, nc 계산 줄은 작성 직후 한 번 소리 내어 읽기
"""

# ↓ 제출 코드
from collections import deque

def solution(maps):
    # 시작점에서 BFS를 활용해 통로가 있는 곳으로 이동
    # 시작점 - 레버(A) BFS, 레버 - 출구(B) BFS를 각각 계산하여 지나간 칸수 더하기
    # 둘중 하나라도 갈 수 없다는 결론이 나오면 -1 반환
    
    ROW = len(maps)
    COL = len(maps[0])
    
    # ==== 시작점 - 레버 ====
    visitedA = [[False] * COL for _ in range(ROW)]
    qA = deque()
    cntA = 0
    
    # 시작점 찾기
    for i in range(0, ROW):
        for j in range(0, COL):
            if maps[i][j] == 'S':
                qA.append((i, j, 0))
                visitedA[i][j] = True
    
    # BFS
    while qA:
        # row, col, 거리
        r, c, a = qA.popleft()
        
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc, na = r + dr, c + dc, a + 1
            
            if 0 <= nr < ROW and 0 <= nc < COL and maps[nr][nc] != 'X' and not visitedA[nr][nc]:
                visitedA[nr][nc] = True
                qA.append((nr, nc, na))
                
                if maps[nr][nc] == 'L':
                    cntA = na
    
    if cntA == 0:
        return -1
    
    # ==== 레버 - 출구 ====
    visitedB = [[False] * COL for _ in range(ROW)]
    qB = deque()
    cntB = 0
    
    # 시작점 찾기
    for i in range(0, ROW):
        for j in range(0, COL):
            if maps[i][j] == 'L':
                qB.append((i, j, 0))
                visitedB[i][j] = True
                
    # BFS
    while qB:
        # row, col, 거리
        r, c, b = qB.popleft()
        
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc, nb = r + dr, c + dc, b + 1
            
            if 0 <= nr < ROW and 0 <= nc < COL and maps[nr][nc] != 'X' and not visitedB[nr][nc]:
                visitedB[nr][nc] = True
                qB.append((nr, nc, nb))
                
                if maps[nr][nc] == 'E':
                    cntB = nb
    if cntB == 0:
        return -1
    
    return cntA + cntB


if __name__ == "__main__":
    tests = [
        (["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"], 16),
        (["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"], -1),
    ]
    for maps, expected in tests:
        result = solution(maps)
        print(result, expected, "OK" if result == expected else "FAIL")
