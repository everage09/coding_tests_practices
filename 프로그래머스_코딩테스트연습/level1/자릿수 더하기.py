# 프로그래머스 코딩테스트 연습
# 자릿수 더하기

def solution(n):
    answer = 0
    while(n//10 != 0):
        answer += n%10
        n //= 10
    answer += n%10
    return answer
