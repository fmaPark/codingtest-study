def solution(survey, choices):
    categories = {
        'RT': 0,
        'CF': 0,
        'JM': 0,
        'AN': 0
    }
    
    for i in range(0, len(survey)):
        print(i)
        if (survey[i] == 'RT'):
            categories['RT'] += -(choices[i] - 4)
        elif (survey[i] == 'TR'):
            categories['RT'] += (choices[i] - 4)
        elif (survey[i] == 'CF'):
            categories['CF'] += -(choices[i] - 4)
        elif (survey[i] == 'FC'):
            categories['CF'] += (choices[i] - 4)
        elif (survey[i] == 'JM'):
            categories['JM'] += -(choices[i] - 4)
        elif (survey[i] == 'MJ'):
            categories['JM'] += (choices[i] - 4)
        elif (survey[i] == 'AN'):
            categories['AN'] += -(choices[i] - 4)
        elif (survey[i] == 'NA'):
            categories['AN'] += (choices[i] - 4)
    
    answer = ''
    if (categories['RT'] >= 0):
        answer += 'R'
    else:
        answer += 'T'
        
    if (categories['CF'] >= 0):
        answer += 'C'
    else:
        answer += 'F'
        
    if (categories['JM'] >= 0):
        answer += 'J'
    else:
        answer += 'M'
        
    if (categories['AN'] >= 0):
        answer += 'A'
    else:
        answer += 'N'
    
    print(categories)
    
    return answer