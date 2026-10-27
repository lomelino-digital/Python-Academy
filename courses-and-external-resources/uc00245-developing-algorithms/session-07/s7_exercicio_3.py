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
    nome = input()

    print("Qual o género do aluno (m) ou (f)?")
    genero = input()

    while True:
        print("Qual a nota final do aluno?")
        nota = input()
        try:
            nota = float(nota)
            break
        except ValueError:
            print("\nIntroduza um número por favor.")

    aluno = {"nome": nome, "genero": genero, "nota": nota}
    return aluno

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



def criar_turma():
    turma = []
    while True:
        print('Acrescente os dados do novo aluno: ')
        aluno = receber_info()
        turma.append(aluno)
        if not novo_aluno():
            print('Terminou de preencher a turma.')
            return turma


turma = criar_turma()

def lista_genero(turma,genero):
    return [gen["nome"] for gen in turma if gen["genero"] == genero]






numero_de_alunos = len(turma)
notas = [n["nota"] for n in turma]
media = sum(notas)/numero_de_alunos
masculinos = lista_genero(turma,'m')
femininos = lista_genero(turma,'f')

acima_da_media = [acima["nome"] for acima in turma if acima["nota"] > media]

abaixo_da_media = [abaixo["nome"] for abaixo in turma if abaixo["nota"] < media]


print(f'A turma tem {numero_de_alunos} alunos')
print()
print(f'A media das notas da turma é: {media}')
print()
if masculinos:
    print(f'Os alunos do género masculino são: {masculinos}')
    print()
else:
    print(f'A turma não tem alunos do género masculino.')
    print()

if femininos:
    print(f'Os alunos do género feminino são: {femininos}')
    print()
else:
    print(f'A turma não tem alunos do género feminino.')
    print()
print(f'Os alunos acima da média são: {acima_da_media}')
print()
print(f'Os alunos abaixo da média são: {abaixo_da_media}')