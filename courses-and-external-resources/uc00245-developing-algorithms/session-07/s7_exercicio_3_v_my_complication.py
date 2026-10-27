"""Crie um programa que peça o nome do ALUNO, GÉNERO E NOTA FINAL na disciplina
de Python.
Guarda os dados de cada aluno num dicionário ALUNO e todos os alunos numa lista
TURMA. No final, o programa deverá apresentar a seguinte informação:
1. Quantos alunos tem a turma
2. Qual a média de notas da turma
3. Quais os alunos masculinos
4. Quais os alunos femininos
5. Qual ou quais os alunos com a nota final acima da média
6. Qual ou quais os alunos com a nota final abaixo da média."""

def receber_info():
    print("Qual o nome do aluno?")
    aluno = input()

    print("Qual o género do aluno?")
    genero = input()

    while True:
        print("Qual a nota final do aluno?")
        nota = input()
        if nota.isnumeric():
            nota = float(nota)
            break
        print("\nIntroduza um número por favor.")

    return aluno, genero, nota


def novo_aluno():
    while True:
        print('Deseja acrescentar mais um aluno?')
        resposta = input()
        resposta = resposta.lower()
        if resposta == 'sim' or resposta == 'nao':
            if resposta == 'sim':
                return True
            return False
        print('Selecione sim ou nao.')


def preencher_info():
    aluno = {}
    turma = []
    generos = []
    notas = []
    while True:
        print('Acrescente os dados do novo aluno: ')
        dados = receber_info()
        turma.append(dados[0])
        generos.append(dados[1])
        notas.append(dados[2])
        aluno[dados[0]] = dados[1:]
        if not novo_aluno():
            print('Terminou de preencher a turma.')
            return aluno, turma, generos, notas


aluno, turma, generos, notas = preencher_info()
numero_de_alunos = len(turma)
media = sum(notas)/numero_de_alunos

   


         



print(f'A turma tem {len(turma)} alunos')
print()
print(f'A media das notas da turma é: {media}')

        








