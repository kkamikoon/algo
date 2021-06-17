import math
import collections

def solution(progresses, speeds):
    res = []

    for index in range(len(progresses)):
        res.append(str(math.ceil((100-progresses[index])/speeds[index])))

    res.sort()

    print(res)

    cnt = collections.Counter(res)

    print(cnt)

solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
