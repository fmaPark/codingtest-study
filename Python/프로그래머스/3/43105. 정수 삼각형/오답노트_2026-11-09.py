"""
[오답노트] 2026-11-09

문제: 43105 정수 삼각형 (프로그래머스 Lv3)
유형: DP
걸린 시간: 25분 (2차원 DP 최초 풀이로 힌트를 제공받고 푼 시간)
막힌 지점: 점화식 case를 세우지 못함

진짜 원인
- dp 초기화를 dp=[]이 아닌 dp=[0]으로 잡아 'TypeError: 'int' object does not support item assignment' 오류가 남
- index를 1차원 dp와 같이 [1]부터 잡으려고 시도하다 조건 누락 -> 삼각형을 index 0부터 그대로 밀면 더 편하다는 걸 인지하지 못함
- 이중포문 for j in range(0, len(triangle))로 써서 index error
- ★조건 누락 - 위에서부터 내려오는 걸 dp[i-1][j-1](왼쪽에서 내려오는 케이스)만 고려함
  -> 오른쪽에서 내려오는 경우와 오른쪽/왼쪽 max 케이스를 고려하지 않음. 문제를 말로 풀이하는 연습 필요
- (지금까지 Python 문제를 풀면서) 추상화된 풀이는 떠오르나 그걸 2차원 list로 자연스럽게 옮기는 데 막힘이 있음. 문법을 손에 익히는 연습 필요

다시 풀 날짜: 2일 뒤(11.11)

* 아래 코드는 2026-11-09 제출 코드(정수 삼각형.py) 사본.
  BaekjoonHub가 재제출 시 원본을 덮어써도 이 파일은 남는다.
"""

def solution(triangle):
    dp = []
    for ele in triangle:
        dp.append([0]*len(ele))
    
    for i in range(0, len(triangle)):
        if i == 0:
            dp[0][0] = triangle[0][0]
            continue
        for j in range(0, len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else: 
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    return max(dp[-1])
