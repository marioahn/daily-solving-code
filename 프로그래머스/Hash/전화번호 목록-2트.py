def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        tmp = len(phone_book[i])
        if phone_book[i+1][0:tmp] == phone_book[i]:
            answer = False
            return answer

    return answer

