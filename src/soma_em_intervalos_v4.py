def somas(v, n, ini, fim, q, resp):
    k = 0
    while k < q:
        s = 0
        i = ini[k]
        limite = fim[k]
        while i + 1 <= limite:
            s = s + v[i] + v[i + 1]
            i += 2
        if i <= limite:
            s = s + v[i]

        resp[k] = s
        k += 1
