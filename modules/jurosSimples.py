#!/usr/bin/python
# coding: utf-8


def juros():
    print("Calculando JUROS")
    print("Informe os seguintes dados:")
    c = float(input("Capital: "))
    i = float(input("Taxa ao mes (apenas numeros, não divida por 100): "))
    t = float(input("Tempo em meses (apenas numeros): "))
    j = c*(i/100)*t
    return j


def capital():
    print("Calculando CAPITAL")
    print("Informe os seguintes dados:")
    j = float(input("Juros: "))
    i = float(input("Taxa ao mes (apenas numeros, não divida por 100): "))
    t = float(input("Tempo em meses (apenas numeros): "))
    c = j/(i/100*t)
    return c


def taxa():
    print("Calculando TAXA")
    print("Informe os seguintes dados:")
    j = float(input("Juros: "))
    c = float(input("Capital: "))
    t = float(input("Tempo em meses (apenas numeros): "))
    i = (j/(t*c))*100
    return i


def tempo():
    print("Calculando TEMPO")
    print("Informe os seguintes dados:")
    j = float(input("Juros: "))
    c = float(input("Capital: "))
    i = float(input("Taxa ao mes (apenas numeros, não divida por 100): "))
    t = j/(i/100*c)
    return t


def montante():
    print("Calculando MONTANTE")
    print("Informe os seguintes dados:")
    print("Caso não saiba algum destes responda '?'")
    j = input("Juros: ")
    if(j == "?"):
        j = juros()
        print("\nJUROS: $"+str(j))

    c = input("Capital: ")
    if(c == "?"):
        c = capital()
        print("\nCAPITAL: $"+str(c))

    j = float(j)
    c = float(c)
    m = c+j

    return m
