# 소수 찾기

"""
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수,
solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
"""

# n은 2이상 1000000이하의 자연수입니다.

# 소수가 아닌 수는 1로 표시하게 만든다.
def solution(n):
    nums = [0 for i in range(n)]
    nums[0] = 1
    for i in range(2,n):
        if nums[i-1] == 0:
            for j in range(i+i,n+1,i):
                nums[j-1] = 1
    return nums.count(0)
