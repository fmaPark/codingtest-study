


# bfs 활용 문제

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[1])
    
    # 이동 방향
    # dx: 행 방향, dy: 열 방향
    dx = [-1, 1, 0, 0] # 위 아래로만 움직임
    dy = [0, 0, -1, 1] # 좌우로만 움직임
    
    def bfs(x, y):
        queue = deque([(x, y)]) # 큐에 시작 좌표 추가
        while queue:
            x, y = queue.popleft() # 현재 좌표
            # 현재 위치에서 4방향 탐색
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                # 맵 범위 안에 있고, 벽이 아니며 아직 방문하지 않은 경우
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1 #이동 거리 기록
                    queue.append((nx, ny))
        
        print('maps: ', maps)
        return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1
    
    return bfs(0, 0)
