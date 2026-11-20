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

## Relatório

### Comparação dos resultados

Os tempos apresentados correspondem à **mediana de cinco execuções** por versão.

| Versão | n = q | Mediana (s) | Comparação com a v0 |
|:---:|---:|---:|---|
| v0 | 10.433 | 8,785270 | Referência |
| v1 | 10.433 | 7,708809 | 12,25% menos tempo |
| v2 | 10.433 | 6,172683 | 29,74% menos tempo |
| v3 | 10.433 | 5,909541 | 32,73% menos tempo |
| v4 (linear) | 10.000.000 | 2,265766 | Não comparável diretamente: entrada diferente |
| v5 (linear) | 10.000.000 | 1,971931 | Não comparável diretamente: entrada diferente |
| v6 | 10.000.000 | 1,557391 | Não comparável diretamente: entrada diferente |

Nos testes com `n = q = 10.433`, as versões v0, v1, v2 e v3 produziram a mesma soma registrada: **15.301**. No cenário 8, com `n = q = 10.000.000`, as versões lineares v4, v5 e v6 também coincidiram, retornando **-269.416**.

**Justificativa dos cenários:** as versões v4, v5 e v6 foram avaliadas no cenário 8 porque, para valores menores de `n`, seus tempos muito curtos dificultam distinguir os ganhos com precisão. Em contrapartida, a v0 torna-se muito lenta em entradas grandes devido à sua complexidade quadrática. Por isso, foram usados tamanhos diferentes para manter os experimentos viáveis. Essa escolha impede calcular diretamente o ganho de tempo da v6 em relação à v0 a partir das medições apresentadas.

### Refatorações que mais renderam

Entre v0 e v3, as melhorias eliminaram verificações e acessos desnecessários, mas mantiveram a complexidade **Θ(n²)**, considerando `n = q`. A v1 reduziu o tempo em **12,25%**, a v2 em **29,74%** e a v3 em **32,73%**, sempre em relação à v0. A passagem de v1 para v2 foi particularmente relevante, pois reduziu o tempo em **19,93%**.

A principal melhoria **algorítmica** ocorreu na v4 linear, com a introdução das **somas prefixadas**. Essa estratégia substituiu o processamento repetido de cada intervalo por um pré-processamento do vetor e consultas de custo constante, reduzindo a complexidade total de **Θ(n²)** para **Θ(n)** quando `n = q` (ou, mais geralmente, de Θ(n·q) para Θ(n + q)).

Nas versões lineares, as refatorações seguintes removeram vetores e laços auxiliares. No cenário 8, a v5 reduziu o tempo em **12,97%** em relação à v4, enquanto a v6 foi **31,26%** mais rápida que a v4 e **21,02%** mais rápida que a v5, considerando a redução percentual do tempo de execução.

### Diferenças entre teoria e medição

A análise das operações primitivas prevê uma redução do trabalho a cada refatoração. As medições acompanharam essa tendência dentro de cada grupo testado com o mesmo `n`, mas **a redução percentual de primitivas não precisa coincidir com a redução percentual de tempo**. O desempenho real também depende do interpretador Python, do acesso à memória, do cache e da carga do sistema durante a execução.

Além disso, como as versões v0–v3 e v4–v6 foram medidas com entradas de tamanhos diferentes, **não é possível comparar diretamente seus tempos absolutos** nem afirmar um fator de aceleração medido da v6 sobre a v0. Para obter esse fator, seria necessário executar ambas com um mesmo tamanho de entrada viável e dividir a mediana da v0 pela mediana da v6.

### Conclusão

Os testes mostram melhorias progressivas: entre as versões quadráticas, a v3 apresentou o menor tempo, com **32,73% de redução em relação à v0**; entre as versões lineares, a v6 foi a mais rápida, com **31,26% de redução em relação à v4 linear**. A maior mudança teórica ocorreu na v4 linear, que reduziu a ordem de crescimento do algoritmo de **Θ(n²) para Θ(n)**, mantendo `n = q`. Os resultados ilustram tanto o benefício de eliminar operações desnecessárias quanto a vantagem de adotar uma estratégia algorítmica mais eficiente.
