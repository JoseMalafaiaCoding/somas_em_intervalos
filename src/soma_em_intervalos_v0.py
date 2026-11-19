def somas(v, n, ini, fim, q, resp):
    for k in range(q):
        s = 0
        for i in range(n):
            if i >= ini[k] and i <= fim[k]:
                s = s + v[i]
        resp[k] = s

import random

n = 10000
q = 10000

v = [random.randint(-100, 100) for _ in range(n)]

ini = [0] * q
fim = [n - 1] * q
resp = [0] * q

somas(v, n, ini, fim, q, resp)

print("Primeira soma:", resp[0])
