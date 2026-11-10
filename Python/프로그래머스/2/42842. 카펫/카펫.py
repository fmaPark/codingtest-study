def solution(brown, yellow):
    # 갈색 = 가로x세로-노란색
    # w x h = b + y
    # y = (w-2)*(h-2)
    for w in range(1, brown+1):
        if (brown+yellow) % w != 0:
            continue
        h = (brown+yellow)//w
        if h > w:
            continue
        if yellow == (w-2)*(h-2):
            return [w, h]
    