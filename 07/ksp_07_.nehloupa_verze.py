def eukleiduv_algoritmus_r(W, U):
    if 0 == U:
        return W
    else:
        return eukleiduv_algoritmus_r(U, W % U)
        

def NSN(a, b):
    return int((a*b)/eukleiduv_algoritmus_r(a, b))


nazev_souboru = input()
nazev_souboru_novy = input()
f = open(nazev_souboru)
cislo_1 = int(f.readline())
cislo_2 = int(f.readline())
f.close()
NSD = eukleiduv_algoritmus_r(cislo_1, cislo_2)
NSN = NSN(cislo_1, cislo_2)
f = open(nazev_souboru_novy, "x")
f.write(str(NSD)+"\n")
f.write(str(NSN))
