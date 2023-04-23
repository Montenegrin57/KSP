##line_total = int(input())
##while line_total > 0:
##    line_x = int(input())
##    divider = 2
##    while divider < line_x:
##        zbytek = line_x % divider
##        if zbytek == 0:
##            print("SLOZENE")
##            break
##        divider += 1
##    else:
##        print("PRVOCISLO")
##    line_total -= 1
import math
line_total = int(input())
for i in range(line_total):
    line_x = int(input())
    end = int((math.sqrt(line_x)+1))
    for divider in range(2, end):
        zbytek = line_x % divider
        if zbytek == 0:
            print("SLOZENE")
            break
    else:
        print("PRVOCISLO")
