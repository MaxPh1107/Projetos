print('Bem Vindo ao Quizz')
print('Serão 3 perguntas no total')
print('O Assunto será:Conhecimentos Gerais')
c = 0
r4 = '' 
while c != 3 or r4!='n':
    print('1- Quem foi Catarina a Grande?')
    print('''
    a) Imperatriz da Russia
    b) Rainha de Portugal
    c) Princesa de Gales
             ''')
    r1 = str(input('Qual a resposta: '))
    if r1 == 'a':
        print('Você acertou!')
        c+=1
    elif r1 == 'b' or r1 == 'c':
        print('Você errou!')
    print('2- Em que ano o Brasil recebeu a Copa do Mundo?')
    print('''
    a) 2000
    b) 2001
    c) 2014
             ''')
    r2 = str(input('Qual a resposta: '))
    if r2 == 'c':
        print('Você acertou!')
        c+=1
    elif r2 == 'a' or r2 == 'b':
        print('Você errou!')
    print('3- Qual a cor de um rubi?')
    print('''
    a) Verde
    b) Vermelho
    c) Azul
             ''')
    r3 = str(input('Qual a resposta: '))
    if r3 == 'b':
        print('Você acertou!')
        c+=1
    elif r3 == 'a' or r3 == 'c':
        print('Você errou!')
    if c == 3:
        print('Parabéns, você acertou todas as perguntas!')
        break
    else:
        print('Gostaria de tentar novamente!')
        r4 = str(input('Qual a resposta: '))
        if r4 =='s':
            print('Vamos de novo')
        else:
            break