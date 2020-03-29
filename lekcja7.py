# zadanie 1
print('---------- zadanie 1')
wynik = ''
for n in range(1, 11):
    suma = 0
    for k in range(1, n + 1):
        suma = suma + k
    if n > 1:
        wynik = wynik + ', '
    wynik = wynik + str(suma)
print(wynik)

# zadanie 2
print('---------- zadanie 2')
for n in range(1, 11):
    print('{:2}{:5}'.format(n, n**3))

# zadanie 3
print('---------- zadanie 3')
imiona = input('Podaj imiona oddzielone spacjami: ')
for imie in imiona.split():
    print('Witaj, {}!'.format(imie))

# zadanie 4
print('---------- zadanie 4')
powt = int(input('Ile razy mam się wykonać? '))
for n in range(1, powt + 1):
    if n % 3 == 0 and n % 4 == 0:
        print('{} - hurra'.format(n))
    elif n % 4 == 0:
        print('{} jest wielokrotnością 4'.format(n))
    elif n % 3 == 0:
        print('{} jest wielokrotnością 3'.format(n))
    else:
        print('{} - *'.format(n))

# zadanie 5
print('---------- zadanie 5')
for wielk in range(2, 6):
    for wiersz in range(1, wielk + 1):
        napis = ''
        for k in range(wiersz):
            napis = napis + '#'
        print(napis)

# zadanie 6
print('---------- zadanie 6')
print('   |   1   2   3   4   5   6   7   8   9  10')
print('---+----------------------------------------')
for w in range(1, 11):
    wiersz = '{:2} |'.format(w)
    for k in range(1, 11):
        wiersz = wiersz + '{:4}'.format(w * k)
    print(wiersz)
