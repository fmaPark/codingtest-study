def solution(park, routes):
    # print(park)
    # print(routes)
    
    width = len(park[0])
    height = len(park)
    
    start = [] # 시작 좌표
    obs = [] # 장애물 좌표
    
    for i in range(0, height):
        for j in range(0, width):
            if park[i][j] == 'S':
                start.append((i, j))
            if park[i][j] == 'X':
                obs.append((i, j))
    
    w = start[0][1]
    h = start[0][0]
    
    for route in routes:
        now_w = w
        now_h = h
        spaces = []
        
        dir, dis = route.split(' ')
        dis = int(dis)
        if dir == 'W':
            w -= dis
            spaces = [(h, x) for x in range(now_w, w-1, -1)]
        elif dir == 'N':
            h -= dis
            spaces = [(x, w) for x in range(now_h, h-1, -1)]
        elif dir == 'S':
            h += dis
            spaces = [(x, w) for x in range(now_h, h+1)]
        elif dir == 'E':
            w += dis
            spaces = [(h, x) for x in range(now_w, w+1)]
            
        print(spaces)
        # w,h가 최댓값보다 큼
        # 장애물이 현 좌표와 이동예정좌표 사이에 있음
        is_obs = False
        for o in obs:
            print(o)
            if o in spaces:
                is_obs = True
        if h >= height or w >= width or h < 0 or w < 0 or is_obs:
            w = now_w
            h = now_h
            
        # print(w, h)
    
    answer = [h, w]
    return answer