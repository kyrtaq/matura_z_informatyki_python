stacja1plik = open("dane_systemy1.txt")
stacja2plik = open("dane_systemy2.txt")
stacja3plik = open("dane_systemy3.txt")

stacja1 = stacja1plik.readlines()
stacja2 = stacja2plik.readlines()
stacja3 = stacja3plik.readlines()

temperatury1 = []
for zapis in stacja1:
    temperatury1.append(int(zapis.split()[1],2))

temperatury2 = []
for zapis in stacja2:
    temperatury2.append(int(zapis.split()[1],4))

temperatury3 = []
for zapis in stacja3:
    temperatury3.append(int(zapis.split()[1],8))

# max1 = temperatury1[0]
# suma1 = 0
# for i in range(1,len(temperatury1)):
#     if temperatury1[i] > max1:
#         max1 = temperatury1[i]
#         suma1 += 1
#
# max2 = temperatury2[0]
# suma2 = 0
# for i in range(1,len(temperatury2)):
#     if temperatury2[i] > max2:
#         max2 = temperatury2[i]
#         suma2 += 1
#
# max3 = temperatury3[0]
# suma3 = 0
# for i in range(1,len(temperatury3)):
#     if temperatury3[i] > max3:
#         max3 = temperatury3[i]
#         suma3 += 1

max1 = temperatury1[0]
max2 = temperatury2[0]
max3 = temperatury3[0]
suma = 1
# co za bezsens ze z tresci zadania mialbym sie domyslec ze pierwszy dzien tez jest rekordem
for i in range(1,len(temperatury1)):
    flaga = False
    if temperatury1[i] > max1:
        max1 = temperatury1[i]
        flaga = True
    if temperatury2[i] > max2:
        max2 = temperatury2[i]
        flaga = True
    if temperatury3[i] > max3:
        max3 = temperatury3[i]
        flaga = True
    if flaga:
        suma+=1

print(suma)
# print(suma1 + suma2 + suma3)