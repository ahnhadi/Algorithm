def solution(m, n):
    answer = []
    a=m
    b=n
    # 최대공약수 gcd
    while True:
        if m%n == 0:
            break
        gcd = m%n
        m = n
        n = gcd
    gcd = n
    answer.append(gcd)

    # 최소공배수 lcm
    lcm = a*b/gcd
    answer.append(lcm)

    return answer
