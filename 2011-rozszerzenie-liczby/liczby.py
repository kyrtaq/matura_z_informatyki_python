liczbyPlik = open("liczby.txt")

liczby = liczbyPlik.readlines()

parzyste = 0
for liczba in liczby:
    liczba = liczba.strip()
    if liczba[-1] == '0':
        parzyste+=1
print(parzyste)

for liczba in liczby:
    liczba = liczba.strip()
    liczba = int(liczba,2)
    print(liczba)
liczbyPlik.close()