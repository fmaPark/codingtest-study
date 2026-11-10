def solution(brown, yellow):
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