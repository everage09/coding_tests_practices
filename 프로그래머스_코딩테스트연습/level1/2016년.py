# 2016년

"""
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요?
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다.
예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.
"""

# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다.
# (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

def solution(a, b):
    day = 0
    answer = ''
    days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    # 29,30,31 달들을 하나로 합쳐서 개선 가능했다
    days29 = [2]
    days30 = [4,6,9,11]
    days31 = [1,3,5,7,8,10,12]
    for month in range(1,a):
        if month in days29:
            day += 29
        elif month in days30:
            day += 30
        else:
            day += 31
    day += b
    print(day)
    answer = days[(5+day%7)%7-1]
    return answer
