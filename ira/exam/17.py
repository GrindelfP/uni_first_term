def Multy_Matrix(a, b):
    c = []
    for i in range(0, len(a)):
        temp = []
        for j in range(0, len(b[0])):
            s = 0
            for k in range(0, len(a[0])):
                s += a[i][k] * b[k][j]
            temp.append(s)
        c.append(temp)
    return c
