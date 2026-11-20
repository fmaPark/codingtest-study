"""
77485 행렬 테두리 회전하기 (Lv2) — 오답노트 2026-11-20

- 걸린 시간: 45분 (목표 25분 초과)
- 힌트: 요청 힌트 1회(1-indexed → 0-indexed)
  + 에러 원인 직접 지적 6회(min 사용법, 행렬 모양, 빈 range, 리스트 참조, maps 갱신 누락, 아랫변·왼쪽 변 범위)
- 막힌 지점
  1. min(정수 하나) → TypeError. min은 iterable이나 두 개 이상의 값을 받는다.
  2. 행렬을 columns x rows로 만듦. rows는 '행 개수', 한 행 길이는 columns. 정사각형 예제에선 안 드러남.
  3. 쿼리 1-indexed를 그대로 인덱스로 씀 → 처음에 r1,c1,r2,c2에서 1씩 빼기.
  4. range(큰 수, 작은 수) → 한 번도 안 돈다. 역순은 step -1.
  5. new_maps = maps는 복사가 아니라 같은 리스트 참조. 2차원은 [row[:] for row in maps].
  6. 아랫변·왼쪽 변 범위가 한 칸씩 밀림 → 모서리 칸 누락 + 테두리 밖(-1 = 맨 끝) 덮어쓰기.
- 원인: ② 구현(주) + ⑤ 단순 실수(행/열 의미, 0-index)
- 다음에 할 것
  - 변수 이름을 a,b,c,d 대신 r1,c1,r2,c2로 받는다.
  - 예제 쿼리 하나의 네 꼭짓점을 0-indexed 숫자로 적고, 반복문마다 "첫 i / 끝 i / 읽는 칸 / 쓰는 칸"을 주석으로 대 본다.
  - 첫 쿼리 처리 후 행렬을 print해서 문제 그림과 비교한다. 직사각형 예제를 꼭 돌린다.
"""


def solution(rows, columns, queries):
    answer = []

    maps = []
    for i in range(1, rows+1):
        map = []
        for j in range(1, columns+1):
            map.append(columns*(i-1)+j)
        maps.append(map)

    for query in queries:
        new_maps = [row[:] for row in maps]
        a, b, c, d = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        min_num = rows*columns+1
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


if __name__ == "__main__":
    assert solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]) == [8, 10, 25]
    assert solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]) == [1, 1, 5, 3]
    assert solution(100, 97, [[1,1,100,97]]) == [1]
    print("ok")
