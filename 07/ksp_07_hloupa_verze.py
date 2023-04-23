def nejvetsi_spolecny_delitel(a, b):
    if b < a:
        delitel = b
    elif a < b:
        delitel = a
    else:
        delitel = a
    while True:
        zbytek_a = a % delitel
        zbytek_b = b % delitel
        if zbytek_a == 0 and zbytek_b == 0:
            return delitel
        else:
            delitel -= 1


def nejmensi_spolecny_nasobek(a, b):
    nasobek = 1
    while True:
        if b > a:
            vetsi = b
            mensi = a
        elif a > b:
            vetsi = a
            mensi = b
        else:
            vetsi = a
            mensi = b
        spolecny_nasobek = vetsi*nasobek
        if spolecny_nasobek % mensi == 0:
            return spolecny_nasobek
        else:
            nasobek += 1


a = input()
b = input()
print(nejvetsi_spolecny_delitel(a, b))
print(nejmensi_spolecny_nasobek(a, b))
