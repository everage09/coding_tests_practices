# 약수의 개수와 덧셈

"""
두 정수 left와 right가 매개변수로 주어집니다.
left부터 right까지의 모든 수들 중에서,
약수의 개수가 짝수인 수는 더하고,
약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
"""

# 1 ≤ left ≤ right ≤ 1,000

# 약수의 개수가 홀수 -> 제곱수
# 약수의 개수가 짝수 -> 그 외

def solution(left, right):
    answer = 0
    for num in range(left,right+1):
        if (num**0.5 == int(num**0.5)):
            answer-=num
        else:
            answer+=num
    return answer
