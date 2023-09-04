# 2018 KAKAO BLIND RECRUITMENT
# [1차] 비밀지도

"""
[입력 형식]
입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.

1 ≦ n ≦ 16
arr1, arr2는 길이 n인 정수 배열로 주어진다.
정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 즉, 0 ≦ x ≦ 2n - 1을 만족한다.

[출력 형식]
원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.

"""

def solution(n, arr1, arr2):
    newMap = [bin(a | b)[2:] for a,b in zip(arr1,arr2)]
    for idx, row in enumerate(newMap):
        row = row.rjust(n,'0')
        row = row.replace("1","#")
        row = row.replace("0", " ")
        newMap[idx] = row
    return newMap
