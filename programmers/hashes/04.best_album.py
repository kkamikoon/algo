def solution(genres, plays):
    each_plays = {}
    g_index    = {}
    answer = []

    for index, g in enumerate(genres):
        try:
            each_plays[g] += plays[index]
        except:
            each_plays[g] = plays[index]

        try:
            g_index[g][str(index)] = plays[index]
        except:
            g_index[g] = {}
            g_index[g][str(index)] = plays[index]
                    

    sorted_genres = sorted(each_plays.items(), key=(lambda x:x[1]), reverse=True)    

    # 출력될 장르 순서
    for sg in sorted_genres:
        # sg[0] : 장르 이름
        tmp = sorted(g_index[sg[0]].items(), key=(lambda x:x[1]), reverse=True)
        try:
            answer.append(int(tmp[0][0]))
        except:
            pass
        
        try:
            answer.append(int(tmp[1][0]))
        except:
            pass

    
    print(each_plays)
    print(sorted(each_plays.items(), key=(lambda x:x[1]), reverse=True))
    print(g_index)
    print(answer)
    print()

    return answer


g_genres = ["classic", "pop", "classic", "classic", "pop"]
g_plays  = [500, 600, 150, 800, 2500]

print(solution(g_genres, g_plays))