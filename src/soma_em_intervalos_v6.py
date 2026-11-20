def somas(v, n, ini, fim, q, resp):
    # prefixo[x] guarda a soma dos primeiros x elementos do vetor.
    prefixo = [0] * (n + 1)

    i = 0
    while i < n:
        prefixo[i + 1] = prefixo[i] + v[i]
        i += 1

    k = 0
    while k < q:
        resp[k] = prefixo[fim[k] + 1] - prefixo[ini[k]]
        k += 1
