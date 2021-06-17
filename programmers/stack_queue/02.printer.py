import collections

# def solution(priorities, location):  
#     mine            = priorities[location]
#     mine_forward    = priorities[:location]
#     mine_backward   = priorities[location+1:]
    
#     forward_cnt     = collections.Counter(mine_forward)
#     backward_cnt    = collections.Counter(mine_backward)
#     forward_sum     = 0
#     backward_sum    = 0

#     print(f'[=] mine_forward   : {mine_forward}')
#     print(f'[=] mine_backward  : {mine_backward}')

#     # forward
#     for i in range(0, mine):
#         # print(f"[=] forward_cnt  : {i} | {forward_cnt[i]}")
#         forward_sum += forward_cnt[i]

#     # backward
#     for i in range(0, 10-mine):
#         # print(f"[=] backward_cnt : {mine+i} | {backward_cnt[mine+i]}")
#         backward_sum += backward_cnt[mine+i]

# def solution(priorities, location):
#     mine        = priorities[location]
#     answer      = 0
#     current_list= priorities

#     for index in range(len(priorities)):
#         tmp_list    = []
#         m, mi       = get_max(current_list)
#         if m == mine:
#             print(f"[=] answer : {answer}")
#             return answer
#         tmp_list   += current_list[:mi]
#         tmp_list   += current_list[mi+1:]
#         answer     += 1
#         current_list= tmp_list

#     print(f"[=] answer : {answer}")
          
# def solution(priorities, location):
#     mine        = priorities[location]
#     answer      = 0
#     current_list= priorities

#     for index in range(len(priorities)):
#         print(f"[=] current  : {current_list}")
#         tmp_list    = []
#         m, mi       = get_max(current_list)
        
#         tmp_list   += current_list[mi:]
#         tmp_list   += current_list[:mi]
#         answer     += 1

#         if m == mine:
#             rest = 0

#             print(f"[+] if")
#             print(f"[=] tmp_list : {tmp_list}")
#             print(f"[-] answer   : {answer}")
#             print(f"[-] location : {location}")

#             for i in range(location-1):
#                 try:
#                     if tmp_list[i] == mine:
#                         rest += 1
#                 except:
#                     pass

#             return answer + rest
#         elif mi == 0:
            
#             print(f"[+] if")
#             print(f"[=] tmp_list : {tmp_list}")
#             print(f"[-] answer   : {answer}")
#             print(f"[-] location : {location}")
#             print()
#         else:
#             location    = len(current_list[:mi]) - len(current_list[:location+1]) + len(current_list[mi+1:])
#             print(f"[+] else")
#             print(f"[=] tmp_list : {tmp_list}")
#             print(f"[-] answer   : {answer}")
#             print(f"[-] location : {location}")
#             print()
        
#         current_list= tmp_list


# def solution(priorities, location):
#     mine        = priorities[location]
#     answer      = 0
#     current_list= priorities

#     for index in range(len(priorities)):
#         tmp_list    = []
#         m, mi       = get_max(current_list)
        
#         tmp_list   += current_list[mi:]
#         tmp_list   += current_list[:mi]

#         if mi == 0:
#             location -= 1
#         else:
#             location    = len(current_list[:mi]) - len(current_list[:location]) + len(current_list[mi:])

#         tmp_list.pop(0)
#         answer += 1

#         print(f"[=] current  : {current_list}")
#         print(f"[=] tmp_list : {tmp_list}")
#         print(f"[=] location : {location}")
#         print(f"[=] anwswer  : {answer}")
        
#         current_list= tmp_list


# Nooooooooooooooooo
# def solution(priorities, location):
#     mine        = priorities[location]
#     answer      = 0

#     m, mi       = get_max(priorities)

#     forward_cnt = 0
#     backward_cnt= 0
#     middle_cnt  = 0

#     # for pf in priorities[:mi]:
#     #     if pf >= mine:
#     #         forward_cnt += 1
    
#     # for pf in priorities[mi:]:
#     #     if pf >= mine:
#     #         backward_cnt += 1
        
#     # for pf in priorities[location:mi]:
#     #     if pf >= mine:
#     #         middle_cnt += 1

#     for pf in priorities[:location]:
#         if pf >= mine:
#             forward_cnt += 1

#     for pf in priorities[location+1:]:
#         if pf > mine:
#             backward_cnt += 1
    

#     answer = forward_cnt - middle_cnt + backward_cnt

#     return answer

# def solution(priorities, location):
#     mine        = priorities[location]
#     answer      = 0
#     current_list= priorities

#     for index in range(len(priorities)):
#         tmp_list    = []
#         m, mi       = get_max(current_list)

#         # print(f"[=] m  : {m}")
#         # print(f"[=] mi : {mi}")
        
#         tmp_list   += current_list[mi:]
#         tmp_list   += current_list[:mi]

#         print(f"[=] len(current_list[:mi]) : {len(current_list[:mi])}")
#         print(f"[=] len(current_list[:location]) : {len(current_list[:location])}")
#         print(f"[=] len(current_list[mi:]) : {len(current_list[mi:])}")
#         print(f"[=] len(current_list[location:mi]) : {len(current_list[location:mi])}")

#         if m == mine:
#             rest = 0
#             for i in range(location):
#                 rest += 1
            
#             return answer + rest
#         elif mi == 0:
#             location = location - 1
#         else:
#             location    = len(current_list[:mi]) - len(current_list[:location]) + len(current_list[mi:]) - len(current_list[location:mi])
        

#         print(f"[=] current  : {current_list}")
#         print(f"[=] before_p : {tmp_list}")
#         tmp_list.pop(0)
#         answer += 1

        
#         print(f"[=] after_p  : {tmp_list}")
#         print(f"[=] location : {location}")
#         print(f"[=] anwswer  : {answer}")
#         print()

#         current_list= tmp_list


def solution(priorities, location):
    mine         = priorities[location]
    answer       = 0
    current_list = priorities


    for index in range(len(priorities)):
        tmp_list    = []
        m, mi       = get_max(current_list)

        tmp_list   += current_list[mi:]
        tmp_list   += current_list[:mi]
    
        for i in range(current_list.index(max(current_list))):
            if location == 0:
                location = len(current_list) - 1
            else:
                location = location - 1

            mi = mi - 1

        current_list = tmp_list
        current_list.pop(0)
        location = location - 1

        answer += 1

        if location < 0:
            return answer

    return answer           


def get_max(current_list):
    return max(current_list), current_list.index(max(current_list))


    

print(f"[+][+][+][+] answer : {solution([2,1,3,2], 2)}") # 1
print()
print(f"[+][+][+][+] answer : {solution([1,1,9,1,1,1], 0)}") # 5
print()
print(f"[+][+][+][+] answer : {solution([1, 1, 2, 3, 4, 1, 2, 1, 1, 9, 8, 7, 8, 1], 4)}") # 5
print()
print(f"[+][+][+][+] answer : {solution([1, 1, 2, 3, 4, 1, 2, 1, 1, 9, 8, 7, 8, 1, 4], 4)}") # 6
print()
print(f"[+][+][+][+] answer : {solution([1, 1, 2, 3, 4, 1, 2, 1, 1, 9, 8, 7, 8, 1, 4], 0)}") # 14
print()
print(f"[+][+][+][+] answer : {solution([2, 3, 4, 1, 2, 1, 1, 9, 8, 7, 8, 1], 4)}") # 8
print()
