import string

tmp = string.digits+string.ascii_lowercase
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]


def solution(n):
    con = convert(n,3)
    con1 = con[::-1]
    answer = int(con1,3)
    return answer
    print(con1)