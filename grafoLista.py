import os
from tkinter import messagebox
import unicodedata
from pilha import Pilha
from filaCircular import FilaCircular




def is_file_of_type(file_path, extension):
    return os.path.splitext(file_path)[1].lower() == extension.lower()

def SelectFile(Type:str):   
    import tkinter as tk
    from tkinter import filedialog
    file_path= ""
    flag=0
    
    # Function to open a file dialog and display the selected file path
    def select_file():
        globals()["file_path"] = filedialog.askopenfilename(filetypes=[("x", Type)])
        
        if is_file_of_type(  globals()["file_path"],Type):
            file_label.config(text=  globals()["file_path"])# Update label with the selected file path
            
            flag=1
            
        else:
            messagebox.showerror("Arquivo invalido!", "Escolha um Arquivo do tipo:"+Type)
    def confirmar():
        if is_file_of_type(  globals()["file_path"],Type):
         root.destroy()
            
        elif file_path== "":
            messagebox.showerror("Nenhum arquivo selecionado", "Escolha um Arquivo do tipo antes de confirmar:")
        else:
            messagebox.showerror("Arquivo invalido!", "Escolha um Arquivo do tipo:"+Type)

    # Create the main application window
    root = tk.Tk()
    root.title("File Selector")
    root.geometry("400x200")  # Set the window size

    # Create a label to display the file path
    file_label = tk.Label(root, text="No file selected")
    file_label.pack(pady=20)

    # Create a button to open the file dialog
    select_button = tk.Button(root, text="Selecionar documento", command=select_file)
    select_button2 = tk.Button(root, text="Confirmar", command=confirmar)
    select_button.pack(pady=10)
    select_button2.pack(pady=10)

    
    root.mainloop()
    return  globals()["file_path"]

def extrair_palavras(caminho_arquivo, encoding='utf-8'):
    """
    Extrai todas as palavras de um arquivo de texto, considerando acentos e outros símbolos,
    onde cada palavra está separada por uma nova linha.

    :param caminho_arquivo: O caminho para o arquivo de texto.
    :param encoding: O encoding do arquivo (padrão é 'utf-8').
    :return: Uma lista de palavras extraídas do arquivo.
    """
    palavras = []

    try:
        with open(caminho_arquivo, 'r', encoding=encoding) as arquivo:
            linhas = arquivo.readlines()

        # Processar cada linha para extrair e normalizar palavras
        for linha in linhas:
            palavra = linha.strip()  # Remove espaços em branco extras
            if palavra:  # Verifica se a linha não está vazia
                palavra_normalizada = unicodedata.normalize('NFKD', palavra)
                palavra_minuscula = palavra_normalizada.lower() 
                palavras.append( palavra_minuscula)

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except UnicodeDecodeError:
        print(f"Erro ao decodificar o arquivo com o encoding: {encoding}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

    return palavras

def palavras():
    caminho= SelectFile(".txt")
    teste =  extrair_palavras(caminho)
    return teste  











#funcoes de apoio para leitura de txt









class GrafoLista:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]
        
	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        self.listaAdj[v].append(w)
        self.m+=1
     
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        self.listaAdj[v].remove(w)
        self.m-=1
        
	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a LISTA de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                print(f"{val:2d}", end="") 

        print("\n\nfim da impressao do grafo." )
    
    #um método que recebe um grafo armazenado em lista de adjacência e inverta a lista de adjacência de todos os vértices do grafo EXE 19
    def inverter_listas_adjacencia(self):
       
        for i in range(self.n):
            self.listaAdj[i].reverse()
    #auxiliar das funcoes de verificacao 
    def grau_saida(self, vertice):
        
        if vertice < self.n:
            return len(self.listaAdj[vertice])
        else:
            raise ValueError("Índice de vértice inválido")
    #auxiliar das funcoes de verificacao 
    def grau_entrada(self, vertice):
       
        if vertice < self.n:
            grau = 0
            for lista in self.listaAdj:
                if vertice in lista:
                    grau += 1
            return grau
        else:
            raise ValueError("Índice de vértice inválido")
    # um método que receba um grafo e um vértice como parâmetro e retorne 1 se vértice for uma fonte EXE 20
    def verificar_fonte(self, vertice):
       
        if vertice < self.n:
            if self.grau_saida(vertice) > 0 and self.grau_entrada(vertice) == 0:
                return 1
            else:
                return 0
        else:
            raise ValueError("Índice de vértice inválido")
    # Escreva um método que receba um grafo e um vértice como parâmetro, retorne 1 se vértice for um sorvedouro  EXE 21
    def verificar_sorvedor(self, vertice):
       
        if vertice < self.n:
            if self.grau_entrada(vertice) > 0 and self.grau_saida(vertice) == 0:
                return 1
            else:
                return 0
        else:
            raise ValueError("Índice de vértice inválido")
    

    # escreva um método que receba um grafo dirigido como parâmetro e retorna 1 se o grafo for simétrico EXE22
    def verificar_simetria(self):
       
        for u in range(self.n):
            for v in self.listaAdj[u]:
                
                if u not in self.listaAdj[v]:
                    return 0
        return 1
    # Escreva um método que receba um grafo dirigido como parâmetro e retorna 1 se o grafo for simétrico  EXE 23
    def Cria_Grafo_Por_Txt3(self , caminho):
    
        info =  extrair_palavras(caminho)
        x = 0
       
        gra = GrafoLista(int(info[0]))
        y = int(info[1])
        for x in range(2,int(info[1])+2):
           gra.insereA(int(info[x][0]),int(info[x][2]))
        return gra
    def ler(nomeArquivo):
        arq = open(nomeArquivo)
        linhas = arq.readlines()
        n = int(linhas[0])
        m = int(linhas[1])
        
        novo = GrafoLista(n)

        for i in range(2,m+2):
            v, w = linhas[i].split(" ")
            novo.insereA(int(v),int(w))
        
        arq.close()
        return novo
    # Fazer um método que permita remover um vértice do Grafo (não dirigido). EXE 24 e
    def removeV(self, vertice):
        # Remove um vértice e todas as arestas associadas a ele
        if vertice >= self.n:
            raise ValueError("Índice de vértice inválido")

        # Remove o vértice da lista de adjacência de todos os outros vértices
        for i in range(self.n):
            if vertice in self.listaAdj[i]:
                self.listaAdj[i].remove(vertice)
        
        # Remove o vértice da lista de adjacência
        self.listaAdj.pop(vertice)
        
        # Atualiza o número de vértices
        self.n-= 1
    # Fazer um método que verifique se o grafo (dirigido ou não) é completo. EXE 26
    def verificar_completude_dirigido(self):
        
        for i in range(self.n):
            
            if len(self.listaAdj[i]) != self.n - 1:
                return 0
        return 1
    
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
                for w in reversed(self.listaAdj[vAtual]):  # Itera sobre os vértices adjacentes na ordem inversa
                    if not visitado[w]:
                        p.push(w)
    
    def percurso_largura(self, v):
        fila = FilaCircular()
        visitado = [False] * self.n  # Vetor de controle de vértices visitados
        
        # Marca o vértice inicial como visitado e o adiciona à fila
        visitado[v] = True
        fila.enqueue(v)
        
        while not fila.isEmpty():
            # Remove o vértice da frente da fila
            vAtual = fila.dequeue()
            print(f"Visitando o vértice {vAtual}")
            
            # Percorre os vizinhos de vAtual
            for adj in self.listaAdj[vAtual]:
                if not visitado[adj]:
                    visitado[adj] = True
                    fila.enqueue(adj)

class TGrafoListaND:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]
        
	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        if w not in self.listaAdj[v]:
            self.listaAdj[v].append(w)
            self.listaAdj[w].append(v)
        self.m+=1
     
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        self.listaAdj[v].remove(w)
        self.listaAdj[w].remove(v)
        self.m-=1
        
	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a LISTA de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                print(f"{val:2d}", end="") 

        print("\n\nfim da impressao do grafo." )
    
    #um método que recebe um grafo armazenado em lista de adjacência e inverta a lista de adjacência de todos os vértices do grafo EXE 19
    def inverter_listas_adjacencia(self):
       
        for i in range(self.n):
            self.listaAdj[i].reverse()
    #auxiliar das funcoes de verificacao 
    def grau_saida(self, vertice):
        
        if vertice < self.n:
            return len(self.listaAdj[vertice])
        else:
            raise ValueError("Índice de vértice inválido")
    #auxiliar das funcoes de verificacao 
    def grau_entrada(self, vertice):
       
        if vertice < self.n:
            grau = 0
            for lista in self.listaAdj:
                if vertice in lista:
                    grau += 1
            return grau
        else:
            raise ValueError("Índice de vértice inválido")
    # um método que receba um grafo e um vértice como parâmetro e retorne 1 se vértice for uma fonte EXE 20
    def verificar_fonte(self, vertice):
       
        if vertice < self.n:
            if self.grau_saida(vertice) > 0 and self.grau_entrada(vertice) == 0:
                return 1
            else:
                return 0
        else:
            raise ValueError("Índice de vértice inválido")
    # Escreva um método que receba um grafo e um vértice como parâmetro, retorne 1 se vértice for um sorvedouro  EXE 21
    def verificar_sorvedor(self, vertice):
       
        if vertice < self.n:
            if self.grau_entrada(vertice) > 0 and self.grau_saida(vertice) == 0:
                return 1
            else:
                return 0
        else:
            raise ValueError("Índice de vértice inválido")
    

    # escreva um método que receba um grafo dirigido como parâmetro e retorna 1 se o grafo for simétrico EXE22
    def verificar_simetria(self):
       
        for u in range(self.n):
            for v in self.listaAdj[u]:
                
                if u not in self.listaAdj[v]:
                    return 0
        return 1
    # Escreva um método que receba um grafo dirigido como parâmetro e retorna 1 se o grafo for simétrico  EXE 23
    def Cria_Grafo_Por_Txt3(self , caminho):
    
        info =  extrair_palavras(caminho)
        x = 0
       
        gra = GrafoLista(int(info[0]))
        y = int(info[1])
        for x in range(2,int(info[1])+2):
           gra.insereA(int(info[x][0]),int(info[x][2]))
        return gra
    def ler(nomeArquivo):
        arq = open(nomeArquivo)
        linhas = arq.readlines()
        n = int(linhas[0])
        m = int(linhas[1])
        
        novo = TGrafoListaND(n)

        for i in range(2,m+2):
            v, w = linhas[i].split(" ")
            novo.insereA(int(v),int(w))
        
        arq.close()
        return novo
    # Fazer um método que permita remover um vértice do Grafo (não dirigido). EXE 24 e
    def removeV(self, vertice):
        # Remove um vértice e todas as arestas associadas a ele
        if vertice >= self.n:
            raise ValueError("Índice de vértice inválido")

        # Remove o vértice da lista de adjacência de todos os outros vértices
        for i in range(self.n):
            if vertice in self.listaAdj[i]:
                self.listaAdj[i].remove(vertice)
        
        # Remove o vértice da lista de adjacência
        self.listaAdj.pop(vertice)
        
        # Atualiza o número de vértices
        self.n-= 1
    # Fazer um método que verifique se o grafo (dirigido ou não) é completo. EXE 26
    def verificar_completude_dirigido(self):
        
        for i in range(self.n):
            
            if len(self.listaAdj[i]) != self.n - 1:
                return 0
        return 1
    
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
                for w in reversed(self.listaAdj[vAtual]):  # Itera sobre os vértices adjacentes na ordem inversa
                    if not visitado[w]:
                        p.push(w)
    
    def percurso_largura(self, v):
        fila = FilaCircular()
        visitado = [False] * self.n  # Vetor de controle de vértices visitados
        
        # Marca o vértice inicial como visitado e o adiciona à fila
        visitado[v] = True
        fila.enqueue(v)
        
        while not fila.isEmpty():
            # Remove o vértice da frente da fila
            vAtual = fila.dequeue()
            print(f"Visitando o vértice {vAtual}")
            
            # Percorre os vizinhos de vAtual
            for adj in self.listaAdj[vAtual]:
                if not visitado[adj]:
                    visitado[adj] = True
                    fila.enqueue(adj)