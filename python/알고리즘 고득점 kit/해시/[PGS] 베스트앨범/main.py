def solution(genres, plays):
    songs_counter_dict = {}
    songs_dict = {}

    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in songs_dict:
            songs_dict[genre] = []
            songs_counter_dict[genre] = 0
        
        songs_dict[genre].append([index, play]) 
        songs_counter_dict[genre] += play 

    sorted_genres = sorted(songs_counter_dict.items(), key=lambda item: item[1], reverse=True)

    answer = []
    for genre, _ in sorted_genres:
        songs_dict[genre].sort(key=lambda x: (-x[1], x[0]))
        answer.extend([song[0] for song in songs_dict[genre][:2]])

    return answer
