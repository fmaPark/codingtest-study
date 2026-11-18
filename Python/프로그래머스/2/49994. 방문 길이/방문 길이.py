def solution(dirs):
    seen = set()
    # 상 하 / 좌 우
    delta = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}
    r, c = 0, 0 # 캐릭터 위치
    cnt = 0 # 처음 걸어본 길
    
    for d in dirs:
        nr, nc = r, c # 현 위치 저장
        dr, dc = delta[d] # 방향
        
        r += dr
        c += dc
        
        # 격자를 벗어날 경우 이동하지 않음
        if not (-5 <= r <=5 and -5 <= c <= 5):
            r, c = nr, nc
            continue
        
        # 이미 간 곳일 경우 카운트하지 않음
        if not (((nr, nc), (r, c)) in seen or ((r, c), (nr, nc)) in seen):
            cnt +=1
            seen.add(((nr, nc), (r, c)))
            
    return cnt