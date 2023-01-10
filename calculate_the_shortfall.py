def solution(price, money, count):
    ran = range(1,count+1)
    sum = 0
    for i in ran:
        total = i*price
        sum = sum + total
    if money<sum:
        answer = sum-money
        return answer
    else:
        return 0


