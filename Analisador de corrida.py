n= input('Qual seu nome? ')
d= float(input('Qual a distância percorrida? '))
t= int(input('Qual o tempo gasto? '))
vm= d / t
m= vm > 10

#Mensagem final

print('{} a distância percorrida foi {}km e você levou um tempo de {}h, a distância média percorrida foi maior ou menor que a meta 10 de {}km'.format(n,d,t,vm,m))