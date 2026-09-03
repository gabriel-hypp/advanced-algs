import numpy as np

# 65 a 90 [A - Z]
# . é 46
# garantir sem vizinhanca e menor possivel

def temVizinho(quadro, i, j, letra):
    if i > 0 and quadro[i-1][j] == letra:
        return True
    if i < len(quadro)-1 and quadro[i+1][j] == letra:
        return True
    if j > 0 and quadro[i][j-1] == letra:
        return True
    if j < len(quadro)-1 and quadro[i][j+1] == letra:
        return True
    return False

def pinta_quadro(quadro, dim):

    for i in range(dim):
        for j in range(dim):
            letra_inicial = 65
            if quadro[i][j] == 46:
                while(quadro[i][j] == 46):
                    if not temVizinho(quadro, i, j, letra_inicial):
                        quadro[i][j] = letra_inicial
                        break
                    letra_inicial += 1
    return quadro

n = int(input())

for i in range(n):
    dim = int(input())

    quadro = np.zeros((dim, dim))
    for j in range(dim):
        quadro[j] = np.array(list(map(ord, input().strip())))
    
    quadro = pinta_quadro(quadro, dim)

    print(f"Caso {i + 1}:")
    for linha in quadro:
        print("".join(map(chr, linha.astype(int))))
    
