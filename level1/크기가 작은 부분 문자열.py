# 프로그래머스 코딩테스트 연습
# 크기가 작은 부분 문자열
# list comprehension을 사용한 식으로 변경하여 len(list)를 return하는 방식도 가능해 보임.
def solution(t, p):
    answer = 0
    for i in range(len(t)-(len(p)-1)):
        if(t[i:i+len(p)] <= p):
            answer += 1
    return answer
