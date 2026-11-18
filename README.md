# Somas em Intervalos - Análise de Complexidade

Projeto da disciplina de **Complexidade de Algoritmos** para analisar e otimizar um algoritmo que responde a `q` consultas de soma em intervalos `[ini, fim]` de um vetor com `n` elementos.

## Objetivo

Partir da implementação original (**v0**, Θ(n · q)) e realizar **6 refatorações cumulativas** (v1 a v6), reduzindo o número de operações sem alterar os resultados. Uma das otimizações possíveis é usar **somas prefixadas**, alcançando Θ(n + q).

## Código original (v0)

Implementação fornecida no enunciado (Tema 12):

```c
void somas(int v[], int n, int ini[], int fim[], int q, long resp[]) {
    for (int k = 0; k < q; k++) {
        long s = 0;
        for (int i = 0; i < n; i++) {
            if (i >= ini[k] && i <= fim[k]) {
                s = s + v[i];
            }
        }
        resp[k] = s;
    }
}
```

## Etapas

- Analisar a complexidade e a função de custo `f(n, q)` de cada versão.
- Validar todas as versões contra a v0 com **1.000 entradas aleatórias** e casos de borda.
- Medir tempo e contar operações em **8 tamanhos de entrada**, com **5 repetições** por tamanho (mediana).
- Comparar os resultados por meio de tabelas e gráficos e documentar as conclusões.

## Execução

As instruções para executar as versões, os testes e os experimentos serão adicionadas conforme a implementação do projeto.
