# 제일 작은 수 제거하기

# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

def solution(arr):
    if len(arr) != 1:
        arr.pop(arr.index(min(arr)))
        answer = arr
    else:
        answer = [-1]
    
    return answer
