# N개의 최소공배수

"""
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중
공통이 되는 가장 작은 숫자를 의미합니다.
예를 들어 2와 7의 최소공배수는 14가 됩니다.
정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
"""

# GCD : Greatest Common Denominator
# LCM : Lowest Common Multiple
# let the two number be A = G*a, B = G*b where a and b are coprime numbers. Then,
# LCM = A * B / GCD (= G*a * G*b / G = G*a*b)

def solution(arr):
    n1 = arr[0]
    def GCD(a,b):
        while b > 0:
            a, b = b, a%b
        return a
    for idx in range(1,len(arr)):
        G = GCD(n1, arr[idx])
        L = n1 * arr[idx] / G
        n1 = L
    return L
