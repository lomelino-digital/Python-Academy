def registar_aluno(turma):
    nome = input("Nome do aluno: ")
    genero = input("Género (M/F): ").strip().upper()

    while True:
        try:
            nota = float(input("Nota final (0-20): "))
            if 0 <= nota <= 20:
                break
            else:
                print("A nota deve estar entre 0 e 20.")
        except ValueError:
            print("Por favor, introduza um valor numérico válido.")

    aluno = {
        "nome": nome,
        "genero": genero,
        "nota": nota
    }

    turma.append(aluno)
    print(f"\nAluno '{nome}' registado com sucesso!\n")


def calcular_media(turma):
    if not turma:
        return 0
    soma = sum(aluno["nota"] for aluno in turma)
    return soma / len(turma)


def alunos_por_genero(turma, genero):
    return [aluno["nome"] 
    for aluno in turma if aluno["genero"] == genero]


def alunos_acima_media(turma, media):
    return [aluno["nome"] 
    for aluno in turma if aluno["nota"] > media]


def alunos_abaixo_media(turma, media):
    return [aluno["nome"] 
    for aluno in turma if aluno["nota"] < media]


def apresentar_resultados(turma):
    if not turma:
        print("Não há alunos registados.")
        return

    num_alunos = len(turma)
    media = calcular_media(turma)
    masculinos = alunos_por_genero(turma, "M")
    femininos = alunos_por_genero(turma, "F")
    acima_media = alunos_acima_media(turma, media)
    abaixo_media = alunos_abaixo_media(turma, media)

    print("\n========== RESULTADOS FINAIS ==========")
    print(f"1. Número de alunos na turma: {num_alunos}")
    print(f"2. Média de notas da turma: {media:.2f}")

    print(f"3. Alunos masculinos ({len(masculinos)}):")
    if masculinos:
        for nome in masculinos:
            print(f"   - {nome}")
    else:
        print("   Nenhum")

    print(f"4. Alunos femininos ({len(femininos)}):")
    if femininos:
        for nome in femininos:
            print(f"   - {nome}")
    else:
        print("   Nenhum")

    print(f"5. Alunos com nota acima da média ({len(acima_media)}):")
    if acima_media:
        for nome in acima_media:
            print(f"   - {nome}")
    else:
        print("   Nenhum")

    print(f"6. Alunos com nota abaixo da média ({len(abaixo_media)}):")
    if abaixo_media:
        for nome in abaixo_media:
            print(f"   - {nome}")
    else:
        print("   Nenhum")

    print("========================================\n")


def menu():
    TURMA = []  

    while True:
        print("=== MENU ===")
        print("1 - Registar novo aluno")
        print("2 - Terminar registo e apresentar resultados")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registar_aluno(TURMA)
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.\n")

    apresentar_resultados(TURMA)


if __name__ == "__main__":
    menu()