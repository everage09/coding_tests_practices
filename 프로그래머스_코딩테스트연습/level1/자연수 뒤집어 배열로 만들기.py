# 자연수 뒤집어 배열로 만들기

def solution(n):
    return [int(str(n)[::-1][i]) for i in range(len(str(n)))]
