VIDA_MAX = 1000

def trata_evento(evento, qtd, vida):
    if evento == 'DMG':
        vida -= qtd
    if evento == 'POISON':
        vida *= 1-qtd
    if evento == 'HEAL':
        vida += qtd
    if evento == 'BLESS':
        vida *= 1+qtd

    return vida

def sobrevive(vida, eventos, vals):
    erro = 1e-8 # para corrigir erro de arredondamento float
    for i in range(len(eventos)):
        vida = trata_evento(eventos[i], vals[i], vida)
        vida = min(vida, VIDA_MAX)
        if vida <= erro:
            return False
    return True

T = int(input())

for _ in range(T):
    # num de eventos
    E = int(input())

    eventos = []
    vals = []

    for _ in range(E):
        evento, qtd = input().split()
        eventos.append(evento)
        vals.append(float(qtd))

    l = 1           # equivale a 0.001
    h = 1000000     # equivale a 1000.000
    menor_resp = 1000000

    while l <= h:
        meio = (h+l) // 2
        vida_teste = meio / 1000.0  # converte float p simular
        if sobrevive(vida_teste, eventos, vals):
            menor_resp = meio
            h = meio-1
        else:
            l = meio+1
    
    print(f'{menor_resp / 1000.0:.3f}')