def prevod_cisel(cislo, end_soustava):
    answer = []
    while cislo > 0:
        zbytek = cislo % end_soustava
        cislo = cislo // end_soustava
        if zbytek > 9:
            zbytek += 55
            znak = chr(zbytek)
        else:
            znak = zbytek
        answer.append(znak)
    return answer


def pocet_nul():
    pocet = 0
    for x in prevod_cisel(cislo, soustava):
        if x == 0:
            pocet += 1
        else:
            return pocet


while True:
    nazev_souboru = input("název souboru:")
    try:
        f = open(nazev_souboru)
        break
    except:
        print("špatný název")
cislo = int(f.read())
f.close()
soustava = 2
max_soustava = 2
max_pocet_nul = 0
nazev_novi = input("název nového souboru:")
while True:
    if pocet_nul() >= max_pocet_nul:
        max_soustava = soustava
        max_pocet_nul = pocet_nul()
    if len(prevod_cisel(cislo, soustava)) <= max_pocet_nul:
        f = open(nazev_novi, "x")
        max_soustava = str(max_soustava)
        print(max_soustava)
        f.write(max_soustava)
        f.close()
        break
    soustava += 1
