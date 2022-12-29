def solution(n):
    pizza = n//7
    if n == 1:
        answer = 1
    elif n>1:
        if n%7 == 0:
            answer = pizza
        else:
            answer = pizza+1
    return answer




solution(7)
solution(1)
solution(15)
