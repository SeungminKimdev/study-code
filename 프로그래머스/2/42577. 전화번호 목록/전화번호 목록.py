def solution(phone_book):
    phone_book = sorted(phone_book)
    book_len = len(phone_book)
    for i in range(book_len-1):
            if phone_book[i+1].find(phone_book[i]) == 0:
                return False
    return True