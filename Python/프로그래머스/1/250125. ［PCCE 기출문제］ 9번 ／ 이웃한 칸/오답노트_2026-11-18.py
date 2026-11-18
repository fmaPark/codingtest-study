"""
[오답노트] 2026-11-18

문제: 250125 이웃한 칸 (프로그래머스 Lv1)
유형: 격자 델타
걸린 시간: 17분
막힌 지점: 일부 구간이 카운트가 안됨
진짜 원인: ② 구현 - 인덱스 0~3 방향 반복을 range(0,4)로 써야되는데 range(0, 3)으로 써서 한 방향이 탐지가 안됨. 내부에서 print 찍어보고 개수 세서 고침
다음에 같은 유형을 만나면: dr dc 패턴을 써서 반복. 확실하게 기억하기
다시 풀 날짜: 이건 의사코드가 다 있어서 괜찮을 것 같고 격자 델타 다른 문제를 풀어보고 싶음

* 아래 solution은 제출 코드(［PCCE 기출문제］ 9번 ／ 이웃한 칸.py, 2026-11-18 11:32) 사본.
  BaekjoonHub가 재제출 시 원본을 덮어써도 이 파일은 남는다.
"""

def solution(board, h, w):
    n = len(board)
    count = 0
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(0, 4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
                print(count)
    
    return count
