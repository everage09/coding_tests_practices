# 정수 제곱근 판별

def solution(n):
    x = 1
    while (x**2 <= n):
        if (x**2==n):
            return (x+1)**2
        else:
            x+=1
    return -1
