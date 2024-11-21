from GRAFO import Grafo
def carregar_grafo_modelado(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    tipo_grafo = int(linhas[0].strip())  # Tipo do grafo (0 a 7)
    n = int(linhas[1].strip())          # Número de vértices
    m = int(linhas[2].strip())          # Número de arestas
    
    direcionado = tipo_grafo >= 4  # Grafos de 4 a 7 são direcionados
    grafo = Grafo(direcionado=direcionado)

    # Lê os vértices
    for i in range(3, 3 + n):
        linha = linhas[i].strip().split()
        id_vertice = linha[0]
        apelido = linha[0] if len(linha) > 1 else id_vertice
        peso_vertice = int(linha[1]) if tipo_grafo in [1, 3, 5, 7] else None
        vertice = grafo.addVertice(apelido)
        if peso_vertice is not None:
            vertice.peso = peso_vertice  # Adiciona peso ao vértice, se necessário

    # Lê as arestas
    for i in range(3 + n, 3 + n + m):
        linha = linhas[i].strip().split()
        id_v1, id_v2 = linha[0], linha[1]
        peso_aresta = int(linha[2]) if tipo_grafo in [2, 3, 6, 7] and len(linha) > 2 else 1
        
        # Obtém os vértices correspondentes
        v1 = grafo.getVertice(id_v1)
        v2 = grafo.getVertice(id_v2)
        
        # Adiciona a aresta ao grafo
        grafo.addAresta(v1, v2, peso=peso_aresta)

    return grafo
