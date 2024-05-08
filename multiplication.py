continuer = 'o'
while continuer =='o':
    nombre = input('Entrez un nombre : ')

    for i in range(0, 13):
        print(nombre, 'x', i, '=', int(nombre) * i)
        #print('{0} X {1} = {2}'.format(nombre, i, int(nombre) * i))

    continuer = input('Voulez-vous continuer ? (o/n) : ')
    if continuer == 'n':
        print('Au revoir !')