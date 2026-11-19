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
        print("방문: ", r, c, n)
        
        if r == W-1 and c == H-1:
            cnt = max(n+1, cnt)
            print(cnt)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc, nn = r + dr, c + dc, n + 1
            if 0 <= nr < W and 0 <= nc < H and not visited[nr][nc] and not maps[nr][nc] == 0:
                # print("다음 방문:", nr, nc)
                visited[nr][nc] = True
                q.append((nr, nc, nn))
        
    if cnt == 0:
        return -1
    
    return cnt