stacja1plik = open("dane_systemy1.txt")
stacja2plik = open("dane_systemy2.txt")
stacja3plik = open("dane_systemy3.txt")

stacja1 = stacja1plik.readlines()
stacja2 = stacja2plik.readlines()
stacja3 = stacja3plik.readlines()

godziny1 = []
for zapis in stacja1:
    godziny1.append(int(zapis.split()[0],2))

godziny2 = []
for zapis in stacja2:
    godziny2.append(int(zapis.split()[0],4))

godziny3 = []
for zapis in stacja3:
    godziny3.append(int(zapis.split()[0],8))

# print(godziny1)
# print(godziny2)
# print(godziny3)

# sum = 0
# for i in range(1,len(godziny1)):
#     if (godziny1[i] - godziny1[i-1] != 24) and (godziny2[i] - godziny2[i-1] != 24) and (godziny3[i] - godziny3[i-1] != 24):
#        sum+=1

sum = 0
for i in range(0,len(godziny1)):
    stan = 12 + 24*i
    if godziny1[i] != stan and godziny2[i] != stan and godziny3[i] != stan:
        sum+=1
print(sum)
