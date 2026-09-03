# Dificil isso aqui

# quer calcular a^b mod 10^9 + 7

# usa algoritmo de exponenciaciao binaria e propriedade de mod
# a^b = a^(b/2) * a^(b/2)
# (a*b) mod m = (a mod m * b mod m) mod m

# propriedade do mod evita overflow
# divide expoente pela metade

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    mod = 10**9 + 7
    
    resultado = 1
    base = a % mod
    while b > 0:
        # Se b ímpar, ultimo bit de b é 1, potencia do bit atual é base, então multiplica resultado por base
        # exemplo: b = 13 (1101) = base^8 * base^4 * base^1 (8+4+1) 
        if b % 2 == 1:
            resultado = (resultado * base) % mod
        base = (base * base) % mod # atualiza base pra proxima potencia de 2 (a = 5, b = 13, base = 5^(2^0), 5^(2^1), 5^(2^2), 5^(2^3))
        b //= 2                    # desloca o bit para a esquerda
    print(resultado)