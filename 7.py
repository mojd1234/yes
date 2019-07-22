num = int(input("typee a number"))
list = [2,6,3,76,7,1,4,634,334,2]
aeh = 0
numless = 0
while aeh < 10:
    if list[aeh] < num:
        numless += 1
    aeh += 1
print(str(numless) +7 " numbers are less than " + str(num))