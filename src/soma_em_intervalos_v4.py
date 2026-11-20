def somas(v, n, ini, fim, q, resp):
    k = 0
    while k < q:
        s = 0
        i = ini[k]
        limite = fim[k]

        # Processa dois elementos por iteração.
        while i + 1 <= limite:
            s = s + v[i] + v[i + 1]
            i += 2

        # Trata o elemento restante em intervalos de tamanho ímpar.
        if i <= limite:
            s = s + v[i]

        resp[k] = s
        k += 1
