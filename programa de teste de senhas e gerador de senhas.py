import random
import string
import re

def validar_senha(senha):
    comprimento = len(senha) >= 10
    tem_maiuscula = re.search(r'[A-Z]', senha)
    tem_minuscula = re.search(r'[a-z]', senha)
    tem_numero = re.search(r'\d', senha)
    tem_simbolo = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)

    pontos = sum([
        bool(comprimento),
        bool(tem_maiuscula),
        bool(tem_minuscula),
        bool(tem_numero),
        bool(tem_simbolo)
    ])

    if pontos <= 2:
        return "fraca"
    elif pontos == 3 or pontos == 4:
        return "media"
    else:
        return "forte"

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

print("Bem-vindo ao Guardião de Senhas!")

senha_usuario = input("Digite sua senha para validar: ")
avaliacao = validar_senha(senha_usuario)

if avaliacao == "forte":
    print("Uau! Sua senha é FORTE. Um hacker descobriria sua senha somente em 5...")

elif avaliacao == "media":
    print("Sua senha é MÉDIA. É importante que melhoremos ela.")
    nova_senha = gerar_senha()
    print("Aqui está sua nova senha segura:", nova_senha)

else:
    print("Sua senha é FRACA! Um hacker descobriria sua senha em 1 minuto!")
    nova_senha = gerar_senha()
    print("Aqui está sua nova senha segura:", nova_senha)

print("Lembre-se, é importante nunca compartilhar suas senhas na internet, mesmo com um programa de teste/gerador de senhas! >:) MWAHAHAHAHAHA")