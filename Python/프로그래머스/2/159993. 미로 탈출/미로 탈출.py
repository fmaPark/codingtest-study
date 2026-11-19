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