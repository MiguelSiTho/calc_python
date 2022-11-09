import webbrowser as wb
import mod1

        #variáveis
try:
    number1 = int(input('primeiro número: '))
    print()
    number2 = int(input('segundo número: '))
    print()
    opcao = 1
except:
    print('|Algo deu de errado, verifique os números inseridos|')
    print()
    print('-->Somente deve haver algarismos no valor, caso tenha uma letra ou simbolo diferente de um número, o programa não funcionará!<--')
    print()
    exit()

        #explicar os inputs
while opcao:
    print("0. Sair")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    print('5. Exponenciação')
    print('6. Raiz Quadrada')
    print('7. Fatorial')
    print('8. Reiniciar')
    print()

    try:
            #pedir o input
        opcao = int(input("Opção: "))
    except:
        print('Coloque somente NÚMEROS de 0 A 8')
        opcao = 8
    try:
            #soma
        if(opcao==1):
            mod1.soma(number1, number2, number1 + number2)
            #subtração
        if(opcao==2):
            mod1.subt(number1, number2, number1 - number2)
            #multiplicação
        if(opcao==3):
             mod1.multi(number1, number2, number1 * number2)
            #divisão
        if(opcao==4):
            if(number2 == 0):
                print('Não é possível dividir por 0')
            else:
                try:
                    mod1.divi(number1, number2, number1 / number2)
                except:
                    print('algo deu de errado')
            #exponenciação
        if(opcao==5):
            try:
                mod1.poten(number1, number2, number1 ** number2)
            except:
                print('algo deu de errado')
                print('Lembre de que 0^[algum número negativo] é indeterminado!')
            #raiz quadrada
        if(opcao==6):
            if(number2 < 0):
                print('Não há raizes de números negativos')
            else:
                try:
                    mod1.rq(number1, number2,)
                except:
                    print('algo deu de errado')
            #fatorial
        if(opcao==7):
            try:
                mod1.fato(number1, number2)
            except:
                print('Houve um erro no programa, certifique se de não ter inserido valores negativos!')
                opcao = 8
        if(opcao==8):
            try:
                number1 = int(input('primeiro número: '))
                print()
                number2 = int(input('segundo número: '))
                print()
                opcao = 1
            except:
                print('|Algo deu de errado, verifique os números inseridos|')
                print()
                print('-->Somente deve haver algarismos no valor, caso tenha uma letra ou simbolo diferente de um número, o programa não funcionará!<--')
                print()
        if(opcao==9):
            wb.open('https://www.youtube.com/watch?v=xvFZjo5PgG0&ab_channel=Duran')
                

        if(opcao>9):
            print()
            print('escolha um número de 0 à 8')
            print()
            opcao = 0
    except:
        print('Houve um erro no programa')






# Adição
#mod1.soma(number1, number2, number1 + number2)


# Subtração
#mod1.subt(number1, number2, number1 - number2)


# Multiplicação
#mod1.multi(number1, number2, number1 * number2)


# Divisão
#mod1.divi(number1, number2, number1 / number2)


#potencia
#mod1.poten(number1, number2, number1 ** number2)


#raiz quadrada
#mod1.rq(number1, number2)


#fatorial
#mod1.fato(number1, number2)