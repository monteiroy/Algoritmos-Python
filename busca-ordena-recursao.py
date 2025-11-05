import random
import time

# 1. BUSCA EM LISTA

def pesquisa_sequencial(lista, valor):
    
    comparacoes = 0
    for i, elemento in enumerate(lista):
        comparacoes += 1
        if elemento == valor:
            return i, comparacoes
    return -1, comparacoes


def pesquisa_binaria(lista, valor):

    inicio, fim = 0, len(lista) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == valor:
            return meio, comparacoes
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes


def testar_buscas():
    lista = sorted(random.sample(range(1000), 100))
    valor = random.choice(lista)

    print("BUSCA EM LISTA")
    print(f"Valor a procurar: {valor}")

    inicio = time.time()
    indice_seq, comp_seq = pesquisa_sequencial(lista, valor)
    tempo_seq = time.time() - inicio

    inicio = time.time()
    indice_bin, comp_bin = pesquisa_binaria(lista, valor)
    tempo_bin = time.time() - inicio

    print(f"Sequencial -> Índice: {indice_seq}, Comparações: {comp_seq}, Tempo: {tempo_seq:.8f}s")
    print(f"Binária    -> Índice: {indice_bin}, Comparações: {comp_bin}, Tempo: {tempo_bin:.8f}s\n")


# 2. ORDENAÇÃO

def ordenacao_selecao(lista):
    
    a = lista.copy()
    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def quicksort(lista):
    
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)


def testar_ordenacao():
    lista = [random.randint(0, 10000) for _ in range(1000)]

    print("ORDENAÇÃO")

    inicio = time.time()
    ordenacao_selecao(lista)
    tempo_sel = time.time() - inicio

    inicio = time.time()
    quicksort(lista)
    tempo_quick = time.time() - inicio

    inicio = time.time()
    sorted(lista)
    tempo_sorted = time.time() - inicio

    print(f"Seleção   -> {tempo_sel:.6f}s")
    print(f"Quicksort -> {tempo_quick:.6f}s")
    print(f"sorted()  -> {tempo_sorted:.6f}s\n")


# 3. RECURSIVIDADE

def fatorial(n):
   
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


def fibonacci(n):
   
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def soma_lista(lista):
   
    if len(lista) == 0:
        return 0
    return lista[0] + soma_lista(lista[1:])


def testar_recursividade():
    print("RECURSIVIDADE")
    print("Fatorial(5):", fatorial(5))
    print("Fibonacci(10):", fibonacci(10))
    print("Soma [1..10]:", soma_lista(list(range(1, 11))))
    print()



if __name__ == "__main__":
    testar_buscas()
    testar_ordenacao()
    testar_recursividade()
