#nome convidado
n= input('Digite seu nome: ')

#Mensagem de boas vindas
print('Seja bem vindo(a) {}'.format(n))

#nome organizador
o= input('Quem está organizando o churrasco? ')

#crianças e adultos
a= int(input('Quantos adultos confirmaram presença? '))
c= int(input('Quantas crianças estarão presentes? '))

#soma adultos, crianças e carnes
t= (a * 0.4) + (c * 0.2)

#Lista total
print('Olá {}, seja bem vindo ao churrasco organizado por {}, temos {} adultos comfirmados e {} crianças confirmadas, o total necessário de carne para este churrasco é {} kilos'.format(n, o, a, c, t))

