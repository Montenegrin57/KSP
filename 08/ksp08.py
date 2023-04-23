import math


def prvocislo(cislo: int):
    for y in range(2, cislo):
        zbytek = cislo % y
        if zbytek == 0:
            return False
    else:
        return True


def vypis_matici(velikost: int, matice: dict):
    s = open("out_1.txt", "x")
    for z in range(velikost):
        s.writelines(matice.get(z))
        s.write("\n")
    s.close()


nazev_souboru = input("nazev souboru")
f = open(nazev_souboru)
cislo = int(f.read())
f.close()
odmocnina = math.ceil(math.sqrt(cislo))
matice = {}
for i in range(odmocnina):
    seznam = []
    for x in range(odmocnina):
        seznam.append(" ")
    matice[i] = seznam
souradnice_y = odmocnina//2
souradnice_x = round(odmocnina/2)-1
matice[souradnice_y][souradnice_x] = "X"
smer = 1
for r in range(2, cislo + 1):
    match smer:
        case 1:
            souradnice_x += 1
            if prvocislo(r):
                matice[souradnice_y][souradnice_x] = "#"
            else:
                matice[souradnice_y][souradnice_x] = "."
            if matice[souradnice_y - 1][souradnice_x] == " ":
                smer = 2
        case 2:
            souradnice_y -= 1
            if prvocislo(r):
                matice[souradnice_y][souradnice_x] = "#"
            else:
                matice[souradnice_y][souradnice_x] = "."
            if matice[souradnice_y][souradnice_x - 1] == " ":
                smer = 3
        case 3:
            souradnice_x -= 1
            if prvocislo(r):
                matice[souradnice_y][souradnice_x] = "#"
            else:
                matice[souradnice_y][souradnice_x] = "."
            if matice[souradnice_y + 1][souradnice_x] == " ":
                smer = 4
        case 4:
            souradnice_y += 1
            if prvocislo(r):
                matice[souradnice_y][souradnice_x] = "#"
            else:
                matice[souradnice_y][souradnice_x] = "."
            if matice[souradnice_y][souradnice_x + 1] == " ":
                smer = 1
vypis_matici(odmocnina, matice)
