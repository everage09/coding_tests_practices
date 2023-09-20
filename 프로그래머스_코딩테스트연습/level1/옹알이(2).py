# 옹알이 (2)

"""
머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다.
조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과
네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고
연속해서 같은 발음을 하는 것을 어려워합니다.
문자열 배열 babbling이 매개변수로 주어질 때,
머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
"""

#  ≤ babbling의 길이 ≤ 100
# 1 ≤ babbling[i]의 길이 ≤ 30
# 문자열은 알파벳 소문자로만 이루어져 있습니다.


# A solution using recursion
# Using regex also seems possible
def solution(babbling):
    answer = 0
    basics = ["aya", "ye", "woo", "ma"]
    def check(word, prev=None):
        l = len(word)
        if l < 2:
            return False
        if prev is None:
            if l == 2 or l == 3:
                if word in basics:
                    return True
                else:
                    return False  
            else:
                if word[0:2] in basics:
                    return check(word[2:],word[0:2])
                elif word[0:3] in basics:
                    return check(word[3:],word[0:3])
                else:
                    return False
        else:
            if l == 2 or l == 3:
                if word == prev:
                    return False
                if word in basics:
                    return True
                else:
                    return False
            elif word[0:2] in basics:
                if word[0:2] == prev:
                    return False
                return check(word[2:],word[0:2])
            elif word[0:3] in basics:
                if word[0:3] == prev:
                    return False
                return check(word[3:],word[0:3])
            else:
                return False
            
    for bab in babbling:
        if check(bab):
            answer += 1
    return answer
