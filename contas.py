from random import randint
#Linha

def linha():
    print('=-'*13)
#Exercicios de subtração
    
def subtracao():
    while True:
        a = randint(1,99)
        b = randint(1,99)
        res = a-b
        if res > 0:
            break
    res2 = int(input(f'Quanto é {a}-{b}? '))
    if res == res2:
        print('Correto!')
    else:
        print('Incorreto :(')
    linha()
#Exercícios de soma
def soma():
    a = randint(1,99)
    b = randint(1,99)
    res = a+b
    res2 = int(input(f'Quanto é {a}+{b}? '))
    if res2 == res:
        print('Correto!')
    else:
        print('Incorreto :(')
    linha()
#Exercícios de divisão

def divisao():
    while True:
        a = randint(1,99)
        b = randint(1,9)
        res = a/b
        if res in range(1,99):
            break
    res2 = int(input(f'Quanto é {a}/{b}? '))
    if res == res2:
        print('Correto!')
    else:
        print('Incorreto :(')
    linha()
#Exercícios de multiplicação
def multiplicacao():
    a = randint(1,9)
    b = randint(1,9)
    res = a*b
    res2 = int(input(f'Quanto é {a}x{b}? '))
    if res == res2:
        print('Correto!')
    else:
        print('Incorreto :(')
    linha()
