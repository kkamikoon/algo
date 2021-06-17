import collections

# Wrong
# def solution(participant, completion):
#     for c in completion:
#         if c in participant:
#             participant.remove(c)

#     return answer


def solution(participant, completion):
    p_cnt = {}
    c_cnt = {}

    for p in participant:
        try:
            p_cnt[p] += 1
        except:
            p_cnt[p] = 1

    for c in completion:
        try:
            c_cnt[c] += 1
        except:
            c_cnt[c] = 1

    for key in p_cnt.keys():
        try:
            if p_cnt[key] != c_cnt[key]:
                return key
        except:
            return key


def other_solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def other_solution_test(participant, completion):
    p = collections.Counter(participant)
    c = collections.Counter(completion)
    print(f"[+] p      : {p}")
    print(f"[+] c      : {c}")
    print(f"[+] p - c  : {p-c}")


print(other_solution_test(["leo", "kiki", "eden"],["eden", "kiki"]))
print(other_solution_test(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(other_solution_test(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

