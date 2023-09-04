# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    return sum(x for x in range(a,b+1)) if a <= b else sum(x for x in range(b,a+1))
