import random

sayi = random.randint(1,50)
hak = int(input('Kaç can ile başlamak istersiniz: '))
can = hak
sayac = 0

while can > 0:
    can -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız {100 - (100/hak) * (sayac-1)}')
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')
    
    if can == 0:
        print(f'Can kalmadı. Tutulan sayı: {sayi}')