def solution(dots):
    x = []
    y = []
    for i in dots:
        x.append(i[0])
        y.append(i[1])
    x.sort()
    y.sort()
    x1 = x[1] - x[0]
    x2 = x[3] - x[2]
    x3 = x[2] - x[0]
    x4 = x[3] - x[1]
    y1 = y[1] - y[0]
    y2 = y[3] - y[2]
    y3 = y[2] - y[0]
    y4 = y[3] - y[1]
    if (x1/y1 == x2/y2):
        return 1
    elif(x3/y3 == x4/y4):
        return 1
    else :
        return 0





solution([[1, 4], [9, 2], [3, 8], [11, 6]])
solution([[3, 5], [4, 1], [2, 4], [5, 10]])