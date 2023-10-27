from random import randint

print('Adivinhe o Número')
n = randint(1, 10)
print('O valor está entre 1 e 10')
v = d = 0

while True:
    jog = int(input('Qual a sua jogada: '))

    if jog > 10 or jog < 1:
        print('Valor Inválido, tente novamente!')
        continue

    if jog == n:
        print('Parabéns, você acertou!')
        v += 1
    else:
        print('Você errou!')
        d += 1

    r1 = input('Deseja jogar novamente? [S/N] ').strip().upper()
    
    if r1 == 'N':
        break
    elif r1 != 'S':
        print('Resposta inválida. Encerrando o jogo.')
        break

print(f'Você venceu {v} vezes')
print(f'Você perdeu {d} vezes')
print(f'Você tentou {v + d} vezes')
