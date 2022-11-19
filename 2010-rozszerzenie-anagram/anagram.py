anagramPlik = open("anagram.txt")
anagramOdp = open("anagramOdp.txt","w")

anagram = anagramPlik.readlines()



# liczbaZnakow = 0
# wiersz = 0
# for linia in anagram:
#     linia = linia.strip()
#     linia = linia.split(' ')
#     liczbaZnakow = len(linia[0])
#     flaga = True
#     for slowo in linia:
#         if len(slowo) != liczbaZnakow:
#             flaga = False
#             break
#     if flaga == True:
#         print(anagram[wiersz])
#     wiersz += 1

wiersz = 0
for linia in anagram:
    linia = linia.strip()
    linia = linia.split()
    flaga = True
    for slowo in linia:
        if ''.join(sorted(linia[0])) != ''.join(sorted(slowo)):
            flaga = False
    if flaga == True:
        print(anagram[wiersz])
    flaga = False
    wiersz+=1
# niesortowane = "dcba"
# posortowane = sorted(niesortowane)
#
# print(''.join(posortowane))

anagramOdp.close()
anagramPlik.close()