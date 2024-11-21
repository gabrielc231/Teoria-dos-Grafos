from GRAFO import Grafo
def salvar_grafo_em_txt(grafo, caminho_arquivo, tipo_grafo):
    with open(caminho_arquivo, 'w') as arquivo:
        # Escreve o tipo do grafo
        arquivo.write(f"{tipo_grafo}\n")
        
        # Escreve o número de vértices
        arquivo.write(f"{grafo.verticesNum}\n")
        
        # Escreve o número de arestas
        arquivo.write(f"{grafo.arestasNum}\n")
        
        # Escreve os vértices
        for vertice in grafo.vertices:
            linha = f"{vertice.nome}"  # Nome do vértice
            if tipo_grafo in [1, 3, 5, 7]:  # Adiciona peso ao vértice, se aplicável
                linha += f" {vertice.peso if hasattr(vertice, 'peso') else 0}"
            linha += "\n"
            arquivo.write(linha)
        
        # Escreve as arestas
        for vertice in grafo.vertices:
            for aresta in vertice.arestas:
                v1 = aresta.vertice1.nome
                v2 = aresta.vertice2.nome
                if grafo.direcionado or (grafo.direcionado is False and vertice == aresta.vertice1):
                    linha = f"{v1} {v2}"
                    if tipo_grafo in [2, 3, 6, 7]:  # Adiciona peso à aresta, se aplicável
                        linha += f" {aresta.peso}"
                    linha += "\n"
                    arquivo.write(linha)



