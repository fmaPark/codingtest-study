"""
87946 피로도 (Lv2, 완전탐색) — 2026-11-20
- 시간: 35분 (목표 25분)
- 힌트 3회 + 에러 원인 지적 1회
- 막힌 지점:
  1) 모든 순서를 도는 걸 코드로 못 옮김 → 재귀 한 번 = "안 간 던전 하나 고르기", 후보는 for문으로 순회
  2) 방문 배열 복제를 for문 밖에서 해서 형제 분기끼리 공유됨 → 분기마다 복제하거나, 호출 뒤 False로 되돌리기
  3) isVisit을 루프 안에서 초기화, cnt 0부터 시작, return 0
- 원인: ② 구현 (보조 ⑤)
- 다음에 할 것: 백트래킹 틀(visited[i]=True → 재귀 → visited[i]=False)을 손으로 한 번 더 써 보기.
  시작점도 루프 안의 후보로 처리하면 첫 던전 피로도 확인을 따로 하지 않아도 됨.
"""

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



if __name__ == "__main__":
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # 3
