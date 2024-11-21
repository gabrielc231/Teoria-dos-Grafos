from TGRAFO import TGrafo
from caminho_hamiltoniano import  HamiltonianPathFinder
from Caminho_euleriano import EulerianPathFinder
from Coloraçao import GraphColoring
from Salvar_grafo import salvar_grafo_em_txt
from grafo_visual import visualizar_grafo
from leitura_arquivo_txt import carregar_grafo_modelado
import os

def lerClips(diretorio):
        

        # Percorrer todos os arquivos e subdiretórios no diretório fornecido
        for root, dirs, files in os.walk(diretorio):
            novo =  TGrafo()
            arquivos_pessoa=[]
            arquivos_animal=[]
            arquivos_carro=[]
            tag = []
            aux=0
            for file in files:
                # Obter o caminho completo do arquivo
                caminho_arquivo = os.path.join(root, file)
                tag = []
                # Verificar se o nome do arquivo contém "Pessoa", "Animal" ou "Carro"
                flag=0
                aux+=1
                if "Pessoa" in file:
                    flag=1
                    arquivos_pessoa.append(caminho_arquivo)
                    tag.append("Pessoa")

                if "Animal" in file:
                    flag=1
                    arquivos_animal.append(caminho_arquivo)
                    tag.append("Animal")
                if "Carro" in file:
                    flag=1
                    arquivos_carro.append(caminho_arquivo)
                    tag.append("Carro")
                if(flag==0):
                    print(file)
                v= novo.addTVertice("clip" + str(aux),caminho_arquivo,tag)
            novo.conectar_all_tags()
        return novo

grafo = lerClips("clips segurança")
#grafo.print()
#print("teste")
#finder = HamiltonianPathFinder(grafo)
#finder.find_hamiltonian_path()
#finder = EulerianPathFinder(grafo)
#finder.find_eulerian_path()
#coloring = GraphColoring(grafo)
#color_map = coloring.color_graph()
#coloring.print_coloring()
#salvar_grafo_em_txt(grafo, "GRAFO.txt", tipo_grafo=1)
#grafo.print()
#carregar_grafo_modelado("GRAFO.txt")
#salvar_grafo_em_txt(grafo, "GRAFO.txt", tipo_grafo=1)
#carregar_grafo_modelado("GRAFO.txt")
#salvar_grafo_em_txt(grafo, "GRAFO.txt", tipo_grafo=1)
#visualizar_grafo(grafo)