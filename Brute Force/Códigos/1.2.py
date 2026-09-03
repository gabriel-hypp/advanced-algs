def dist_hamming(str1, str2):
    if len(str1) != len(str2):
        print("Tamanho diferente")
        return 0
    sum = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            sum += 1
    return sum

M, Q = map(int, input().split())

banco = []
clipes_ia = []

for i in range(M):
    banco.append(input())
for i in range(Q):
    clipes_ia.append(input())

# Para cada clipe, encontrar o indice do clipe do banco
# com a menor dist de hamming para os clipes de ia
# comparando com clipes e substrings no banco
for i in range(Q):
    clipe = clipes_ia[i]
    min_dist = 100
    min_idx = 500
    for j in range(M):
        banco_clipe = banco[j]
        if len(banco_clipe) < len(clipe):
            continue
        for k in range(len(banco_clipe) - len(clipe) + 1):
            sub_banco_clipe = banco_clipe[k:k+len(clipe)]
            dist = dist_hamming(clipe, sub_banco_clipe)
            if dist == min_dist and j < min_idx:
                min_idx = j
            if dist < min_dist:
                min_dist = dist
                min_idx = j
    print(min_idx)
