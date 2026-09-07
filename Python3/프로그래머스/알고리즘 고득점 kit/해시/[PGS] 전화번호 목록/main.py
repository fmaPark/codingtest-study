#try1: 시간초과
def solution(phone_book):
    phone_book.sort(key=len)
    phone_book.sort()
    for i in range(0, len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                return False
        
    return True


# try2: 통과
# sorted array를 출력하고 보니 접두어가 존재한다면 정렬된 다음 요소의 접두어라는 경향성 발견 -> 코드에 적용
def solution(phone_book):
    phone_book.sort()
    for i in range(0, len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    return True