import os 

def soma(a,b):
    return a + b

def sub(a,b):
    return a - b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

def limpa_terminal():
    os.system('cls' if os.name == 'nt' 'clear' else 'cls')