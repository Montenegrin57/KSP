pocet_studentu = int(input())
slovnik = {}
studenti = []
ucitele = []


for i in range(pocet_studentu):
    ucitele = []
    student = input()
    pocet = int(input())
    studenti.append(student)
    for x in range(pocet):
        ucitele.append(input())
    slovnik[student] = set(ucitele)
print(slovnik)
prunik_ucitelu = set(ucitele)


for x in studenti:
    prunik_ucitelu = prunik_ucitelu & slovnik[x]
if len(prunik_ucitelu) > 0:
    prunik_ucitelu = list(prunik_ucitelu)
    print(prunik_ucitelu[0])
else:
    print("NEEXISTUJE")


student_1 = ""
student_2 = ""
max_pocet_ucitelu = 0
index = 1
for jmeno_1 in studenti:
    for jmeno_2 in studenti[index:]:
        ucitele = slovnik[jmeno_1] | slovnik[jmeno_2]
        pocet_ucitelu = len(ucitele)
        if pocet_ucitelu > max_pocet_ucitelu:
            student_1 = jmeno_1
            student_2 = jmeno_2
            max_pocet_ucitelu = pocet_ucitelu
    index += 1
print(student_1, student_2)
