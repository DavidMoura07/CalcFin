#!/usr/bin/python
# coding: utf-8

import os

import sys
sys.path.insert(0, '/modules')

from modules import menu, jurosSimples, jurosComposto


def main():
    clean()
    print("Calculadora Financeira")
    print("David de Moura Marques\n")

    isValid = False
    while not isValid:
        opc = menu.principal()
        if isNumber(opc):
            opc = int(opc)
            isValid = True

            if(opc == 1):
                clean()
                print("Opção escolhida: JUROS SIMPLES")
                opc = menu.jurosSimples()
                if isNumber(opc):
                    opc = int(opc)
                    # JUROS
                    if opc == 1:
                        clean()
                        result = jurosSimples.juros()
                        print("JUROS: $"+str(result))
                    # CAPITAL
                    elif opc == 2:
                        clean()
                        result = jurosSimples.capital()
                        print("CAPITAL: $"+str(result))
                    # TAXA
                    elif opc == 3:
                        clean()
                        result = jurosSimples.taxa()
                        print("TAXA: "+str(result)+"%")
                    # TEMPO
                    elif opc == 4:
                        clean()
                        result = jurosSimples.tempo()
                        print("TEMPO: "+str(result)+" meses")
                    # MONTANTE
                    elif opc == 5:
                        clean()
                        result = jurosSimples.montante()
                        print("MONTANTE: $"+str(result))
                    else:
                        isValid = False
                else:
                    isValid = False
            elif(opc == 2):
                clean()
                print("Opção escolhida: JUROS COMPOSTOS")
                menu.jurosComposto()
                print("Informe os dados que você possui")
                print("Caso não possua algum dos dados a seguir pressione enter")
                m = raw_input("Montante: ")
                j = raw_input("Juros: ")
                c = raw_input("Capital: ")
                emMeses = input(
                    "Sua taxa está em meses?\n1 - SIM \t 2 - NÃO\n")
                if(emMeses == 1):
                    print("Ótimo, não a divida por 100 entao, blz?")
                    i = raw_input("Qual o valor da taxa? ")
                else:
                    print("Então vamos converte-la!")
                    i = raw_input(
                        "qual o valor da taxa? Não divida por 100 ok?!\n")
                    print("Agora me diga, sua taxa esta em:")
                    print("1 - dias")
                    print("2 - meses")
                    print("3 - anos")
                    tipo = input("> ")
                    if(tipo == 1):
                        period = input("Hum... Quantos dias? ")
                    elif(tipo == 2):
                        period = input("Hum... Quantos meses? ")
                    elif(tipo == 3):
                        period = input("Hum... Quantos anos? ")
                    i = jurosComposto.taxaEquivalenteMensal(i, tipo, period)
                    print(
                        "Exelente! sua taxa equivalente é de %0.2f%% ao mês!" % (i*100))

                t = raw_input("Tempo: ")
                print("\n")

                # MONTANTE
                if(m == ""):
                    m = jurosComposto.montante(c, i, t, j)
                    if(m != ""):
                        print("MONTANTE = "+str(m))
                    else:
                        print("Impossível calcular o MONTANTE!")
                # JUROS
                if(j == ""):
                    j = jurosComposto.juros(m, c, i, t)
                    if(j != ""):
                        print("JUROS = $"+str(j))
                    else:
                        print("Impossível calcular os JUROS!")
                # CAPITAL
                if(c == ""):
                    c = jurosComposto.capital(m, i, t, j)
                    if(c != ""):
                        print("CAPITAL = $"+str(c))
                    else:
                        print("Impossivel calcular o CAPITAL!")
                # TAXA
                if(i == ""):
                    i = jurosComposto.taxa(m, c, t)
                    if(i != ""):
                        print("TAXA = "+str(i*100)+"%")
                    else:
                        print("Impossivel calcular a TAXA!")
                # TEMPO
                if(t == ""):
                    t = jurosComposto.tempo(m, c, i)
                    if(t != ""):
                        print("TEMPO = "+str(t)+" meses")
                    else:
                        print("Impossivel calcular o TEMPO!")
            # DESCONTO SIMPLES
            elif(opc == 3):
                clean()
                print("Opção escolhida: DESCONTO SIMPLES")
                print("Escolha um tipo:")
                print("1 - Comercial / Por Fora")
                print("2 - Racional  / Por dentro")
                opc = input("> ")
            else:
                isValid = False
        else:
            isValid = False

        if not isValid:
            clean()
            print("Opção inválida! Tente novamente")
            continue

        print("\nDeseja fazer outra operação?")
        print("1- SIM \t 2- NÃO")
        opc = input()
        if isNumber(opc):
            opc = int(opc)
            if(opc == 1):
                isValid = False
            else:
                isValid = True
        else:
            isValid = True

        clean()

    print("Obrigado e até a próxima!")


def clean():
    os.system('cls' if os.name == 'nt' else 'clear')


def isBetween(num, a, b):
    if num >= a and num <= b:
        return True
    else:
        return False


def isNumber(texto):
    try:
        int(texto)
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    main()
