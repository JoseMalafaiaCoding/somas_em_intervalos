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

| Critério | O que se espera | Peso |
|---|---|:---:|
| Análise da v0 | Contagem linha por linha correta, f(n) do pior caso, prova de Θ com tabela e gráfico | 20% |
| Refatorações | 6 versões que realmente diminuem a f(n), cada uma com antes/depois, justificativa, nova f(n) e classe | 30% |
| Correção | Teste automático comparando todas as versões com a v0, com casos de borda | 10% |
| Experimento | Contador de primitivas batendo com a f(n), tempos com mediana, gráficos e ganho total | 25% |
| Conclusão e relatório | Explicação do que rendeu mais e das diferenças entre teoria e medição; clareza | 10% |
| Apresentação | Domínio do grupo sobre o próprio código | 5% |

## Execução

Pistas para começar
* Para que percorrer o vetor inteiro se só interessa o trecho ini..fim?
* Se você soubesse a soma de v[0..x] para todo x, como sairia a soma de v[ini..fim]?

Tabela Padrão
| Teste | n |
|---|---:|
| 1 | 1.000 |
| 2 | 2.000 |
| 3 | 5.000 |
| 4 | 10.433 |
| 5 | 20.000 |
| 6 | 30.000 |
| 7 | 50.000 |
| 8 | 10.000.000 |