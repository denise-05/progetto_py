from random import *

semi = ['bastoni', 'coppe', 'denari', 'spade']
valori = ['asso', 'due', 'tre', 'quattro', 'cinque', 'sei', 'sette', 'fante', 'cavallo', 're']

n = 40

carte = list(range(n))

shuffle(carte)

while True:
    estrai = input('Per estrarre premi invio, altrimenti premi E! ')
    if estrai == 'E':
        break
    estratta = carte.pop()      
    n -= 1
    s = estratta//10
    v = estratta%10
    print('La carta estratta è', estratta)
    print(valori[v], 'di', semi[s]) 