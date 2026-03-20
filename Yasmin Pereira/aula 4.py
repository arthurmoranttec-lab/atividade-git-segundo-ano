# Autorização para entrada no evento #

idade = int(input("Insira sua idade: "))
autorizacao = input("Possui autorização dos responsáveis?(sim/não) ")

if  idade >= 18:
    print("Entrada permitida no evento")

elif idade < 16 and autorizacao == "sim":
    print("Entrada permitida no evento com a autorização do responsável")

elif idade >= 16 and autorizacao == "sim":
    print("Entrada permitida no evento")

else:
    print("Entrada negada!")
