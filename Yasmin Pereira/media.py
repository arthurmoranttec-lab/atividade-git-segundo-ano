alunos = int(input("Quantas alunos deseja cadastrar? "))
notas = int(input("Quantas notas para cada aluno deseja cadatrar? "))




for i in range(alunos):
    soma = 0
    nome = input("Insira o nome do aluno: ")
    for nota in range(notas):
        nota = int(input("Digite a nota: "))
        soma+=nota
    media = soma/notas


    if media>=6:
        print(f"Média = {media} Aluno aprovado!")
    elif media<4:
        print(f"Média = {media} Reprovado")
    else:
        print(f"Média = {media}Recuperação")
