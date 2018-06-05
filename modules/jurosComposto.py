#!/usr/bin/python
# coding: utf-8
import math

# TIPO
# 1 - Ao dia
# 2 - Ao mes
# 3 - Ao ano


def taxaEquivalenteMensal(taxa, tipo, duracao):
    i = ""
    taxa = float(taxa)
    tipo = int(tipo)
    duracao = int(duracao)
    if(tipo == 1):
        i = ((1 + (taxa/100.0))**(30*duracao) - 1)
    elif(tipo == 2):
        i = ((1 + (taxa/100.0))**duracao - 1)
    elif(tipo == 3):
        i = ((1 + (taxa/100.0))**(1.0/(12*duracao)) - 1)
    return i


def juros(m, c, i, t):
    if(m == ""):
        m = montante(c, i, t, "")
    if(c == ""):
        c = capital(m, i, t, "")
    if (m != "" and c != ""):
        m = float(m)
        c = float(c)
        return m-c
    else:
        return ""


def capital(m, i, t, j):
    if(m != "" and i != "" and t != ""):
        m = float(m)
        i = float(i)
        t = float(t)
        return m/((1+i/100) ** t)
    elif (j != "" and m != ""):
        j = float(j)
        m = float(m)
        return m-j
    else:
        return ""


def taxa(m, c, t):
    if(m != "" and c != "" and t != ""):
        m = float(m)
        c = float(c)
        t = float(t)
        return ((m/c)**(1/t))-1
    else:
        return ""


def tempo(m, c, i):
    if(m != "" and c != "" and i != ""):
        m = float(m)
        c = float(c)
        i = float(i)
        return math.log(m/c) / math.log(1+(i/100))
    else:
        return ""


def montante(c, i, t, j):
    if(c != "" and i != "" and t != ""):
        c = float(c)
        i = float(i)
        t = float(t)
        return c*(1+i/100) ** t
    elif (j != "" and c != ""):
        j = float(j)
        c = float(c)
        return j+c
    else:
        return ""
