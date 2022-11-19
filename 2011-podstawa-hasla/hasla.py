def czy_palindrom(haslo):
    for i in range(0,int(len(haslo)/2)):
        if haslo[i] != haslo[-1-i]:
            return False
    return True

def kolejne_znaki_220(haslo):
    for i in range(0,len(haslo)-1):
        if ord(haslo[i]) + ord(haslo[i+1]) == 220:
            return True
    return False

hasla = open("hasla.txt")

haslaPlik = hasla.readlines()

parzyste = 0
for haslo in haslaPlik:
    if len(haslo) % 2 == 0:
        parzyste += 1
print(f"{parzyste} hasel ma parzysta liczbe znakow, {200 - parzyste} ma nieparzysta liczbe znakow")

# for haslo in haslaPlik:
#     if czy_palindrom(haslo.strip()):
#         print(haslo)

for haslo in haslaPlik:
    if kolejne_znaki_220(haslo.strip()):
        print(haslo)

hasla.close()