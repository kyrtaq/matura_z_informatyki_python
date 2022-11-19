napisyPlik = open("napisy.txt")
odpowiedzi = open("napisyODP.txt","w")

napisy = napisyPlik.readlines()


def suma_cyfr(liczba):
    suma = 0
    for cyfra in liczba:
        suma += int(cyfra)
    return suma

def czy_tyle_samo(napis):
    if len(napis.strip()) % 2 == 1:
        return False
    if suma_cyfr(napis) != (len(napis.strip())/2):
        return False
    return True


suma = 0
for napis in napisy:
    if len(napis.strip()) % 2 == 0:
        suma+=1
odpowiedzi.write(f"1) {suma} \n")

suma = 0
for napis in napisy:
    if czy_tyle_samo(napis.strip()):
        suma+=1
odpowiedzi.write(f"2) {suma} \n")

jedynki = 0
for napis in napisy:
    if '0' not in napis:
        jedynki+=1

odpowiedzi.write(f"3) same jedynki: {jedynki} \n")
zera = 0
for napis in napisy:
    if '1' not in napis:
        zera+=1
odpowiedzi.write(f" same zera: {zera} \n")


suma = 0
for k in range(2,16+1):
    for napis in napisy:
        if len(napis.strip()) == k:
            suma+=1
    odpowiedzi.write(f"slow {k}-znakowych jest {suma}\n ")
    suma = 0

napisyPlik.close()
odpowiedzi.close()