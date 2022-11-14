plik = open("przyklad.txt", "r")

tekst = plik.readlines()
print(tekst)

for i in range(39, len(tekst), 40):
    print(tekst[i][9],end="")

plik.close()