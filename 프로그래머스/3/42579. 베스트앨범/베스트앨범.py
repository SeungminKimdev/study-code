def solution(genres, plays):
    songs = len(genres)
    genre_total = {} # 장르별 재생 합
    genre_songs = {} # 장르별 각 노래 재생수, 고유번호
    
    for i in range(songs):
        genre = genres[i]
        play = plays[i]
        if genre in genre_total:
            genre_total[genre] += play
            genre_songs[genre].append((play, i))
        else:
            genre_total[genre] = play
            genre_songs[genre] = [(play, i)]
    
    answer = []
    genre_rank = sorted(genre_total, key=lambda x:genre_total[x], reverse=True)
    for genre in genre_rank:
        genre_rank_songs = sorted(genre_songs[genre], key=lambda x:(x[0],-x[1]), reverse=True)
        genre_songs_num = 0
        for song, i in genre_rank_songs:
            answer.append(i)
            genre_songs_num += 1
            if genre_songs_num == 2:
                break
    return answer