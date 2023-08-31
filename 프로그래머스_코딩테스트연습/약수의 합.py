# 프로그래머스 코딩테스트 연습
# 약수의 합

def solution(n):
    return sum([x for x in range(1,n+1) if n%x==0])
