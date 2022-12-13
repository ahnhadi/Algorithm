def solution(numbers):
    answer = []
    for i in numbers:
        j = 2*i
        answer.append(j)
    return answer


solution([1, 2, 100, -99, 1, 2, 3])