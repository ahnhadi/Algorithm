def solution(a, b):
    r = range(a,b+1)
    s = range(b,a+1)
    answer = 0
    if a==b:
        answer = a
    elif a<b:
        for i in r:
            answer = answer + i
    else :
        for i in s:
            answer = answer + i
    return answer


solution(3,5)
solution(3,3)
solution(5,3)