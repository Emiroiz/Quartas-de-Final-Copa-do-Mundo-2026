from random import sample
selecoes = [ 'Brasil', 'Portugal', 'Argentina', 'Holanda', 'França', 'Croácia', 'Espanha',
'Inglaterra', 'Alemanha', 'Catar', 'Estados Unidos', 'Marrocos' ]
quartas = sample(selecoes,8)

print('Seleções classificadas para as quartas de final da Copa do Mundo 2026: ')
for selecoes in quartas: 
    print('-', selecoes)
