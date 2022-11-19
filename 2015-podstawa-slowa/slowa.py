slowaPlik = open("slowa.txt","r")
slowaOdp = open("slowaODP.txt","w")
nowePlik = open("nowe.txt","r")

slowa = slowaPlik.readlines()
nowe = nowePlik.readlines()

def odbij_slowo(slowo):
    slowo.strip()
    slowo = slowo[::-1]
    return slowo


liczbaWierszy = 0
for i in range(1,12+1):
    for slowo in slowa:
        if len(slowo.strip()) == i:
            liczbaWierszy+=1
    slowaOdp.write(f"W tym pliku jest {liczbaWierszy} slow {i} literowych")
    liczbaWierszy = 0

liczbaWord = 0
for word in nowe:
    for slowo in slowa:
        if slowo.strip() == word.strip():
            liczbaWord+=1
    slowaOdp.write(f"{word.strip()} {liczbaWord} ")
    liczbaWord=0

liczbaWord = 0
for word in nowe:
    for slowo in slowa:
        word = word.strip()
        slowo = slowo.strip()
        if slowo == (word[::-1]):
            liczbaWord+=1
    print(f"{word.strip()} {liczbaWord} ")
    liczbaWord = 0

nowePlik.close()
slowaPlik.close()
slowaOdp.close()