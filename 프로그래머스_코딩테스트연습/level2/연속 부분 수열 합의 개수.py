# 연속 부분 수열 합의 개수

"""
철호는 수열을 가지고 놀기 좋아합니다.
어느 날 철호는 어떤 자연수로 이루어진 원형 수열의 연속하는 부분 수열의 합으로 만들 수 있는 수가모두 몇 가지인지 알아보고 싶어졌습니다.
원형 수열이란 일반적인 수열에서 처음과 끝이 연결된 형태의 수열을 말합니다.

원형 수열은 처음과 끝이 연결되어 끊기는 부분이 없기 때문에 연속하는 부분 수열도 일반적인 수열보다 많아집니다.
원형 수열의 모든 원소 elements가 순서대로 주어질 때,
원형 수열의 연속 부분 수열 합으로 만들 수 있는 수의 개수를 return 하도록 solution 함수를 완성해주세요.
"""

# 3 ≤ elements의 길이 ≤ 1,000
# 1 ≤ elements의 원소 ≤ 1,000


# This answer takes redundant computation --> (Currently quite slow due to O(n^3) complexity)
# Could be enhanced from O(n^3) to O(n^2) by storing sum value to a variable without using sum func.
# Without slicing list, just iterate over each elements of the list and add it to the sum value.

def solution(elements):
    answer = set()
    l = len(elements)
    for i in range(1,l+1):
        for j in range(l):
            if l > j+i:
                answer.add(sum(elements[j:j+i]))
            else:
                answer.add(sum(elements[j:l]+elements[:j+i-l]))
            
    return len(answer)
