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