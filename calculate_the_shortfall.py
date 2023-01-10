def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        total = i*price
        sum += total
    if money<sum:
        answer = sum-money
        return answer
    else:
        return 0