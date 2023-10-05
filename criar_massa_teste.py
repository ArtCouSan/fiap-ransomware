import os
import random
import string

# Nome da pasta onde você deseja criar os arquivos
pasta = "massa_teste"

# Crie a pasta se ela não existir
if not os.path.exists(pasta):
    os.makedirs(pasta)

# Número de arquivos que você deseja criar
num_arquivos = 5

# Tamanho máximo do conteúdo de cada arquivo (em caracteres)
tamanho_maximo = 1000

for i in range(num_arquivos):
    # Gere um nome de arquivo aleatório
    nome_arquivo = f"arquivo_{i + 1}.txt"
    
    # Gere conteúdo aleatório para o arquivo
    conteudo = f'Massa bla bla bla {i + 1}'

    # Caminho completo para o arquivo
    caminho_arquivo = os.path.join(pasta, nome_arquivo)
    
    # Escreva o conteúdo no arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

print(f"{num_arquivos} arquivos foram criados na pasta '{pasta}'.")
