def solution(numbers):
    nums = [1,2,3,4,5,6,7,8,9,0]
    answer = []
    for i in nums:
        if i not in numbers:
            answer.append(i)

    print(sum(answer))
    return sum(answer)



solution([1,2,3,4,6,7,8,0]) #14
solution([5,8,4,0,6,7,9]) #6