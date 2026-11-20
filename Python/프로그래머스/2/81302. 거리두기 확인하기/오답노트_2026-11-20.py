"""
[오답노트] 프로그래머스 81302 거리두기 확인하기 (Lv2, 2021 카카오 인턴십)
- 날짜: 2026-11-20
- 걸린 시간: 29분 (목표 25분 초과)
- 힌트: 0회
- 결과: 통과

막힌 지점
- 맨해튼 거리 2 이내를 "모양"으로 쪼갰다: 인접 1칸 / 직선 2칸 / 대각선, 세 경우를 손으로 나열.
- 경우마다 방향·사이 칸 인덱스(nr+1, nc-1 등)를 따로 맞추느라 코드가 길어지고 끼워맞추기가 됨.
- 칸막이 = "그 사이를 지나갈 수 없다"는 경로 개념인데, 이를 거리 공식 + 예외로만 봤다.
- 처음에 BFS를 떠올리긴 했지만 카카오 프렌즈4블록(애니팡)과 비슷해 보여서 일단 나열로 감.
- 처음 틀린 이유: 상하좌우 2칸을 처음엔 습관적으로 4방위 한 묶음으로 썼다가, 나눈 뒤
  [(-2, 0), (2, 0)]에서 사이 칸을 place[nr-1][nc] != 'X' 하나로만 검사함
  ((0, -2), (0, 2)도 같은 실수). 방향마다 사이 칸이 다른데 한 식으로 처리한 게 화근.
  그래서 dr == -2 / dr == 2 같은 불필요한 분기가 생김. (어쨌든 수습은 함)
- 디버깅: 모든 isChecked = False 바로 위에 print를 찍어 어느 구간을 지나는지 확인함.
  다음에 구현 수습할 때도 쓸 만한 방법.

원인: ① 유형 인식 (경로 문제로 못 봄) + ② 구현 (경우 나열 → 분기 증가)

다음에 할 것
- "벽이 막는다 / 몇 칸 이내" 조합이 보이면 먼저 '경로 탐색(BFS, 깊이 제한)'으로 쓸 수 있는지 본다.
  P에서 BFS, X는 못 지나감, 거리 2까지만 → 그 안에서 P를 만나면 0. 경우 나열이 사라진다.
- 다른 시점: 빈칸 O 기준으로 상하좌우에 P가 2개 이상이면 위반, P 옆에 P가 붙어 있으면 위반.
- 경우 나열로 가기 전에 "이 경우들을 하나의 규칙으로 묶을 수 있나?"를 30초 자문.
- 조건을 더 명확하게 세우면서 알고리즘을 구성할 것. 그랬다면 BFS도 알아볼 수 있었을 것.
- 나열식으로 갈 때는 방향 배열에 (목표 칸, 사이 칸)을 같이 넣어 분기를 없앤다.
"""


def solution(places):
    # 맨해튼거리: (r1, c1), (r2, c2)일 때 |r1 - r2| + |c1 - c2| => 2 초과여야 함
    # 사람이 있는 모든 칸에 대해 - 상하좌우 2칸 이내 또는 대각선에 사람이 있나 탐색
    # 상하좌우 2칸 이내일 경우 그사이에 칸막이가 있으면 ok
    # 대각선에 있을 경우 그 방향 양옆에 칸막이가 있어야 함

    ROWS = len(places)
    COLS = len(places[0])

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


# ---- 다시 푼 풀이: BFS (거리 2까지, X는 못 지나감) ----
from collections import deque


def solution_bfs(places):
    return [1 if is_safe(place) else 0 for place in places]


def is_safe(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P' and not bfs(place, r, c):
                return False
    return True


def bfs(place, sr, sc):
    q = deque([(sr, sc, 0)])
    visited = {(sr, sc)}
    while q:
        r, c, d = q.popleft()
        if d == 2:                      # 거리 2까지만 본다
            continue
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < 5 and 0 <= nc < 5) or (nr, nc) in visited:
                continue
            if place[nr][nc] == 'X':    # 칸막이는 못 지나감
                continue
            if place[nr][nc] == 'P':    # 거리 2 안에서 사람 만남
                return False
            visited.add((nr, nc))
            q.append((nr, nc, d + 1))
    return True


if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    out = solution(places)
    print(out)
    assert out == [1, 0, 1, 1, 1]
    out_bfs = solution_bfs(places)
    print(out_bfs)
    assert out_bfs == [1, 0, 1, 1, 1]
