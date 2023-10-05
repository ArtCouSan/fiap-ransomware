# Execute o codigo abaixo para instalar as bibliotecas necessarias
pip install -r requirements.txt

# Execute o criar_massa_teste.py para evitar o trabalho oneroso de criacao
python .\criar_massa_teste.py

# Execute o encriptar.py para encriptar os arquivos e as chaves 
# criadas irao para o arquivo chaves

python .\encriptar.py

## Exemplo de caminho de massa: ./massa_teste/

# Execute o decriptar para decriptar os arquivos 
# e use as chaves criadas no arquivo

python .\decriptar.py
