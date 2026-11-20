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

원인: ① 유형 인식 (경로 문제로 못 봄) + ② 구현 (경우 나열 → 분기 증가)

다음에 할 것
- "벽이 막는다 / 몇 칸 이내" 조합이 보이면 먼저 '경로 탐색(BFS, 깊이 제한)'으로 쓸 수 있는지 본다.
  P에서 BFS, X는 못 지나감, 거리 2까지만 → 그 안에서 P를 만나면 0. 경우 나열이 사라진다.
- 다른 시점: 빈칸 O 기준으로 상하좌우에 P가 2개 이상이면 위반, P 옆에 P가 붙어 있으면 위반.
- 경우 나열로 가기 전에 "이 경우들을 하나의 규칙으로 묶을 수 있나?"를 30초 자문.
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


if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
              ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
              ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
              ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
              ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    out = solution(places)
    print(out)
    assert out == [1, 0, 1, 1, 1]
