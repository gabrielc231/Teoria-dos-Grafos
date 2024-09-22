from GrafoMatriz import Grafo

def TesteOrdenacaoTopologica():
    # Criando o grafo com base nos exemplos do material
    grafo = Grafo(8)
    grafo.insereA(0, 1)
    grafo.insereA(0, 2)
    grafo.insereA(0, 4)
    grafo.insereA(1, 3)
    grafo.insereA(1, 4)
    grafo.insereA(2, 5)
    grafo.insereA(2, 6)
    grafo.insereA(3, 7)
    grafo.insereA(4, 7)
    grafo.insereA(5, 4)
    grafo.insereA(5, 6)
    grafo.insereA(6, 7)

    grafo2 = Grafo(4)
    grafo.insereA(0, 1)
    grafo.insereA(1, 2)
    grafo.insereA(2, 3)
    grafo.insereA(3, 1)

    # Executando a ordenação topológica
    print("grafo")
    resultado = grafo.ordenacaoTopologica()

    if resultado:
        print("Ordenação Topológica:", resultado)
    
    print("grafo2")    
    resultado2 = grafo2.ordenacaoTopologica()

    if resultado2:
        print("Ordenação Topológica:", resultado2)