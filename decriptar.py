import os
from Crypto.Cipher import AES
import pickle
import tkinter as tk
from tkinter import messagebox


def show_encryption_message():
    root = tk.Tk()
    root.attributes('-topmost', True)  # Traz a janela para o primeiro plano
    root.withdraw()  # Esconde a janela principal do tkinter
    messagebox.showwarning("ATENÇÃO", "Todos os seus arquivos foram descriptografados")
    root.destroy()


def descriptografar(caminho_pasta, chave_arquivo):
    # Listar todos os arquivos na pasta
    arquivos = os.listdir(caminho_pasta)

    # Abre o arquivo em modo de leitura de binario ('rb')
    with open(chave_arquivo, "rb") as arquivo:
        key, iv = pickle.load(arquivo)

    # Inicializar o objeto AES para descriptografia
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Iterar sobre os arquivos e descriptografá-los
    for arquivo in arquivos:
        if os.path.isfile(os.path.join(caminho_pasta, arquivo)):
            with open(os.path.join(caminho_pasta, arquivo), 'rb') as arquivo_criptografado:
                dados_criptografados = arquivo_criptografado.read()

            # Descriptografar os dados
            dados_descriptografados = cipher.decrypt(dados_criptografados)

            # Remover o preenchimento (padding) adicionado durante a criptografia
            dados_descriptografados = dados_descriptografados.rstrip(b' ')

            # Escrever os dados descriptografados de volta no arquivo
            with open(os.path.join(caminho_pasta, arquivo), 'wb') as arquivo_original:
                arquivo_original.write(dados_descriptografados)

    show_encryption_message()
