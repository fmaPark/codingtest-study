from collections import deque

def solution(maps):
    ROWS = len(maps)
    COLS = len(maps[0])
    
    visited = [[False] * COLS for _ in range(ROWS)] # 다녀간 곳
    days = [] # 섬에 머물 수 있는 일수
    
    # 전체를 순회하며 BFS 시작점 찾기
    # 시작점별로 하나씩 이동하며 전체 합 찾아서 days에 넣기
    for sr in range(0, ROWS):
        for sc in range(0, COLS): #BFS 시작점에 대한 반복
            # 이미 갔다왔거나 X면 세지 않음
            if visited[sr][sc] or maps[sr][sc] == 'X':
                continue
            
            # 여기서부터 BFS
            q = deque() # 가야 할 곳
            q.append((sr, sc))
            total = int(maps[sr][sc])
            visited[sr][sc] = True
            
            while q:
                r, c = q.popleft()
                
                # 다음에 갈 곳 찾기
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and maps[nr][nc] != 'X' and not visited[nr][nc]:
                        total += int(maps[nr][nc])
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        
            days.append(total)
    
    if len(days) == 0:
        return [-1]
    return sorted(days)