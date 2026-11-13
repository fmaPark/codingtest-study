"""
[오답노트] 2026-11-13

문제: 172928 공원 산책 (프로그래머스 Lv1)
유형: 구현 · 2차원 격자 이동
걸린 시간: 45분 / 힌트 4개(4번은 정답 공개, 이후 전체 코드 제공) + 문법 도움 1
막힌 지점:
 - 도착 칸만 검사하고, 지나가는 칸에 장애물이 있는지는 검사하지 않음
 - N·W처럼 값이 줄어드는 방향에서 range(now, end)가 빈 리스트가 됨(간격 -1과 끝 값 ±1 누락)
 - 경로를 만든 뒤 도착 칸 검사가 빠짐(range 끝 값 미포함)
 - w/h 이름(좌우/상하)과 start에서 꺼낸 (행, 열) 순서가 어긋남. 오류를 보고 이름을 중간에 바꾸다가 의미가 섞임

진짜 원인: ② 구현 — 좌표 변수의 의미(행=상하, 열=좌우)를 코딩 전에 고정하지 않아
          start·이동·범위 검사·반환값이 서로 다른 순서를 썼다.

다시 풀 날짜: 2026-11-20

* 아래 코드는 2026-11-13 제출 코드(공원 산책.py) 사본.
  BaekjoonHub가 재제출 시 원본을 덮어써도 이 파일은 남는다.
"""

def solution(park, routes):
    # print(park)
    # print(routes)
    
    width = len(park[0])
    height = len(park)
    
    start = [] # 시작 좌표
    obs = [] # 장애물 좌표
    
    for i in range(0, height):
        for j in range(0, width):
            if park[i][j] == 'S':
                start.append((i, j))
            if park[i][j] == 'X':
                obs.append((i, j))
    
    w = start[0][1]
    h = start[0][0]
    
    for route in routes:
        now_w = w
        now_h = h
        spaces = []
        
        dir, dis = route.split(' ')
        dis = int(dis)
        if dir == 'W':
            w -= dis
            spaces = [(h, x) for x in range(now_w, w-1, -1)]
        elif dir == 'N':
            h -= dis
            spaces = [(x, w) for x in range(now_h, h-1, -1)]
        elif dir == 'S':
            h += dis
            spaces = [(x, w) for x in range(now_h, h+1)]
        elif dir == 'E':
            w += dis
            spaces = [(h, x) for x in range(now_w, w+1)]
            
        print(spaces)
        # w,h가 최댓값보다 큼
        # 장애물이 현 좌표와 이동예정좌표 사이에 있음
        is_obs = False
        for o in obs:
            print(o)
            if o in spaces:
                is_obs = True
        if h >= height or w >= width or h < 0 or w < 0 or is_obs:
            w = now_w
            h = now_h
            
        # print(w, h)
    
    answer = [h, w]
    return answer
