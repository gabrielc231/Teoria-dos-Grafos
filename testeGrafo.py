import os
from tkinter import messagebox
import unicodedata
from grafoLista import GrafoLista
from grafoLista import TGrafoListaND
from grafoMatriz import Grafo
from grafoMatriz import TGrafoND




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

















g = Grafo(6)
#insere as arestas do grafo
#A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g.insereA(0,1)
g.insereA(0,2)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(1,3)
g.insereA(3,4)
g.insereA(5,3)
# mostra o grafo 

#EXERCICIO 1:

print("TESTE! 1:")
g.show()
print("Grau de entrada de 1 deveria ser 2 e a funcao retorna: "+str(g.in_degree(1)))
print("Grau de entradaree de 2 deveria ser 1 e a funcao retorna: "+str(g.in_degree(2)))
print("Grau de entradade 3 deveria ser 3 e a funcao retorna: "+str(g.in_degree(3)))
print("Grau de entradade 4 deveria ser 1 e a funcao retorna: "+str(g.in_degree(4)))
print("Grau de entradade 5 deveria ser 0 e a funcao retorna: "+str(g.in_degree(5)))
print("\n")
#EXERCICIO 2:
print("TESTE! 2:")
g.show()
print("Grau de saida 1 deveria ser 1 e a funcao retorna: "+str(g.out_degree(1)))
print("Grau de saida 2 deveria ser 2 e a funcao retorna: "+str(g.out_degree(2)))
print("Grau de saida 3 deveria ser 1 e a funcao retorna: "+str(g.out_degree(3)))
print("Grau de saida 4 deveria ser 0 e a funcao retorna: "+str(g.out_degree(4)))
print("Grau de saida 5 deveria ser 1 e a funcao retorna: "+str(g.out_degree(5)))
print("\n")
#EXERCICIO 3: 
print("TESTE! 3:")
g.show()
print("Fonte de 1 deveria ser 0 e a funcao retorna: "+str(g.verificar_fonte(1)))
print("Fonte de 2 deveria ser 0 e a funcao retorna: "+str(g.verificar_fonte(2)))
print("Fonte  de 3 deveria ser 0 e a funcao retorna: "+str(g.verificar_fonte(3)))
print("Fonte de 4 deveria ser 0 e a funcao retorna: "+str(g.verificar_fonte(4)))
print("Fonte  de 5 deveria ser 1 e a funcao retorna: "+str(g.verificar_fonte(5)))


print("\n")
#EXERCICIO 4: 
print("TESTE! 4:")
g.show()
print("sorvedouro de 1 deveria ser 0 e a funcao retorna: "+str(g.verificar_sorvedouro(1)))
print("sorvedouro de 2 deveria ser 0 e a funcao retorna: "+str(g.verificar_sorvedouro(2)))
print("sorvedouro de 3 deveria ser 0 e a funcao retorna: "+str(g.verificar_sorvedouro(3)))
print("sorvedourode 4 deveria ser 0 e a funcao retorna: "+str(g.verificar_sorvedouro(4)))
print("sorvedouro  de 5 deveria ser 1 e a funcao retorna: "+str(g.verificar_sorvedouro(5)))
print("\n")
#EXERCICIO 5: 
print("TESTE! 5:")
g.show()
print("Grafo g e simetrico ? "+str(g.verificar_simetria()))
g2 = Grafo(2) 
g2.insereA(0,1)
g2.insereA(1,0)
print("Grafo g2 e simetrico ? "+str(g2.verificar_simetria()))
#input()
#EXERCICIO 6:
print("TESTE! 6:")
#print("selecione o arquivo txt para grafo ")
#g = g.Cria_Grafo_Por_Txt(SelectFile(".txt")) 
g = Grafo.ler("TXT PARA CRIAR GRAFOS.txt")
g.show()
print("\n")
#EXERCICIO 7: 
print("TESTE! 7:")
g=TGrafoND(6)
g.insereA(0,1)
g.insereA(0,2)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(1,3)
g.insereA(3,4)
g.insereA(5,3)
g.show()
g.showMin()
print("\n")

#EXERCICIO 8: 
print("TESTE! 8:")
g= TGrafoND(6)
g.insereAV(0,1,1.2)
g.insereAV(0,2,0.1)
g.insereAV(2,1,0.5)
g.insereAV(2,3,1)
g.insereAV(1,3,0.7)
g.insereAV(3,4,0.8)
g.insereAV(5,3,0.9)
g.show()
print("\n")
#EXERCICIO 9:
print("TESTE! 9:")
g=TGrafoND(6)
g.insereA(0,1)
g.insereA(0,2)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(1,3)
g.insereA(3,4)
g.insereA(5,3)
g.removeV(3)
print("Removendo vertice 3")

g.show()
g.showMin()
print("\n")

#EXERCICIO 10: 
print("TESTE! 10:")
g = TGrafoND(4)

g.insereA(0,1)
g.insereA(0,2)
g.insereA(0,3)
g.insereA(1,2)
g.insereA(1,3)
g.insereA(1,3)
g.insereA(2,3)
g.show()
print("g e completo ? "+str(g.Completo()))
print("\n")
#input()
#EXERCICIO 11: 
print("TESTE! 11:")
g = Grafo(4)

g.insereA(0,1)
g.insereA(0,2)
g.insereA(0,3)

g.show()
g.showMin()
print("g e completo ? "+str(g.isCompleto()))
print("\n")
#EXERCICIO 12: 
print("TESTE! 12:")
g= Grafo(4)
g.insereA(0, 1)
g.insereA(0, 2)
g.insereA(0, 3)
g.show()
g.complemento().show()
print("\n")
#EXERCICIO 13: 
print("TESTE! 13:")
g = TGrafoND(2)
g.show()
print(" g tipo conexo ? " + str(g.eh_conectado2()))

print("\n")
g.insereA(0,1)
g.show()
print(" g2 tipo conexo? " + str(g.eh_conectado2()))
print("\n")
#EXERCICIO 14: 
print("TESTE! 14:")
g = Grafo(2)
g.show()
print(" nivel de g ? " + str(g.categoria_conexidade()))
g.insereA(0,1)
g.show()
print(" nivel de g ? "+  str(g.categoria_conexidade()))
g.insereA(1,0)
g.show()
print(" nivel de g ? " +  str(g.categoria_conexidade()))
print("\n")
#EXERCICIO 15: 
print("TESTE! 15:")
g = Grafo(3)
g.insereA(0,1)
g.insereA(1,0)
g.insereA(1,2)


g.show()

print("como fica esse grafo reduzido ?")
g.reduzido().show()
print("\n")
#input()
#EXERCICIO 16:
print("TESTE! 16:")
g= Grafo(6)
g.insereAV(0,1,1.2)
g.insereAV(0,2,0.1)
g.insereAV(2,1,0.5)
g.insereAV(2,3,1)
g.insereAV(1,3,0.7)
g.insereAV(3,4,0.8)
g.insereAV(5,3,0.9)
g.show()
print("\n")


#EXERCICIO 17: 
print("TESTE! 17:")
g= Grafo(6)
g2=Grafo(6)
g2.insereA(1,0)
print("G1:")
g.show()
print("------------------------------------")
print("G2:")
g2.show()
print("G1 e igual a ele mesmo ? "+str(g.iguais(g)))
print("G1 e igual a G2 ? "+str(g.iguais(g2)))
print("\n")


#EXERCICIO 18:
print("TESTE! 18:") 
g= Grafo(4)
g.insereA(1,0)
g.insereA(0,1)
g.insereA(0,2)
g.insereA(0,3)
g.insereA(3,1)
g.insereA(3,2)
print("Modo Matrix:")
g.show()
g2 = g.matriz_para_lista()
print("Modo Lista:")
g2.show()
print("\n")
#EXERCICIO 19: 
print("TESTE! 19:") 
print("lista original:")
g2.show()
print("lista invertida:")
g2.inverter_listas_adjacencia()
g2.show()
print("\n")
#EXERCICIO 20:
#input()
print("TESTE! 20:") 
g = GrafoLista(6)
#insere as arestas do grafo
#A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g.insereA(0,1)
g.insereA(0,2)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(1,3)
g.insereA(3,4)
g.insereA(5,3)
g.show()
print("Fonte de 1 deveria ser 0 e a funcao retorna: "+str(g.verificar_fonte(1)))
print("Fonte de 2 deveria ser 0 e a funcao retorna: "+str(g.verificar_fonte(2)))
print("Fonte  de 3 deveria ser 0 e a funcao retorna: "+str(g.verificar_fonte(3)))
print("Fonte de 4 deveria ser 0 e a funcao retorna: "+str(g.verificar_fonte(4)))
print("Fonte  de 5 deveria ser 1 e a funcao retorna: "+str(g.verificar_fonte(5)))
print("\n")
#EXERCICIO 21: 
print("TESTE! 21:") 
g.show()
print("sorvedor de 1 deveria ser 0 e a funcao retorna: "+str(g.verificar_sorvedor(1)))
print("sorvedor de 2 deveria ser 0 e a funcao retorna: "+str(g.verificar_sorvedor(2)))
print("sorvedor  de 3 deveria ser 0 e a funcao retorna: "+str(g.verificar_sorvedor(3)))
print("sorvedor de 4 deveria ser 1 e a funcao retorna: "+str(g.verificar_sorvedor(4)))
print("sorvedor  de 5 deveria ser 0 e a funcao retorna: "+str(g.verificar_sorvedor(5)))
print("\n")
#EXERCICIO 22: 
print("TESTE! 22:") 
g.show()
print("Grafo g e simetrico ? "+str(g.verificar_simetria()))

g2 = GrafoLista(2) 
g2.insereA(0,1)
g2.insereA(1,0)
g2.show()
print("Grafo g2 e simetrico ? "+str(g2.verificar_simetria()))
print("\n")
#EXERCICIO 23:
print("TESTE! 23:")  
print("selecione um arquivo TXT para formar o grafo!")
#g2 = g2.Cria_Grafo_Por_Txt3(SelectFile(".txt"))
g2 = GrafoLista.ler("Txt PARA CRIAR GRAFOS.txt")
g2.show()
print("\n")
#EXERCICIO 24:
print("TESTE! 24:")  
g2.show()
print("vertice 0 foi removido")
g2.removeV(0)
g2.show()
print("\n")
#EXERCICIO 25:
print("TESTE! 25:") 
g = Grafo(3)
g.insereA(1,0)
g.insereA(0,2)
g.insereA(2,0) 
g.show()
g.removeV(1)
print("vertice 1 foi removido")
g.show()
print("\n")
#input()
#EXERCICIO 26:
print("TESTE! 26:")  
g = GrafoLista(2)
g.insereA(1,0)
g.insereA(0,1)
g.show()
print("g e completo ? " + str(g.verificar_completude_dirigido()))


# Percurso

# Grafo para teste simples
sg = TGrafoListaND(3)
sg.insereA(0,1)
sg.insereA(0,2)
sg.show()

print("Percurso em profundidade:")
sg.percurso_profundidade(0)
print("\nPercurso em largura:")
sg.percurso_largura(0)

# Grafo para teste igual da aula
tg = Grafo(8)
tg.insereA(0,1)
tg.insereA(0,2)
tg.insereA(0,4)
tg.insereA(1,3)
tg.insereA(1,4)
tg.insereA(2,5)
tg.insereA(2,6)
tg.insereA(3,7)
tg.insereA(4,7)
tg.insereA(5,4)
tg.insereA(5,6)
tg.insereA(6,7)
tg.showMin()

print("Percurso em profundidade:")
tg.percurso_profundidade(0)
print("\nPercurso em largura:")
tg.percurso_largura(0)