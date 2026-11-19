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
            # print('---')
            lst = ['X'] * (m-len(lst)) + lst
            # print(lst)
            for i in range(0, m):
                new_board[i][c] = lst[i]
        
        board = new_board

    return cnt


# TTTANT
# RRFACC
# RRRFCC
# TRRRAA
# TTMMMF
# TMMTTJ


# TTTANT
# XXFAXX
# XXXFXX
# TXXRAA
# TTMMMF
# TMMTTJ


# CCBDE
# AADDE
# AADDF
# CCBBF

# CCBDE
# XXXXE
# XXXXF
# CCBBF

# -> 8

# XXXXE
# XXXXE
# CCBDF
# CCBBF

# XXXXE
# XXXXE
# XXBDF
# XXBBF

# -> 12