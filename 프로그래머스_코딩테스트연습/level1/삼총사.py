# 프로그래머스 코딩테스트 연습문제
# 삼총사
# 조합 모듈 사용없이 풀어보고자 작성한 방법.
# 학생수가 많아지면 복잡도가 높기 때문에 실행시간이 길어질 것으로 예상,
# 더 나은 알고리즘이 필요해 보임.

def solution(number):
    answer = 0
    l = len(number)
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if (number[i]+number[j]+number[k] == 0):
                    answer += 1
    return answer
