import os
import secrets
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import pickle

# Gere uma chave AES de 256 bits (32 bytes)
key = secrets.token_bytes(32)

# Vetor de inicialização (IV) - deve ser diferente para cada arquivo
iv = get_random_bytes(16)

with open('chaves', 'wb') as arquivo:
    pickle.dump((key, iv), arquivo)

# Pasta que você deseja criptografar
caminho_pasta = input("Digite o caminho da pasta que deseja criptografar:")

# Listar todos os arquivos na pasta
arquivos = os.listdir(caminho_pasta)

# Inicializar o objeto AES
cipher = AES.new(key, AES.MODE_CBC, iv)

# Iterar sobre os arquivos e criptografá-los
for arquivo in arquivos:
    if os.path.isfile(os.path.join(caminho_pasta, arquivo)):
        with open(os.path.join(caminho_pasta, arquivo), 'rb') as arquivo_original:
            dados = arquivo_original.read()
            dados = dados + b' ' * (16 - len(dados) % 16)
            dados_criptografados = cipher.encrypt(dados)
        with open(os.path.join(caminho_pasta, arquivo), 'wb') as arquivo_criptografado:
            arquivo_criptografado.write(dados_criptografados)