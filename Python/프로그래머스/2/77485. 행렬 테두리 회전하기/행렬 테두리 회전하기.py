def solution(rows, columns, queries):
    # 시뮬레이션, 빡구현...
    # queries만큼 반복하면서 테두리 회전시킨걸로 덮어씌우기
    # 한번 반복할때마다 가장 작은 숫자 배열에 담기
    
    answer = [] # 위치가 바뀐 숫자들 중 가장 작은 숫자들
    
    # 첫 행렬 만들기
    maps = []
    for i in range(1, rows+1):
        map = []
        for j in range(1, columns+1):
            map.append(columns*(i-1)+j)
        maps.append(map)
    
    # 테두리 회전시키기
    for query in queries:
        new_maps = [row[:] for row in maps]
        a, b, c, d = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        min_num = rows*columns+1
        # query를 (a, b, c, d)라고 할 때
        # (a,b) (a,d)
        # (c,b) (c,d)
        # map[a][b]~map[a][d-1] -> 오른쪽으로 한칸
        # map[a][d]~map[c-1][d] -> 아래로 한칸
        # map[c][d]~map[c][b+1] -> 왼쪽으로 한칸
        # map[c][b]~map[a+1][b] -> 위로 한칸
        for i in range(b, d):
            new_maps[a][i+1] = maps[a][i]
            min_num = min(min_num, maps[a][i])
        for i in range(a, c):
            new_maps[i+1][d] = maps[i][d]
            min_num = min(min_num, maps[i][d])
        for i in range(b+1, d+1):
            new_maps[c][i-1] = maps[c][i]
            min_num = min(min_num, maps[c][i])
        for i in range(a+1, c+1):
            new_maps[i-1][b] = maps[i][b]
            min_num = min(min_num, maps[i][b])
        answer.append(min_num)
        maps = new_maps
    
    return answer