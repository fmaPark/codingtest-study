def solution(k, dungeons):
    # 모든 순서대로 탐험을 해보고 최대 던전 수 찾기
    # print(dungeons)
    cnt_list = []

    def visit(k, n, visited, cnt):
        k -= dungeons[n][1]
        # 현 피로도, 갈 던전, 간 던전
        isVisit = False
        for i in range(len(visited)):
            now_visited = visited[:]
            if dungeons[i][0] <= k and not visited[i]: #최소 필요 피로도가 현 피로도보다 적으면
                now_visited[i] = True
                isVisit = True
                visit(k, i, now_visited, cnt+1)
        if not isVisit:
            cnt_list.append(cnt)
    
    for i in range(0, len(dungeons)):
        v = [False for _ in range(len(dungeons))]
        v[i] = True
        visit(k, i, v, 1)
    return max(cnt_list)
