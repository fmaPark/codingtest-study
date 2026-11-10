"""
[오답노트] 2026-11-10

문제: 42842 카펫 (프로그래머스 Lv2)
유형: 완전탐색
걸린 시간: 25분 (한 번 막혀 힌트를 받고 통과, 통과 후 코드를 다듬음)
막힌 지점: if문 조건을 빠뜨림

진짜 원인
- 갈색 = 가로x세로-노란색 조건은 세우고 시작했으나 노란색 = (w-2)*(h-2) 조건을 빠뜨려
  탐색 시 답을 찾지 못하고 조기 종료되는 케이스가 많았음
- 조건 범위를 잘못 설정해 불필요한 이중포문
    # for i in range(0, brown):
    #     for j in range(0, i+1):
    #         if i*j == brown+yellow and yellow == (i-2)*(j-2):
    #             w = i
    #             h = j
    #             break
- 정수 나눗셈 연산자(//)를 몰라서 소수로 나누어 오차 발생 (답에는 영향 주지 않았지만, 운이 좋았던 케이스)
- 세로가 가로보다 적으므로 세로를 기준으로 반복문을 돌리면 continue조건이 하나 줄고 연산도 빠름.

다시 풀 날짜: 1주 뒤(11.17)

* 아래 solution은 최종 제출 코드(카펫.py, 2026-11-10 10:03) 사본.
  solution_first는 처음 통과한 코드(09:38) — 다듬기 전과 비교용.
  BaekjoonHub가 재제출 시 원본을 덮어써도 이 파일은 남는다.
"""

def solution(brown, yellow):
    # 갈색 = 가로x세로-노란색
    # w x h = b + y
    # y = (w-2)*(h-2)
    for w in range(1, brown+1):
        if (brown+yellow) % w != 0:
            continue
        h = (brown+yellow)//w
        if h > w:
            continue
        if yellow == (w-2)*(h-2):
            return [w, h]
    


# ---- 처음 통과한 코드 (2026-11-10 09:38) ----
def solution_first(brown, yellow):
    # 갈색 = 가로x세로-노란색
    # w x h = b + y
    # 노란색 = (w-2)*(h-2)
    w = brown
    h = 1
    # for i in range(0, brown):
    #     for j in range(0, i+1):
    #         if i*j == brown+yellow and yellow == (i-2)*(j-2):
    #             w = i
    #             h = j
    #             break
    for w in range(1, brown+1):
        h = (brown+yellow)/w
        if h > w:
            continue
        if w*h == brown+yellow and yellow == (w-2)*(h-2):
            break
    return [w, h]
