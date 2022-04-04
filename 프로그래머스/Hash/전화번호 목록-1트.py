# 억지해쉬 - 차라리 이렇게 하려면 걍 이중포문쓰셈..
# 효율성테스트 2/4만 통과(cause of 시간초과)
    # -> 해쉬 다를게 써보기
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        standard = len(phone_book[i])
        hash = {}
        hash[phone_book[i]] = 0
        for j in range(len(phone_book)):
            if len(phone_book[j]) >= standard and phone_book[j][0:standard] == phone_book[i]:
                hash[phone_book[i]] += 1
        if hash[phone_book[i]] >= 2:
            answer = False
            break
    return answer


# 이중포문으로 풀이 -> 당연히 시간초과 ㅠ 해쉬문제잖아
# def solution(phone_book):
#     answer = True
#     for ele in phone_book:
#         cnt = 0
#         tmp = len(ele)
#         for ele2 in phone_book:
#             if len(ele2) >= tmp and ele2[0:tmp] == ele:
#                 cnt += 1
#         if cnt >= 2:
#             answer = False
#             break
        
#     return answer

# print(solution(["119", "97674223", "1195524421"]))