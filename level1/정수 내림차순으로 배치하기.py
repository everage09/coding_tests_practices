# 정수 내림차순으로 배치하기

def solution(n):
    answer = ""
    str_n = [int(str(n)[i]) for i in range(len(str(n)))]
    str_n.sort(reverse=True)
    l = list(map(str,str_n))
    for elem in l:
        answer += elem
    return int(answer)
