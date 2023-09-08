# 문자열을 정수로 바꾸기

def solution(s):
    return int(s) if s[0] != '-' else (-1) * int(s[1::])
