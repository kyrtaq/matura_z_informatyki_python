stacja1plik = open("dane_systemy1.txt")
stacja2plik = open("dane_systemy2.txt")
stacja3plik = open("dane_systemy3.txt")

stacja1 = stacja1plik.readlines()
stacja2 = stacja2plik.readlines()
stacja3 = stacja3plik.readlines()
# print(stacja1[0].split())

temperatury1 = []
for zapis in stacja1:
    temperatury1.append(int(zapis.split()[1]))

temperatury2 = []
for zapis in stacja2:
    temperatury2.append(int(zapis.split()[1]))

temperatury3 = []
for zapis in stacja3:
    temperatury3.append(int(zapis.split()[1]))

temperatury1.sort()
temperatury2.sort()
temperatury3.sort()

print(temperatury1[0])

temp2 = int(str(temperatury2[0]),4)
print(bin(temp2))
temp3 = int(str(temperatury3[0]),8)
print(bin(temp3))