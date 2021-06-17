import re

# Wrong 1
# def solution(phone_book):
#     str_phone_book = "-".join(phone_book)

#     for pb in phone_book:
#         if str_phone_book.count(pb) > 1:
#             return False

#     return True


# Wrong 2 => 모두 통과 but 효율성 문제
# def solution(phone_book):
#     str_phone_book = "-".join(phone_book)

#     for pb in phone_book:
#         if indexes_check(indexes=[i.start()-1 for i in re.finditer(f"{pb}", str_phone_book)], string=str_phone_book) >= 2:
#             return False

#     return True

# def indexes_check(indexes, string):
#     cnt = 0

#     for idx in indexes:
#         if list(string)[idx] == "-" or idx == -1:
#             # 접두사 찾음
#             cnt += 1

#     return cnt   

# Wrong 3 틀린 문제 있음. 효율성은 괜찮음
# def solution(phone_book):
#     str_phone_book = "-".join(phone_book)

#     for index, pb in enumerate(phone_book):
#         if index == 0 and str_phone_book.count(f"-{pb}") > 0:
#             return False
#         elif str_phone_book.count(f"-{pb}") > 1:
#             return False

#     return True


# 91.7 점(효울성 2개 실패)
# def solution(phone_book):
#     phone_book.sort(reverse=False)
#     str_phone_book  = "-".join(phone_book)

#     for index, pb in enumerate(phone_book):
#         if index == 0 and str_phone_book.count(f"-{pb}") > 0:
#             return False
#         elif str_phone_book.count(f"-{pb}") > 1:
#             return False

#     return True


# 91.7 점(효울성 2개 실패)
# def solution(phone_book):
#     phone_book = sorted(phone_book)
#     str_phone_book  = "-".join(phone_book)
#     start = phone_book[0]

#     for pb in phone_book:
#         if start == pb and str_phone_book.count(f"-{pb}") > 0:
#             return False
#         elif str_phone_book.count(f"-{pb}") > 1:
#             return False

#     return True


# def tmp(phone_book):
#     str_phone_book  = "-".join(phone_book)

#     for index, pb in enumerate(phone_book):
#         # print(f"[+] {pb} : {str_phone_book.count(f'-{pb}')}")
#         if index == 0 and str_phone_book.count(f"-{pb}") > 0:
#             return False
#         elif str_phone_book.count(f"-{pb}") > 1:
#             return False

#     return True


def solution(phone_book):
    phone_book.sort(reverse=False)

    for i in range(0, len(phone_book)):
        try:
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                return False
        except:
            pass
    
    return True

        



print("01. ", solution(["119", "97674223", "1195524421"]))
print("02. ", solution(["123","456","789"]))
print("03. ", solution(["12","123","1235","567","88"]))
print("04. ", solution(["12","567","88","123","1235"]))
print("05. ", solution(["8", "12","123","1235","567","88"]))
print("06. ", solution(["7890","123","456","789"]))