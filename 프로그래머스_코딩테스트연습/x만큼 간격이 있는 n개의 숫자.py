# x 만큼 간격이 있는 n개의 숫자

def solution(x, n):
    return [x for x in range(x,x+n*x,x)] if x != 0 else [x]*n
