#Print de tafel van een op te geven getal met input()
# Bijv. 1 x 4 = 4 ; 2 x 4 = 8 etc t/m 10 x 4 = 40

g = int(input("Van welk getal wilt u de tafel weten? "))
for t in range(1, 11):
    print(f'{g} x {t} = {g*t}')
