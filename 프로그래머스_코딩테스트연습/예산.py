# 프로그래머스 코딩테스트 연습
# 예산
# 가능한 한 budget에 맞춰서 지급하는게 아니라
# 최대한 많은 부서에 지급이 목표이므로 d를 sort,
# 작은 예산 요청부터 지급하여 부서 수를 세도록 한다. 

def solution(d, budget):
    if (sum(d) == budget):
        return len(d)
    total, count = 0, 0
    d.sort()
    for request in d:
        if (total+request <= budget):
            total += request
            count += 1
        else:
            continue
    return count
