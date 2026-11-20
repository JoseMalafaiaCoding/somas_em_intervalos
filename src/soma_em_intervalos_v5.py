def somas(v, n, ini, fim, q, resp):
    prefixo = [0] * (n + 1)

    i = 0
    while i < n:
        prefixo[i + 1] = prefixo[i] + v[i]
        i += 1

    somas_ate_fim = [0] * q
    k = 0

    while k < q:
        somas_ate_fim[k] = prefixo[fim[k] + 1]
        k += 1

    k = 0
    while k < q:
        resp[k] = somas_ate_fim[k] - prefixo[ini[k]]
        k += 1