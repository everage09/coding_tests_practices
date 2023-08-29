# 프로그래머스
# 이상한 문자 만들기
def solution(s):
    answer = ""
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
            count = 0
        else:
            if count%2 == 0:
                answer += s[i].upper()
            else:
                answer += s[i].lower()
            count += 1
    return answer
