import itertools
def fala_verdade(pessoa, mundo):
    if mundo[pessoa] == "divina":
        return True
    elif mundo[pessoa] == "maligna":
        return False
    elif mundo[pessoa] == "humana":
        return mundo["tempo"] == "dia"
    elif mundo[pessoa] == "mentirosa":
        return False
    return False

def declaracao_consist(alvo, tem_neg, tipo_afirmado, mundo):
    if alvo == "Tempo":
        valor = (mundo["tempo"] == tipo_afirmado)
        return not valor if tem_neg else valor
    
    if tipo_afirmado in ["divina", "maligna", "humana"]:
        valor = (mundo[alvo] == tipo_afirmado)
        return not valor if tem_neg else valor
    
    if tipo_afirmado == "mentirosa":
        valor = not fala_verdade(alvo, mundo)
        return not valor if tem_neg else valor

    return False

def resolve():
    num_conversas = 1
    
    while True:
        num_declaracoes = int(input())
        if num_declaracoes == 0:
            break
        
        declaracoes = []
        nomes = set()
        for _ in range(num_declaracoes):
            frase = input().strip()
            locutora, texto = frase.split(":", 1)
            locutora = locutora.strip()
            texto = texto.strip().rstrip(".")
            
            texto = texto.replace("estou mentindo", "sou mentirosa")

            # Identifica declaração
            if texto.startswith("É "):
                atributo = texto.split()[1] # dia ou noite
                declaracoes.append((locutora, 'Tempo', False, atributo))
            else:
                palavras = texto.split()
                sujeito = palavras[0]
                if sujeito == "Eu":
                    sujeito = locutora
                
                tem_negacao = "não" in palavras
                atributo = palavras[-1]
                declaracoes.append((locutora, sujeito, tem_negacao, atributo))

        nomes = ["Ana", "Bruna", "Carla", "Daniela", "Eduarda"]
        estados_validos = []
        
        tipos_habitantes = ['divina', 'humana', 'maligna']
        periodos = ['dia', 'noite']

        for valor_tempo in periodos:
            for combinacao_tipos in itertools.product(tipos_habitantes, repeat=len(nomes)):
                estado = {'tempo': valor_tempo}
                for i, p in enumerate(nomes):
                    estado[p] = combinacao_tipos[i]

                possivel = True
                
                # Verifica cada declaração
                for loc, suj, negacao, attr in declaracoes:
                    locutora_mentindo = not fala_verdade(loc, estado)
                    declaracao_verdadeira = declaracao_consist(suj, negacao, attr, estado)
                    
                    # Se quem fala mente, declaração falsa.
                    # Se quem fala diz verdade, declaração verdadeira.
                    if locutora_mentindo == declaracao_verdadeira: 
                        possivel = False
                        break
                        
                if possivel:
                    estados_validos.append(estado)

        # Imprime os resultados no formato esperado
        print(f"Conversa #{num_conversas}")
        
        if not estados_validos:
            print("Nenhum fato pode ser deduzido.")
        else:
            fatos_deduzidos = []
            
            # Habitantes
            for p in nomes:
                primeiro_tipo = estados_validos[0][p]
                if all(est[p] == primeiro_tipo for est in estados_validos):
                    fatos_deduzidos.append(f"{p} é {primeiro_tipo}.")
            
            # Deduz se é dia ou noite
            primeiro_tempo = estados_validos[0]['tempo']
            if all(est['tempo'] == primeiro_tempo for est in estados_validos):
                fatos_deduzidos.append(f"É {primeiro_tempo}.")
                
            if not fatos_deduzidos:
                print("Nenhum fato pode ser deduzido.")
            else:
                for fato in fatos_deduzidos:
                    print(fato)
                    
        print()
        num_conversas += 1


resolve()