# 숫자 문자열과 영단어

# 1 ≤ s의 길이 ≤ 50
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

def solution(s):
    table = {
        "zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4",
        "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    for elem in table.keys():
        if elem in s:
            s = s.replace(elem, table.get(elem))
    return int(s)
