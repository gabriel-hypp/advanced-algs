n = int(input())

for _ in range(n):
    M, W = map(int, input().split())
    peso_koroks = []
    peso_total = 0
    qtd = 0

    peso_koroks = list(map(int, input().split()))
    peso_koroks.sort()

    for p in peso_koroks:
        if peso_total + p <= W:
            peso_total += p
            qtd += 1
    
    print(qtd)