def solution(x, n):
    answer = []
    for i in range(n):
        number = (i+1)*x
        answer.append(number)

    return answer


solution(2,5)
solution(4,3)
solution(-4,2)