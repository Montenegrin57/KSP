#přečteme čísla a uložíme do seznamu a
N = int(input())
list_a = []
for i in range(N):
    list_a.append(int(input()))

#přečteme čísla a uložíme do seznamu b    
M = int(input())
list_b = []
for x in range(M):
    list_b.append(int(input()))
    
#počítání dvojic v seznamu
pocet_shod = 0
for a in list_a:
    for b in list_b:
        if a == b:
            pocet_shod +=1
            
print(pocet_shod)
