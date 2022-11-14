plikLiczby = open("liczby.txt")

liczby = plikLiczby.readlines()


# 4.1
# suma = 0
# for liczba in liczby:
#     if int(liczba) % 2 != 0:
#         suma+=1
#
# print(suma)

# 4.2

# def sumaCyfr(n):
#     n = str(n)
#     suma = 0
#     for cyfra in n:
#         suma += int(cyfra)
#
#     return suma
#
#
# for liczba in liczby:
#     if sumaCyfr(int(liczba)) == 11:
#         print(liczba, end=" ")

# 4.3

def czy_w_przedziale(n):
    if n < 4000:
        return False
    elif n > 5000:
        return False
    else:
        return True

def czy_pierwsza(n):
    for i in range(2,int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

for liczba in liczby:
    if czy_w_przedziale(int(liczba)) and czy_pierwsza(int(liczba)):
        print(liczba,end=" ")
plikLiczby.close()
