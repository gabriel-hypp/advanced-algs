n = int(input())

for _ in range(n):
    # Num palavras do conto, Max linha por pag, Max carac por linha
    N, L, C = map(int, input().split())

    palavras = input().split()

    caracteres = 0
    linhas = 1

    for p in palavras:
        tam = len(p)

        if caracteres == 0:
            caracteres += tam
        elif caracteres + 1 + tam <= C:
            caracteres += 1 + tam
        else:
            linhas += 1
            caracteres = tam
        
    if linhas % L == 0:
        paginas = linhas // L
    else:
        paginas = linhas // L + 1
    
    print(paginas)