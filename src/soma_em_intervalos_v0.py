def somas(v, n, ini, fim, q, resp):
    k = 0
    while k < q:
        s = 0
        i = 0
        while i < n:
            if i >= ini[k] and i <= fim[k]:
                s = s + v[i]
            i += 1
        resp[k] = s
        k += 1