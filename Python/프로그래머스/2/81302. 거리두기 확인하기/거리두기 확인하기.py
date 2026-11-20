def solution(places):
    # 맨해튼거리: (r1, c1), (r2, c2)일 때 |r1 - r2| + |c1 - c2| => 2 초과여야 함
    # 사람이 있는 모든 칸에 대해 - 상하좌우 2칸 이내 또는 대각선에 사람이 있나 탐색
    # 상하좌우 2칸 이내일 경우 그사이에 칸막이가 있으면 ok
    # 대각선에 있을 경우 그 방향 양옆에 칸막이가 있어야 함
    
    answer = []
    
    for place in places:
        # 고사장마다 반복
        isChecked = True # 맨해튼거리 지켰으면 True 안지켰으면 False
        for r in range(len(place)):
            for c in range(len(place[0])):
                if place[r][c] == 'P':
                    # 상하좌우 검사
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < len(place) and 0 <= nc < len(place[0]) and place[nr][nc] == 'P':
                            isChecked = False
                    # 상하좌우 2칸 검사
                    for dr, dc in [(-2, 0), (2, 0)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < len(place) and 0 <= nc < len(place[0]) and (place[nr][nc] == 'P') :
                            if dr == -2 and place[nr+1][nc] != 'X':
                                isChecked = False
                            if dr == 2 and place[nr-1][nc] != 'X':
                                isChecked = False
                            
                    for dr, dc in [(0, -2), (0, 2)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < len(place) and 0 <= nc < len(place[0]) and (place[nr][nc] == 'P') :
                            if dc == -2 and place[nr][nc+1] != 'X':
                                isChecked = False
                            if dc == 2 and place[nr][nc-1] != 'X':
                                isChecked = False
                            
                    # 대각선 검사
                    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < len(place) and 0 <= nc < len(place[0]) and (place[nr][nc] == 'P' and (place[r][nc] != 'X' or place[nr][c] != 'X')):
                            # 대각선에 사람이 있고, 그 사이 둘 중 하나라도 칸막이가 있지 않음
                            isChecked = False
        
        if isChecked:
            answer.append(1)
        else:
            answer.append(0)
                
    return answer