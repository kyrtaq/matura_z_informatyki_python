plikPesel = open("dane.txt")

pesele = plikPesel.readlines()

# 6.1
# print(pesele)
#
# kobiety = 0
# mezczyzni = 0
# for pesel in pesele:
#     if int(pesel[9]) % 2 == 0:
#         kobiety += 1
#     else:
#         mezczyzni += 1
#
# print(f"liczba kobiet to {kobiety}, liczbe mezczyzn to {mezczyzni}")

# 5.2
# listopad to 11 albo 31
# urodzeni = 0
# for pesel in pesele:
#     if (pesel[2] == "1" and pesel[3] == "1") or (pesel[2] == "3" and pesel[3] == "1"):
#         urodzeni += 1
#
# print(urodzeni)

# 5.3
# 1 * a1 + 3 * a2 + 7 * a3 + 9 * a4 + 1 * a5 + 3 * a6 + 7 * a7 + 9 * a8 + 1 * a9 + 3 * a10 + a11
p = []
# czyPop = 1*int(p[0]) + 3 * int(p[1]) + 7*int(p[2]) + 9*int(p[3])+1*int(p[4])+3*int(p[5])+7*int(p[6])+9*int(p[7])+1*int(p[8])+3*int(p[9])+int(p[10])

suma = 0
for p in pesele:
    czyPop = 1 * int(p[0]) + 3 * int(p[1]) + 7 * int(p[2]) + 9 * int(p[3]) + 1 * int(p[4]) + 3 * int(p[5]) + 7 * int(
        p[6]) + 9 * int(p[7]) + 1 * int(p[8]) + 3 * int(p[9]) + int(p[10])
    if czyPop % 10 != 0:
        suma += 1

print(suma)

plikPesel.close()