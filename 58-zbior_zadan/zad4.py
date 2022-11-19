import math
stacja1plik = open("dane_systemy1.txt")

stacja1 = stacja1plik.readlines()
# print(stacja1[0].split())

temperatury1 = []
for zapis in stacja1:
    temperatury1.append(int(zapis.split()[1],2))

j = 0
okrazenie = 0
najwiekszySkok = 0
for i in range(0,len(temperatury1)-1):
    for j in range(1+okrazenie,len(temperatury1)):
        ti = temperatury1[i]
        tj = temperatury1[j]
        r = (ti - tj) ** 2
        skok = math.ceil(r/abs(i - j))
        if skok > najwiekszySkok:
            najwiekszySkok = skok
    okrazenie +=1
print(najwiekszySkok)
