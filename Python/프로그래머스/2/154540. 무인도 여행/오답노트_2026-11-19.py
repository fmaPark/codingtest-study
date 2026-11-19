"""
[오답노트] 2026-11-19

문제: 154540 무인도 여행
유형: 격자 BFS · 연결 영역
걸린 시간: 1시간 30분 +a, 힌트 받으면서 풂 (힌트 8개)
막힌 지점: "이중 for + 미방문 칸에서 BFS 시작"이라는 틀을 떠올리지 못함.
진짜 원인:위 대화의 막힌 지점을 각각 매핑 - ② 구현, ② 구현, ① 유형 인식, ① 유형 인식, ② 구현, ② 구현,

  (참고: 위 매핑이 가리키는 풀이 중 막힌 지점 1~6, 힌트 세션에서 정리한 목록)
  1. maps[nr][nc]를 범위 검사 if보다 위 줄에서 읽어 IndexError (게임 맵 ①과 같은 자리)
  2. W = len(maps[0])(열 개수)로 두고 nr < W로 행과 짝지어 IndexError → ROWS·COLS로 해결
  3. (0,0)에서 BFS를 한 번만, X까지 건너게 짜서 섬 구분 불가
     ("못 건너면 도달 못 하고, 건너면 구분이 안 된다")
  4. "이중 for + 미방문 칸에서 BFS 시작" 틀을 떠올리지 못함
     (첫 코드 주석에 "모든 시작점에 대해 반복(단, 이미 갔다면 제외)"라고 써 두고도 코드로 못 옮김)
  5. 게임 맵 걸음 수처럼 d를 칸마다 들고 다녀 "경로를 따라 온 합"이 됨 → BFS 바깥 total에 모음
  6. 시작 칸 visited를 True로 안 해서 시작값이 두 번 더해짐

다음에 같은 유형을 만나면:

* BFS를 이중포문으로 돌리는 발상을 해봐야겠다. 처음이라 몰랐음...
* 주요 변수가 의미하는 바를 주석으로 명확하게 표현하고, 로직이 머릿속에 명확하게 그려지는 선에서 의사코드를 작성해두고 시작할 것
* BFS는 툭 치면 톡 하고 나오게 연습해야 함

다시 풀 날짜: 다음 코테 전

* 아래 코드는 2026-11-19 첫 통과 제출 코드 사본.
  BaekjoonHub가 재제출 시 원본을 덮어써도 이 파일은 남는다.
"""

from collections import deque

def solution(maps):
    ROWS = len(maps)
    COLS = len(maps[0])
    
    visited = [[False] * COLS for _ in range(ROWS)] # 다녀간 곳
    days = [] # 섬에 머물 수 있는 일수
    
    # 전체를 순회하며 BFS 시작점 찾기
    # 시작점별로 하나씩 이동하며 전체 합 찾아서 days에 넣기
    for sr in range(0, ROWS):
        for sc in range(0, COLS): #BFS 시작점에 대한 반복
            # 이미 갔다왔거나 X면 세지 않음
            if visited[sr][sc] or maps[sr][sc] == 'X':
                continue
            
            # 여기서부터 BFS
            q = deque() # 가야 할 곳
            q.append((sr, sc))
            total = int(maps[sr][sc])
            visited[sr][sc] = True
            
            while q:
                r, c = q.popleft()
                
                # 다음에 갈 곳 찾기
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and maps[nr][nc] != 'X' and not visited[nr][nc]:
                        total += int(maps[nr][nc])
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        
            days.append(total)
    
    if len(days) == 0:
        return [-1]
    return sorted(days)