# zadanie 5
print('----- zadanie 5')
a = float(input('Podaj dł. boku A: '))
b = float(input('Podaj dł. boku B: '))
c = float(input('Podaj dł. boku C: '))
if a + b >= c:
    print('Ok, da się z tego naspawać trójkąt.')
    boki = [a, b, c]
    boki.sort()
    print('DEBUG:', boki)
    print('DEBUG:', a, b, c)
    a = boki[0]
    b = boki[1]
    c = boki[2]
    print('DEBUG:', a, b, c)
    if c**2 == a**2 + b**2:
        print('To jest trójkąt prostokątny (pitagorejski).')
        if a / 3 == b / 4 and b / 4 == c / 5:
            print('To jest trójkąt egipski.')
        else:
            print('To jest jakiś badziewny i nudny trójkąt prostokątny.')
    else:
        print('To nie jest trójkąt prostokątny.')
else:
    print('E, z tego to się trójkąta nie poskleja!')
