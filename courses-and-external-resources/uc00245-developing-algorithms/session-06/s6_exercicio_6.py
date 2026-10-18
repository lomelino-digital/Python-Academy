"""6.Utilizando listas, faça um programa que faça 5 perguntas sobre um crime.
As perguntas são:
●
 "Telefonou para a vítima?"
●
 "Esteve no local do crime?"
●
 "Mora perto da vítima?"
●
 “Tinha algum conflito com a vítima?"
●
 "Já trabalhou com a vítima?“
O programa deve no final emitir uma classificação sobre
a participação da pessoa no crime. Se a pessoa
responder positivamente a 2 questões ela deve ser
classificada como "Suspeita“; entre 3 e 4 como
"Cúmplice" e; 5 como "Assassino". Caso contrário, ela
será classificada como "Inocente"."""



def perguntas():
    perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Tinha algum conflito com a vítima?", "Já trabalhou com a vítima?"]
    respostas = []
    print("Responda apenas sim ou nao: \n")
    for p in perguntas:        
        while True:
            print(p)
            resposta = input()
            resposta = resposta.lower()
            if resposta == 'sim' or resposta == 'nao':
                if resposta == 'sim':
                    respostas.append(1)
                else:
                    respostas.append(0)
                break
            print("Responda apenas sim ou nao: \n")            
    return sum(respostas)


def veredito(respostas):
    possivel = ['Inocente', 'Suspeita', 'Cúmplice','Cúmplice','Assassino','Inocente']
    return possivel[respostas-1]



investigacao = perguntas()

print(f" A pessoa é {veredito(investigacao)}")

        
