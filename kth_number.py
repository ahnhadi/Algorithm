def solution(array, commands):
    answer = []
    for i in commands:
        a = i[0]-1
        b = i[1]-1
        c = i[2]-1
        if a==b:
            result = array[a]
            answer.append(result)
        else:
            result = sorted(array[a:b+1])
            answer.append(result[i[2]-1])
    return answer


