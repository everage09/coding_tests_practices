# 프로그래머스 코딩테스트 연습
# 시저 암호
# 알파벳은 26개이므로 0-25까지 범위에 알파벳을 배정하여
# 시저 암호 로테이션이 되도록 한다.
# 답에는 숫자로 식을 기입하였으나, 
# 65 = ord('A'), 97 = ord('a') 이므로 ord를 사용하여 표기하는 법이
# 코드가 더 이해하기 쉬운 방법으로 생각된다.

def solution(s, n):
    l = list(s)
    after = []
    for letter in l:
        if letter == ' ':
            after.append(' ')
            continue
        if letter.isupper():
            after.append(chr((ord(letter)-65+n)%26+65))
        else:
            after.append(chr((ord(letter)-97+n)%26+97))
    return "".join(after)
