def solution(record):
    answer = []
    id_name_dict = dict()
    
    for s in record:
        data = s.split(' ')
        
        if data[0] == 'Leave':
            continue
        
        id_name_dict[data[1]] = data[2]
    
    for s in record:
        data = s.split(' ')
        
        if data[0] == 'Enter':
            answer.append(id_name_dict[data[1]] + '님이 들어왔습니다.')
            
        if data[0] == 'Leave':
            answer.append(id_name_dict[data[1]] + '님이 나갔습니다.')
    
    return answer