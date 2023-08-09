def Media(n,n2,n3,n4):
     return (n+n2+n3+n4)/4

def Conteudo():
    nome = input('Digite seu nome: ')
    print('=================================================')
    nota = float(input('Digite sua primeira nota: '))
    print('=================================================')
    nota2 = float(input('Digite sua segunda nota: '))
    print('=================================================')
    nota3 = float(input('Digite sua terceira nota: '))
    print('=================================================')
    nota4 = float(input('Digite sua utima  nota: '))
    print('=================================================')

    media = Media(nota,nota2,nota3,nota4)

    resultado =''

    if(media>=6):
        resultado="Aprovado"
    
    else:
       resultado ='Reprovado'
        

    print('A média do aluno(a) {} é : {:.2f}, ele(a) esta {} !'.format(nome,media,resultado))
    

def Opcao():
 while(True):
    Conteudo()
    opcao=input("Deseja continuar: (sim,não)?\n")
    if(opcao=="n"or opcao=="não"):
        break

print("====== Média Escolar======")
Opcao()




