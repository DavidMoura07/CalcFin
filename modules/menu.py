#!/usr/bin/python
# coding: utf-8


def jurosComposto():
    print("Considerando: M=C(1+i)^t & J=M-C onde,")
    print("M: MONTANTE \t J: JUROS \t C: CAPITAL")
    print("i: TAXA (em meses, não divida por 100)")
    print("t: TEMPO (meses)\n")


def descontoComercialSimples():
    print("Considerando Dc=N*i*t onde,")
    print("Dc = Desconto Comercial")
    print("N = Valor Nominal")
    print("i = Taxa")
    print("t = Tempo")


def descontoRacionalSimples():
    print("Considerando Dr=(N*i*t)/(100+i*t) & N=C(1+i*t) & Dr= N-C")
    print("Dr = Desconto Racional")
    print("N = Valor Nominal")
    print("i = Taxa")
    print("t = Tempo")
    print("C = Valor Atual")


def jurosSimples():
    print("Considerando j = cit")
    print("E, m = c+j")
    print("Onde,")
    print("j: JUROS \t c: CAPITAL")
    print("i: TAXA \t t: TEMPO")
    print("m: montante\n")

    print("O que você deseja saber?")
    print("1- j \t 2- c")
    print("3- i \t 4- t")
    print("5- m")
    return input()


def principal():
    print("Escolha uma opção pelo numero:")
    print("1- JUROS SIMPLES")
    print("2- JUROS COMPOSTO")
    print("3- DESCONTO SIMPLES")
    return input()
