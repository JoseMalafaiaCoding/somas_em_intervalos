def somas(v, n, ini, fim, q, resp):
    k = 0
    while k < q:
        s = 0
        i = ini[k]
        limite = fim[k]
        while i + 3 <= limite:
            s = s + v[i] + v[i + 1] + v[i + 2] + v[i + 3]
            i += 4
        while i <= limite:
            s = s + v[i]
            i += 1

        resp[k] = s
        k += 1
