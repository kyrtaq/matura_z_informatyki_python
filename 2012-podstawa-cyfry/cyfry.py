cyfryPlik = open("cyfry.txt")

odpowiedzi = open("cyfryODP.txt","w")
cyfry = cyfryPlik.readlines()

def sumaCyfr(cyf):
    suma = 0
    for c in cyf:
        suma += int(c)
    return suma

def czy_rosnaca(cyf):
    for i in range(1,len(cyf)):
        if cyf[i] <= cyf[i-1]:
            return False
    return True

suma = 0
for cyfra in cyfry:
    if int(cyfra)%2 == 0:
        suma += 1

odpowiedzi.write(f"1) {suma}\n")

zsumowane_cyfry = []
for cyfra in cyfry:
    zsumowane_cyfry.append(int(sumaCyfr(cyfra.strip())))

MAX = max(zsumowane_cyfry) # 59
MIN = min(zsumowane_cyfry) # 2
index = 0
for cyfra in zsumowane_cyfry:
    if cyfra == MAX:
        break
    index+=1
odpowiedzi.write(f"2) najwieksza: {cyfry[index]}")

index = 0
for cyfra in zsumowane_cyfry:
    if cyfra == MIN:
        break
    index+=1
odpowiedzi.write(f"2) najmniejsza: {cyfry[index]}")

odpowiedzi.write("3) ")
for cyfra in cyfry:
    if czy_rosnaca(cyfra.strip()):
        odpowiedzi.write(cyfra)

cyfryPlik.close()
odpowiedzi.close()