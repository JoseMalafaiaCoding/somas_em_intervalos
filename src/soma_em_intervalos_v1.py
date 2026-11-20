def somas(v, n, ini, fim, q, resp):
    k = 0
    while k < q:
        s = 0
        i = ini[k]
        while i < n:
            if i <= fim[k]:
                s = s + v[i]
            i += 1
        resp[k] = s
        k += 1
