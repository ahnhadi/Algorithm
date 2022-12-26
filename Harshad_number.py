def solution(x):
    if x>=1000:
        a = x//1000
        b = (x%1000)//100
        c = (x%100)//10
        d = x%10
        answer = x%(a+b+c+d)
    elif 100<=x<1000:
        a = x//100
        b = (x%100)//10
        c = x%10
        answer = x%(a+b+c)
    elif 10<=x<100:
        a = x//10
        b = x%10
        answer = x%(a+b)
    else:
        return True
    if answer ==0:
        return True
    else:
        return False