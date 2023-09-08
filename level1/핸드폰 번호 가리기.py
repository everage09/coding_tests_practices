# 핸드폰 번호 가리기

# phone_number는 길이 4 이상, 20이하인 문자열입니다.

def solution(phone_number):
    return "*" * (len(phone_number)-4) + phone_number[-4:]
