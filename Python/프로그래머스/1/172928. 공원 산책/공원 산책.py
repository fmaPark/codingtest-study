def solution(park, routes):
    H, W = len(park), len(park[0])
    # 방향 = (행 변화, 열 변화)
    delta = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    for r in range(H):
        for c in range(W):
            if park[r][c] == 'S':
                sr, sc = r, c
                
    r, c = sr, sc
    for route in routes:
        d, n = route.split() # 방향, 칸 수
        dr, dc = delta[d] # 행 변화, 열 변화
        
        nr, nc = r, c # 현재 칸
        ok = True
        for _ in range(int(n)):
            nr += dr
            nc += dc
            if not (0 <= nr < H and 0 <= nc < W) or park[nr][nc] == 'X':
                ok = False
                break
        if ok:
            r, c = nr, nc
        
    return [r, c]