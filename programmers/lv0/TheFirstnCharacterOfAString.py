# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, n):
    a = []
    for i in my_string:
        a.append(i)
    for i in a:
        answer = a.pop(n-1)
    return answer