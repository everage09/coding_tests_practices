# 다음 큰 숫자

"""
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때,
n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
"""

# n은 1,000,000 이하의 자연수 입니다.

def solution(n):
    answer = 0
    binary = list(bin(n)[2:])
    l = len(binary)
    z = binary.count('0')

    # if n is exponetiation of 2, shift left
    if n&n-1 == 0:
        return n<<1
    # if there is no '0', i.e. n=2**a-1 form(a is integer), insert a '0' 
    if z == 0:
        binary.insert(1,"0")
        return int('0b'+''.join(binary), 2)
    else:
        # if n in binary form has all '0's at the end,
        # e.g. '1111000' -> next number needs 1 more digit. 
        # thus the next number would have one 1 on left most digit
        # and all the other one the right most digits.
        if n^int('0b'+'1'*(l-z)+'0'*z,2) == 0:
            return int('0b1'+ '0'*(z+1) + bin(n>>(z+1))[2:], 2)
        # All the other case corresponds to this case
        # find the rightmost"01" in the binary form of n.
        # swap '01' to '10', then reverse all the numbers on the right side of swapped 0 and 1.
        else:
            idx = bin(n)[2:].rfind('01')
            left = binary[:idx+2]
            left[idx:idx+2] = list('10')
            right = binary[idx+2:]
            right.reverse()
            new = left + right
            return int('0b'+ ''.join(new), 2)
            
