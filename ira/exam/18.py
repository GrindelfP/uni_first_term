def Sieve(n):
    er = [True] * (n + 1)
    pr = []
    er[0] = er[1] = False
    for i in range(2, n + 1):
        if er[i]:
            for j in range(2 * i, n + 1, i):
                er[j] = False
            pr.append(i)
    ans = []
    for i in range(2, n + 1):
        if er[i]:
            ans.append(i)
    return ans
