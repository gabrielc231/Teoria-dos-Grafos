from filaCircular import FilaCircular
from pilha import Pilha
from grafoLista import GrafoLista
from grafoLista import TGrafoListaND

class Grafo:    


    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # matriz de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.m+=1
        
        self.adj[v][w] = 1
    
    
    #insercao com espaco para rotulo/peso  EXE 16 (alem de varias  mudancas em  outras funcoes)
    def insereAV(self, v, w,valor):
        if self.adj[v][w] == 0:
            self.m+=1
        
        self.adj[v][w] = valor
           
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        if self.adj[v][w] != 0:
            self.adj[v][w]=0
            self.m = self.m - 1

    # Fazer um método que permita remover um vértice do Grafo (não dirigido e dirigido). Não se esqueça de remover as arestas associadas EXE 9 
    def removeV(self, v):
        val = len(self.adj) - 1
        for i in range(len(self.adj)):
            self.removeA(v,i)

        if v == 0 or v == len(self.adj) - 1:
            return
        
        # move elementos da matriz para cima (diminui uma linha) a partir do vertice removido
        for i in range(v,len(self.adj)-1):
            for j in range(len(self.adj[i])):
                temp = self.adj[i][j]
                self.adj[i][j] = self.adj[i+1][j]
                self.adj[i+1][j] = temp

        # move elemntos da matriz para esquerda (diminui uma coluna) a partir do vertice removido
        for i in range(len(self.adj)):
            for j in range(v,len(self.adj[i]) - 1):
                temp = self.adj[i][j]
                self.adj[i][j] = self.adj[i][j+1]
                self.adj[i][j+1]
        
        #reduz numero de vertices:
        self.n -= 1

        # cria nova matriz com numero de linhas e colunas (vertices) menor
        nova = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
                for j in range(self.n):
                    nova[i][j] = self.adj[i][j]

        #define a nova lista como self.adj
        self.adj = nova



    # Escreva um método “int inDegree(int v)” que calcula e retorna o grau de entrada de um vértice v de um grafo dirigido EXE 1 
    def in_degree(self, v):
        if v < 0 :
            raise ValueError("Vértice inválido")
        
        grau_entrada = 0
        for i in range(self.n):
            if self.adj[i][v] != 0:
                grau_entrada += 1
        
        return grau_entrada
    # Escreva o método outDegree(int v) que calcula o grau de saída de v em grafo dirigido. O método deve ser implementado na classe TGrafo  EXE 2     
    def out_degree(self, v):
        if v < 0:
            raise ValueError("Vértice inválido")
        
        grau_saida = 0
        for j in range(self.n):
            if self.adj[v][j] != 0:
                grau_saida += 1
        
        return grau_saida
    # Escreva um método para um grafo direcionado que recebe um vértice como parâmetro e retorne 1 se vértice for uma fonte  EXE 3
    def verificar_fonte(self, v):
        entrada  = self.in_degree(v)
        saida = self.out_degree(v)
        if entrada == 0 and saida > 0 : 
            return 1 
        else: 
            return 0 
    # Escreva um método para um grafo direcionado que recebe um vértice como parâmetro, retorne 1 se vértice for um sorvedouro EXE 4 
    def verificar_sorvedouro(self,v):
        entrada  = self.in_degree(v)
        saida = self.out_degree(v)
        if saida == 0 and entrada > 0 : 
            return 1 
        else: 
            return 0 
    # Escreva um método que receba um grafo dirigido como parâmetro e retorna 1 se o grafo for simétrico e 0 caso contrário EXE 5
    def verificar_simetria(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != self.adj[j][i]:
                    return 0
        return 1
    # Fazer um método que verifique e retorne e o grafo (dirigido) é completo 11
    def isCompleto(self):
        for i in range(len(self.adj)):
            for j in range(len(self.adj[i])):
                if i == j:
                    continue
                if self.adj[i][j] == 0:
                    return False
        return True 
    # Escreva um método que receba um nome de arquivo com o formato acima e construa a representação do grafo como matriz de adjacência. EXE 6 

    def ler(nomeArquivo):
        arq = open(nomeArquivo)
        linhas = arq.readlines()
        n = int(linhas[0])
        m = int(linhas[1])
        
        novo = Grafo(n)

        for i in range(2,m+2):
            v, w = linhas[i].split(" ")
            novo.insereA(int(v),int(w))
        
        arq.close()
        return novo
    
    def ler(nomeArquivo):
        arq = open(nomeArquivo)
        linhas = arq.readlines()
        n = int(linhas[0])
        m = int(linhas[1])
        
        novo = Grafo(n)

        for i in range(2,m+2):
            v, w = linhas[i].split(" ")
            novo.insereA(int(v),int(w))
        
        arq.close()
        return novo

    """ def Cria_Grafo_Por_Txt(self,caminho):
        
    
        
        info =  extrair_palavras(caminho)
        x = 0
       
        gra = Grafo(int(info[0]))
        y = int(info[1])
        for x in range(2,int(info[1])+2):
           gra.insereA(int(info[x][0]),int(info[x][2]))
        return gra """
    
    def percurso_profundidade(self, v):
        visitado = [False] * self.n  # Array para marcar os vértices visitados
        p = Pilha()  # Instancia a pilha
        p.push(v)  # Empilha o vértice inicial

        while not p.isEmpty():
            vAtual = p.pop()  # Desempilha o vértice atual

            if not visitado[vAtual]:  # Verifica se o vértice já foi visitado
                print(f"Visitando o vértice {vAtual}")
                visitado[vAtual] = True  # Marca o vértice como visitado

                # Adiciona todos os vértices adjacentes não visitados na pilha, na ordem inversa
                for w in range(self.n - 1, -1, -1):  # Itera de n-1 até 0
                    if self.adj[vAtual][w] == 1 and not visitado[w]:
                        p.push(w)

    def percurso_largura(self, v):
        visitado = [False] * self.n  # Array para marcar os vértices visitados
        f = FilaCircular()  # Instancia a fila circular
        f.enqueue(v)  # Enfileira o vértice inicial
        visitado[v] = True  # Marca o vértice inicial como visitado

        while not f.isEmpty():
            vAtual = f.dequeue()  # Remove o vértice da fila
            print(f"Visitando o vértice {vAtual}")

            # Adiciona todos os vértices adjacentes não visitados na fila
            for w in range(self.n):
                if self.adj[vAtual][w] == 1 and not visitado[w]:
                    f.enqueue(w)
                    visitado[w] = True  # Marca o vértice adjacente como visitado

    #funcao de apoio para categoria conexidade
    def percurso_profundidade3(self, v, visitado, grafo):
        p = Pilha()  # Instancia a pilha
        p.push(v)  # Empilha o vértice inicial

        while not p.isEmpty():
            vAtual = p.pop()  # Desempilha o vértice atual

            if not visitado[vAtual]:  # Verifica se o vértice já foi visitado
                visitado[vAtual] = True  # Marca o vértice como visitado

                # Adiciona todos os vértices adjacentes não visitados na pilha, na ordem inversa
                for w in range(self.n - 1, -1, -1):  # Itera de n-1 até 0
                    if grafo[vAtual][w] == 1 and not visitado[w]:
                        p.push(w)

    #funcao de apoio para categoria conexidade
    def eh_conectado_forte(self):
        # Verifica se o grafo é fortemente conexo
        for start in range(self.n):
            visited = [False] * self.n
            self.percurso_profundidade3(start, visited, self.adj)
            if not all(visited):
                return False

        # Inverte o grafo para verificar a conectividade reversa
        adj_reversa = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != 0 :
                    adj_reversa[j][i] = 1
        
        for start in range(self.n):
            visited = [False] * self.n
            self.percurso_profundidade3(start, visited, adj_reversa)
            if not all(visited):
                return False

        return True
    #funcao de apoio para categoria conexidade
    def eh_conectado_fraco(self):
        # Converte o grafo direcionado para não direcionado
        adj_nao_direcionado = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] == 1 or self.adj[j][i] == 1:
                    adj_nao_direcionado[i][j] = 1
                    adj_nao_direcionado[j][i] = 1
        
        # Verifica se o grafo não direcionado é conexo
        visited = [False] * self.n
        self.percurso_profundidade3(0, visited, adj_nao_direcionado)
        return all(visited)
    #funcao de apoio para categoria conexidade
    def eh_conectado_minimo(self):
        # Verifica se o grafo é conectado em um sentido mínimo, não fortemente nem fracamente
        for start in range(self.n):
            visited = [False] * self.n
            self.percurso_profundidade3(start, visited, self.adj)
            if any(not visited[i] for i in range(self.n) if i != start):
                return True
        return False
    #funcao de apoio para categoria conexidade
    def eh_desconectado(self):
        # Verifica se o grafo não é nem fortemente nem fracamente conexo
        return not (self.eh_conectado_forte() or self.eh_conectado_fraco())
    # Fazer um método que retorne a categoria de conexidade para um grafo direcionado (3 – C3, 2 – C2, 1 – C1 ou 0 – c0) EXE 14
    def categoria_conexidade(self):
        if self.eh_conectado_forte():
            return 3  # C3 - fortemente conexo
        elif self.eh_conectado_fraco():
            return 2  # C2 - Semifortemente conexo
        elif self.eh_conectado_minimo():
            return 1  # C1 - simplesmente conexo
        else:
            return 0  # C0 - Desconectado






	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
                    print(f"Adj[{i:2d},{w:2d}] = "+str(self.adj[i][w])+" ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )


	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
                    print(" "+str(self.adj[i][w]) +" ", end="") 
                else:
                    print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )
    # Fazer um método que retorne o complemento (grafo complementar) de um grafo (dirigido) na forma de uma matriz de adjacência EXE 12
    def complemento(self):
        n = len(self.adj)
        complemento = TGrafoND(self.n)
        complemento.adj = [[1 for i in range(n)] for j in range(n)]
        


        for i in range(n):
            complemento.adj[i][i] = 0  # Os laços não existem no complemento
            for j in range(n):
                if self.adj[i][j] != 0:
                    complemento.adj[i][j] = 0
                     # Para grafos não dirigidos

        return complemento
    #Funcao de apoio de Reduzido
    def dfss(self, v, visited, stack, graph):
        visited[v] = True
        for neighbor in range(self.n):
            if graph[v][neighbor] != 0 and not visited[neighbor]:
                self.dfss(neighbor, visited, stack, graph)
        stack.append(v)
    #Funcao de apoio de Reduzido
    def get_transposed_graph(self):
        transposed = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != 0:
                    transposed[j][i] = 1
        return transposed
    #Funcao de apoio de Reduzido
    def kosaraju_scc(self):
        # Step 1: Fill vertices in stack according to their finishing time
        stack = []
        visited = [False] * self.n
        for i in range(self.n):
            if not visited[i]:
                self.dfss(i, visited, stack, self.adj)
        
        # Step 2: Get the transposed graph
        transposed = self.get_transposed_graph()
        
        # Step 3: Process all vertices in order defined by stack
        scc = []
        visited = [False] * self.n
        while stack:
            node = stack.pop()
            if not visited[node]:
                component_stack = []
                self.dfss(node, visited, component_stack, transposed)
                scc.append(component_stack)
        
        return scc
    #Funcao de apoio de Reduzido
   
    def construir_grafo_reduzido(self, scc):
        
            scc_map = {}
            for index, component in enumerate(scc):
                for node in component:
                    scc_map[node] = index
        
        # Cria o grafo reduzido
            num_scc = len(scc)
            grafo_reduzido = Grafo(num_scc)

        # Preenche a matriz de adjacência para o grafo reduzido
            for i in range(self.n):
                for j in range(self.n):
                    if self.adj[i][j] == 1:
                        scc_i = scc_map[i]
                        scc_j = scc_map[j]
                        if scc_i != scc_j:
                            grafo_reduzido.insereA(scc_i, scc_j)
        
            return grafo_reduzido
# um método que retorne o grafo reduzido de um grafo direcionado no formato de uma matriz de adjacência EXE 15 
    def reduzido(self):
        scc = self.kosaraju_scc()
        return self.construir_grafo_reduzido(scc)
# Escreva um método que decida se dois grafos direcionados são iguais. O método deve ser implementado para a classe TGrafo faz uso da lista de adjacência EXE 17
    def iguais(self, outro_grafo):
        # Verifica se os grafos são iguais
        
        if self.n != outro_grafo.n:
            return False
        
        for v in range(self.n):
            if self.adj[v] != outro_grafo.adj[v]:
                return False
        
        return True
# Escreva um método que converta uma representação de um grafo em outra. Por exemplo, converta um grafo armazenado em matriz de adjacência em uma lista de adjacência EXE 18
    def matriz_para_lista(self):
        # Cria uma lista de adjacência vazia para cada vértice
        lista = GrafoLista(self.n)
        
        
        
        
        # Preenche a lista de adjacência com base na matriz de adjacência
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != 0:
                    lista.insereA(i,j)
        
        return lista
    # Método para realizar a ordenação topológica
    def ordenacaoTopologica(self):
        # Calcula o grau de entrada para cada nó
        grau_entrada = [0] * self.n
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[j][i] == 1:
                    grau_entrada[i] += 1

        # Inicializa a fila circular com todos os nós com grau de entrada zero
        fila = FilaCircular(self.n)  # Tamanho da fila é o número de nós
        for i in range(self.n):
            if grau_entrada[i] == 0:
                fila.enqueue(i)

        resultado = []

        while not fila.isEmpty():
            u = fila.dequeue()  # Remove o nó da frente da fila
            resultado.append(u)

            # Reduz o grau de entrada dos nós adjacentes
            for v in range(self.n):
                if self.adj[u][v] == 1:
                    grau_entrada[v] -= 1
                    if grau_entrada[v] == 0:
                        fila.enqueue(v)

        # Verifica se existe ciclo no grafo
        if len(resultado) != self.n:
            print("O grafo contém um ciclo, logo não pode ser ordenado topologicamente.")
        else:
            return resultado
            
    def dijkstra(self, origem):
        # Inicializa as distâncias e a lista de visitados
        dist = [float('inf')] * self.n
        dist[origem] = 0
        visitado = [False] * self.n

        for _ in range(self.n):
            # Encontra o vértice não visitado com a menor distância
            u = self.encontrar_min_dist(dist, visitado)

            if u is None:  # Caso todos os vértices tenham sido visitados
                break

            visitado[u] = True

            # Atualiza as distâncias dos vizinhos
            for v in range(self.n):
                if self.adj[u][v] != 0 and not visitado[v]:  # Verifica se existe uma aresta e o vértice não foi visitado
                    nova_dist = dist[u] + self.adj[u][v]
                    if nova_dist < dist[v]:
                        dist[v] = nova_dist

        return dist

    def encontrar_min_dist(self, dist, visitado):
        min_dist = float('inf')
        min_index = None
        for v in range(self.n):
            if not visitado[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_index = v
        return min_index

#	Criar uma outra classe TGrafoND e modifique as funções insereA, removeA e show para representar um grafo não-dirigido  EXE 7 
class TGrafoND:
    
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # matriz de adjacência
        self.adj = [[0 for i in range(n)] for j in range(n)]

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w ) :
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.adj[w][v] = 1
            self.m+=1 # atualiza qtd arestas
    #	insercao com valor para 8 permitir a criação de um grafo não direcionado rotulado EXE 8 (alem de mudancas em outras funcoes )
    def insereAV(self, v, w,valor):
        if self.adj[v][w] == 0:
            self.m+=1
        self.adj[v][w] = valor
        self.adj[w][v] = valor
          
    
    # remove uma aresta v->w do Grafo	
    def removeA(self, v,w):
        if self.adj[v][w] != 0:
            self.adj[v][w]=0
            self.adj[w][v]=0
            self.m = self.m - 1
    
    def removeV(self, v):
        val = len(self.adj) - 1
        for i in range(len(self.adj)):
            self.removeA(v,i)

        if v == 0 or v == len(self.adj) - 1:
            return
        
        # move elementos da matriz para cima (diminui uma linha) a partir do vertice removido
        for i in range(v,len(self.adj)-1):
            for j in range(len(self.adj[i])):
                temp = self.adj[i][j]
                self.adj[i][j] = self.adj[i+1][j]
                self.adj[i+1][j] = temp

        # move elemntos da matriz para esquerda (diminui uma coluna) a partir do vertice removido
        for i in range(len(self.adj)):
            for j in range(v,len(self.adj[i]) - 1):
                temp = self.adj[i][j]
                self.adj[i][j] = self.adj[i][j+1]
                self.adj[i][j+1]
        
        #reduz numero de vertices:
        self.n -= 1

        # cria nova matriz com numero de linhas e colunas (vertices) menor
        nova = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
                for j in range(self.n):
                    nova[i][j] = self.adj[i][j]

        #define a nova lista como self.adj
        self.adj = nova


    
    #exe 1
    def in_degree(self, v):
        if v < 0 :
            raise ValueError("Vértice inválido")
        
        grau_entrada = 0
        for i in range(self.n):
            if self.adj[i][v] == 1:
                grau_entrada += 1
        
        return grau_entrada
    #exe 2
    def out_degree(self, v):
        if v < 0:
            raise ValueError("Vértice inválido")
        
        grau_saida = 0
        for j in range(self.n):
            if self.adj[v][j] == 1:
                grau_saida += 1
        
        return grau_saida
    #exe 3
    def verificar_fonte(self, v):
        entrada  = self.in_degree(v)
        saida = self.out_degree(v)
        if entrada == 0 and saida > 0 : 
            return 1 
        else: 
            return 0 
    #exe 4
    def verificar_sorvedouro(self,v):
        entrada  = self.in_degree(v)
        saida = self.out_degree(v)
        if saida == 0 and entrada > 0 : 
            return 1 
        else: 
            return 0 
    #exe 5    
    def verificar_simetria(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.adj[i][j] != self.adj[j][i]:
                    return 0
        return 1
    # Fazer um método que verifique e retorne se o grafo (não dirigido) é completo EXE 10
    def Completo(self):
        for i in range(len(self.adj)):
            for j in range(len(self.adj[i])):
                if i == j:
                    continue
                if self.adj[i][j] == 0:
                    return False
        return True 
    # Fazer um método que retorne o complemento (grafo complementar) de um grafo ( Nao dirigido) na forma de uma matriz de adjacência EXE 12
    def complemento(self):
        n = len(self.adj)
        complemento = TGrafoND(self.n)
        complemento.adj = [[1 for i in range(n)] for j in range(n)]
        


        for i in range(n):
            complemento.adj[i][i] = 0  # Os laços não existem no complemento
            for j in range(n):
                if self.adj[i][j] == 1:
                    complemento.adj[i][j] = 0
                    complemento.adj[j][i] = 0  # Para grafos não dirigidos

        return complemento
    
    """ def Cria_Grafo_Por_Txt2(self , caminho):
    
        info =  extrair_palavras(caminho)
        x = 0
       
        gra = TGrafoND(int(info[0]))
        y = int(info[1])
        for x in range(2,int(info[1])+2):
           gra.insereA(int(info[x][0]),int(info[x][2]))
        return gra """
    
    def ler(nomeArquivo):
        arq = open(nomeArquivo)
        linhas = arq.readlines()
        n = int(linhas[0])
        m = int(linhas[1])
        
        novo = TGrafoND(n)

        for i in range(2,m+2):
            v, w = linhas[i].split(" ")
            novo.insereA(int(v),int(w))
        
        arq.close()
        return novo

    # Funcao de apoio 
    def percurso_profundidade2(self, v, visitado):
        p = Pilha()  # Instancia a pilha
        p.push(v)  # Empilha o vértice inicial

        while not p.isEmpty():
            vAtual = p.pop()  # Desempilha o vértice atual

            if not visitado[vAtual]:  # Verifica se o vértice já foi visitado
                print(f"Visitando o vértice {vAtual}")
                visitado[vAtual] = True  # Marca o vértice como visitado

                # Adiciona todos os vértices adjacentes não visitados na pilha, na ordem inversa
                for w in range(self.n - 1, -1, -1):  # Itera de n-1 até 0
                    if self.adj[vAtual][w] == 1 and not visitado[w]:
                        p.push(w)

    def percurso_profundidade(self, v):
        visitado = [False] * self.n  # Array para marcar os vértices visitados
        p = Pilha()  # Instancia a pilha
        p.push(v)  # Empilha o vértice inicial

        while not p.isEmpty():
            vAtual = p.pop()  # Desempilha o vértice atual

            if not visitado[vAtual]:  # Verifica se o vértice já foi visitado
                print(f"Visitando o vértice {vAtual}")
                visitado[vAtual] = True  # Marca o vértice como visitado

                # Adiciona todos os vértices adjacentes não visitados na pilha, na ordem inversa
                for w in range(self.n - 1, -1, -1):  # Itera de n-1 até 0
                    if self.adj[vAtual][w] == 1 and not visitado[w]:
                        p.push(w)

    def percurso_largura(self, v):
        visitado = [False] * self.n  # Array para marcar os vértices visitados
        f = FilaCircular()  # Instancia a fila circular
        f.enqueue(v)  # Enfileira o vértice inicial
        visitado[v] = True  # Marca o vértice inicial como visitado

    # Fazer um método que retorne o tipo de conexidade de um grafo não direcionado (0 - conexo ou 1 - não conexo – desconexo) EXE 13
    def eh_conectado(self):
        visited = [False] * self.n
        self.percurso_profundidade2(0, visited)
        return all(visited)
    
    def eh_conectado2(self):
        visited = [False] * self.n
        self.percurso_profundidade2(0, visited)
        if all(visited):
            return 1
        else:
            return 0

    def numero_de_componentes(self):
        visited = [False] * self.n
        num_componentes = 0
        
        for v in range(self.n):
            if  visited[v]:
                num_componentes += 1
                self.dfs(v, visited)
        
        return num_componentes

    def categoria_conexidade(self):
        if self.eh_conectado():
            return 1  # C3 - Conectado
        elif self.numero_de_componentes() > 1:
            return 1  # C1 - Desconectado
        else:
            return 0  # C0 - Desconectad
	    

	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
                    print(f"Adj[{i:2d},{w:2d}] = "+str(self.adj[i][w])+" ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )

    # Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] != 0:
                    print(" "+str(self.adj[i][w]) +" ", end="") 
                else:
                    print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )
    
    def dijkstra(self, origem):
        # Inicializa as distâncias e a lista de visitados
        dist = [float('inf')] * self.n
        dist[origem] = 0
        visitado = [False] * self.n

        for _ in range(self.n):
            # Encontra o vértice não visitado com a menor distância
            u = self.encontrar_min_dist(dist, visitado)

            if u is None:  # Caso todos os vértices tenham sido visitados
                break

            visitado[u] = True

            # Atualiza as distâncias dos vizinhos
            for v in range(self.n):
                if self.adj[u][v] != 0 and not visitado[v]:  # Verifica se existe uma aresta e o vértice não foi visitado
                    nova_dist = dist[u] + self.adj[u][v]
                    if nova_dist < dist[v]:
                        dist[v] = nova_dist

        return dist