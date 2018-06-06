#!/usr/bin/python
# coding: utf-8


def desconto(n, i, t):
    if(n != "" and i != "" and t != ""):
        n = float(n)
        i = float(i)
        t = float(t)
        return n*(i/100.0)*t
    else:
        return ""


def valNominal(d, i, t):
    if(d != "" and i != "" and t != ""):
        d = float(d)
        i = float(i)
        t = float(t)
        return d/((i/100)*t)
    else:
        return ""


def taxa(d, n, t):
    if(d != "" and n != "" and t != ""):
        d = float(d)
        n = float(n)
        t = float(t)
        return d/(n*t)
    else:
        return ""


def tempo(d, n, i):
    if(d != "" and n != "" and i != ""):
        d = float(d)
        n = float(n)
        i = float(i)
        return d/(n*(i/100))
    else:
        return ""
