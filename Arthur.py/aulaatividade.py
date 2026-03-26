alunos = int(input("Quantos alunos serão registrados? "))

qnotax = int(input("Quantas notas para cada aludo serão inseridas? "))

for aluno in range (alunos):
    soma = 0
    nome = input("Nome do discente: ")
    for nota in range (qnotax):
        nota = float (input("Insira a nota do discente: "))
        soma += nota 
    media = soma / qnotax
    if media >= 6:
        fim = "Aprovado"
    elif media < 6 and media >= 4:
        fim = "Recuperação"
    else:
        fim = "Reprovado"
    print (f"Nome do discente: {nome}") #Será o professor que vai responder
    print (f"Nota do discente: {media}") #O sistema irá calcular
    print (f"O Discente está: {fim}") #resposta do sistema