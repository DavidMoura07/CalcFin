#!/usr/bin/python
# coding: utf-8

import os

import sys
sys.path.insert(0, '/modules')

from modules import menu, jurosSimples, jurosComposto, descComercialSimples, descRacionalSimples


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
            # JUROS SIMPLES
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

            # JUROS COMPOSTO
            elif(opc == 2):
                clean()
                print("Opção escolhida: JUROS COMPOSTOS")
                menu.jurosComposto()
                print("Informe os dados que você possui")
                print("Caso não possua algum dos dados a seguir pressione enter")
                m = input("Montante: ")
                j = input("Juros: ")
                c = input("Capital: ")
                emMeses = input(
                    "Sua taxa está em meses?\n1 - SIM \t 2 - NÃO\n")
                if(emMeses == "1"):
                    print("Ótimo, não a divida por 100 entao, blz?")
                    i = input("Qual o valor da taxa? ")
                else:
                    print("Então vamos converte-la!")
                    i = input(
                        "qual o valor da taxa? Não divida por 100 ok?!\n")
                    print("Agora me diga, sua taxa esta em:")
                    print("1 - dias")
                    print("2 - meses")
                    print("3 - anos")
                    tipo = input("> ")
                    if(tipo == "1"):
                        period = input("Hum... Quantos dias? ")
                    elif(tipo == "2"):
                        period = input("Hum... Quantos meses? ")
                    elif(tipo == "3"):
                        period = input("Hum... Quantos anos? ")
                    i = jurosComposto.taxaEquivalenteMensal(i, tipo, period)
                    print(
                        "Exelente! sua taxa equivalente é de %0.2f%% ao mês!" % (i*100))

                t = input("Tempo: ")
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
                # COMERCIAL / POR FORA
                if(opc == "1"):
                    clean()
                    menu.descontoComercialSimples()
                    print("Informe os dados que você possui")
                    print("Caso não possua algum dos dados a seguir pressione enter")
                    d = input("Dc = ")
                    n = input("N = ")
                    print("Não divida por 100")
                    i = input("i = ")
                    t = input("t = ")
                    print("\n")

                    # DESCONTO COMERCIAL
                    if(d == ""):
                        d = descComercialSimples.desconto(n, i, t)
                        if(d != ""):
                            print("DESCONTO COMERCIAL = $"+str(d))
                        else:
                            print("Impossível calcular o DESCONTO COMERCIAL!")
                    # VALOR NOMINAL
                    if(n == ""):
                        n = descComercialSimples.valNominal(d, i, t)
                        if(n != ""):
                            print("VALOR NOMINAL = $%.2f" % n)
                        else:
                            print("Impossível calcular o VALOR NOMINAL!")
                    # TAXA
                    if(i == ""):
                        i = descComercialSimples.taxa(d, n, t)
                        if(i != ""):
                            print("TAXA = %.2f%%" % (i*100))
                        else:
                            print("Impossível calcular a TAXA !")
                    # TEMPO
                    if(t == ""):
                        t = descComercialSimples.tempo(d, n, i)
                        if(t != ""):
                            print("TEMPO = "+str(t))
                        else:
                            print("Impossível calcular o TEMPO!")
                # RACIONAL / POR DENTRO
                elif(opc == "2"):
                    clean()
                    menu.descontoRacionalSimples()
                    print("Informe os dados que você possui")
                    print("Caso não possua algum dos dados a seguir pressione enter")
                    d = input("Dr = ")
                    n = input("N = ")
                    print("Não divida por 100")
                    i = input("i = ")
                    t = input("t = ")
                    c = input("C = ")
                    print("\n")

                    # DESCONTO COMERCIAL
                    if(d == ""):
                        d = descRacionalSimples.desconto(n, i, t, c)
                        if(d != ""):
                            print("DESCONTO COMERCIAL = $%.2f" % d)
                        else:
                            print("Impossível calcular o DESCONTO COMERCIAL!")
                    # VALOR NOMINAL
                    if(n == ""):
                        n = descRacionalSimples.valNominal(d, i, t, c)
                        if(n != ""):
                            print("VALOR NOMINAL = $%.2f" % n)
                        else:
                            print("Impossível calcular o VALOR NOMINAL!")
                    # TAXA
                    if(i == ""):
                        i = descRacionalSimples.taxa(d, n, t, c)
                        if(i != ""):
                            print("TAXA = %.2f%%" % (i*100))
                        else:
                            print("Impossível calcular a TAXA !")
                    # TEMPO
                    if(t == ""):
                        t = descRacionalSimples.tempo(d, n, i, c)
                        if(t != ""):
                            print("TEMPO = "+str(t))
                        else:
                            print("Impossível calcular o TEMPO!")
                    # VALOR ATUAL
                    if(c == ""):
                        c = descRacionalSimples.valAtual(d, n, i, t)
                        if(c != ""):
                            print("VALOR ATUAL = %.2f" % c)
                        else:
                            print("Impossível calcular o VALOR ATUAL!")
                else:
                    print("1")
                    isValid = False
            else:
                print("2")
                isValid = False
        else:
            print("3")
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

    print("Calculadora Financeira\n\n")
    print("Obrigado e até a próxima!")
    print("Por David de Moura Marques")


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
