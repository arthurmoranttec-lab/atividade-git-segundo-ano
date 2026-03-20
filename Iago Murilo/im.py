alunos = int (input("Quantos alunos serão registrados? "))
qnotas = int (input("Quantas notas para cada aluno serão inseridas? "))
for aluno in range(alunos):
    soma = 0
    nome = input("Insira nome do aluno: ")
    for nota in range(qnotas):
        nota = float (input("insira nota do aluno: "))
        soma += nota
    media = soma / qnotas 
    if media >= 6:
        final = "Aprovado"
    elif media < 6 and media >= 4:
        final = "Recuperação"
    else:
        final = "Reprovado"
    print (f"Nome do aluno: {nome}") #será oq o professor inserir
    print (f"Nota do aluno: {media:.2f}") #será calculada pelo sistema
    print (f"Aluno está: {final}") #respósta do sistema