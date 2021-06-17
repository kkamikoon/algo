import collections
import itertools

# Wroooooooonnnnngggg
# def solution(clothes):
#     clothes_dict    = dict(clothes)
#     clothes_dict_cnt= collections.Counter(dict(clothes).values())
#     comb = 0

#     for i in range(1, len(clothes_dict_cnt)+1):
#         comb += len(list(itertools.combinations(clothes, i))) - summary(clothes_dict_cnt, i)
    
#     print(comb)

    
# def summary(dictionary, i):    
#     if i < 2:
#         return 0
#     elif i == 2:
#         return 1
    
#     sum = 0

#     for v in dictionary.values():
#         sum += (v * (v + 1))/2

#     return int(sum)


def solution(clothes):
    clothes_dict    = dict(clothes)
    clothes_dict_cnt= collections.Counter(dict(clothes).values())
    
    mul = 1

    for cdc_value in clothes_dict_cnt.values():
        mul *= (cdc_value + 1)

    return mul - 1
        



print(f'[=] {solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])}')
print(f'[=] {solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["white_turban", "headgear"]])}')
print(f'[=] {solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["jeen", "pants"], ["green_jeen", "pants"]])}')
print(f'[=] {solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["jeen", "pants"], ["cout", "outer"]])}')
print(f'[=] {solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])}')

'''
얼굴 : 2
상의 : 1
하의 : 1
'''
