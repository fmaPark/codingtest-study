"""
[오답노트] 2026-11-20

문제: 17679 [1차] 프렌즈4블록
유형: 격자 시뮬레이션 (2×2 판정 → 일괄 삭제 → 열 단위 낙하 반복)
걸린 시간: 36분 (목표 25분 초과), 힌트 4개
막힌 지점:
  1. 2×2 블록을 어떻게 잡을지 감이 안 옴 → 왼쪽 위 칸 (i, j) 하나로 대표, 범위 range(m-1)·range(n-1)
  2. board가 문자열 리스트라 board[i][j] = ... 할당 오류 → [list(row) for row in board]로 변환
  3. 블록 내리기 방법 → 열마다 빈칸이 아닌 것만 모아 아래에 두고, 위는 빈칸으로 채움
  4. 찾으면서 바로 'X'로 바꾸고 cnt += 4 → 겹친 2×2를 놓치고 겹친 칸을 중복 셈
     → set에 좌표를 모은 뒤 한꺼번에 지우고 len(set)만큼 셈
  5. new_board를 만들어 놓고 board = new_board를 빠뜨려 다음 반복이 옛 보드를 검사
원인: 1 ② 구현, 2 ⑤ 단순 실수(자료형), 3 ② 구현, 4 ② 구현, 5 ⑤ 단순 실수

다음에 같은 유형을 만나면:
* 시뮬레이션은 코딩 전에 "한 라운드 = 표시 → 삭제 → 낙하" 순서를 주석으로 먼저 적는다
* 지울 칸은 set에 모았다가 한꺼번에 지운다 (겹침·중복 카운트 동시 해결)
* 격자를 고칠 거면 시작하자마자 list(row)로 바꾼다
* 새 배열을 만들었으면 원래 변수에 다시 넣었는지 확인한다

다시 풀 날짜: 다음 코테 전

* 아래 코드는 2026-11-20 첫 통과 제출 코드 사본.
  BaekjoonHub가 재제출 시 원본을 덮어써도 이 파일은 남는다.
"""

def solution(m, n, board):
    board = [list(row) for row in board]
    cnt = 0
    
    while True:
        # 왼쪽 위를 기준으로 같은지 검증
        is_del = False
        changes = set()
        for i in range(0, m-1):
            for j in range(0, n-1):
                # 빈칸이면 건너뛰기
                if board[i][j] == 'X':
                    continue
                # 네 칸이 같은지 검증
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    changes.add((i, j))
                    changes.add((i+1, j))
                    changes.add((i, j+1))
                    changes.add((i+1, j+1))
                    is_del = True
                    
        for i, j in changes:
            board[i][j] = 'X'
        cnt += len(changes)
        
        if not is_del:
            break
            
        # 열에서 빈칸이 아닌것만 골라내기
        new_board = [[0] * n for _ in range(m)]
        for c in range(0, n):
            lst = []
            for r in range(0, m):
                if board[r][c] != 'X':
                    lst.append(board[r][c])
            lst = ['X'] * (m-len(lst)) + lst
            for i in range(0, m):
                new_board[i][c] = lst[i]
        
        board = new_board

    return cnt


if __name__ == "__main__":
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))  # 15
