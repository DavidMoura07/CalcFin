#!/usr/bin/python
# coding: utf-8


def desconto(n, i, t, c):
    if(n != "" and c != ""):
        n = float(n)
        c = float(c)
        return n-c

    elif(n != "" and i != "" and t != ""):
        n = float(n)
        i = float(i)
        i = i/100.0
        t = float(t)
        if(i*t != -1):
            return (n*i*t)/(1+i*t)
    elif(i != "" and c != "" and t != ""):
        i = float(i/100.0)
        c = float(c)
        t = float(t)
        return i*c*t

    return ""


def valNominal(d, i, t, c):
    if(c != "" and d != ""):
        d = float(d)
        c = float(c)
        return d+c

    elif(d != "" and i != "" and t != ""):
        d = float(d)
        i = float(i)
        i = i/100.0
        t = float(t)
        c = d/(i*t)
        return d+c
    elif(c != "" and i != "" and t != ""):
        c = float(c)
        i = float(i/100.0)
        t = float(t)
        return c*(1+i*t)

    return ""


def taxa(d, n, t, c):
    if(c == "" and n != "" and d != ""):
        d = float(d)
        n = float(n)
        c = float(n-d)

    if(d != "" and t != "" and c != ""):
        d = float(d)
        c = float(c)
        t = float(t)
        if(t*c != 0):
            return d/(t*c)

    return ""


def tempo(d, n, i, c):
    if(c == "" and n != "" and d != ""):
        d = float(d)
        n = float(n)
        c = float(n-d)

    if(d != "" and i != "" and c != ""):
        d = float(d)
        c = float(c)
        i = float(i)
        i = i/100.0
        if(i*c != 0):
            return d/(i*c)

    return ""


def valAtual(d, n, i, t):
    if(d != "" and n != ""):
        n = float(n)
        d = float(d)
        return n-d

    elif(n != "" and i != "" and t != ""):
        n = float(n)
        i = float(i)
        i = i/100.0
        t = float(t)
        if(i*t != -1):
            return n/(1+i*t)
    elif(i != "" and d != "" and t != ""):
        i = float(i)
        i = i/100.0
        d = float(d)
        t = float(t)
        if(i*t != 0):
            return d/(i*t)

    return ""
