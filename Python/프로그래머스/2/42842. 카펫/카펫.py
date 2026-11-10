def solution(brown, yellow):
    # 갈색 = 가로x세로-노란색
    # w x h = b + y
    # y = (w-2)*(h-2)
    w = brown
    h = 1
    for w in range(1, brown+1):
        h = (brown+yellow)/w
        if h > w:
            continue
        if w*h == brown+yellow and yellow == (w-2)*(h-2):
            break
    return [w, h]