# Num de casos de teste
cases = int(input())

for _ in range(cases):
    # Eixo X
    x = 0
    moves = []
    
    # Num de instrucoes
    num_inst = int(input())
    for i in range(num_inst):
        instrucao = input().split()
        move = instrucao[0]
        
        if move == "ESQUERDA":
            desloca = -1
        if move == "DIREITA":
            desloca = 1
        if move == "REPETE":
            num = int(instrucao[1])
            desloca = moves[num]
        
        moves.append(desloca)
        x += desloca
        
    print(f"{x}")