import math

def solution(progresses, speeds):
    days = []

    # N번 계산
    for index in range(len(progresses)):
        days.append(math.ceil((100-progresses[index])/speeds[index]))   

    # N번 계산
    tmp_cnt = 1
    tmp_day = days[0]

    answer = []

    for index in range(len(days)):
        try:
            if tmp_day >= days[index+1]:
                tmp_cnt += 1
            else:
                answer.append(tmp_cnt)
                tmp_day = days[index+1]
                tmp_cnt = 1
        except:
            answer.append(tmp_cnt)
    
    return answer

solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
