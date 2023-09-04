# 나누어 떨어지는  숫자 배열

# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.

def solution(arr, divisor):
    arr.sort()
    return [x for x in arr if x%divisor==0] if any(x for x in arr if x%divisor==0) else [-1]
