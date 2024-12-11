added = 0
tot = 200


ItemsDictionary = {
    "A1":["Case", "Compact",75.00],
    "A2":["Case", "Tower",150.00],
    "B1":["RAM", "8 GB",79.99],
    "B2":["RAM", "16 GB",149.99],
    "B3":["RAM", "32 GB",299.99],
    "C1":["Main Hard Disk Drive", "1 TB HDD",49.99],
    "C2":["Main Hard Disk Drive", "2 TB HDD",89.99],
    "C3":["Main Hard Disk Drive", "4 TB HDD",129.99],
    "D1":["Solid State Drive", "240 GB SSD",59.99],
    "D2":["Solid State Drive", "480 GB SSD",119.99],
    "E1":["Second Hard Disk Drive", "1 TB HDD",49.99],
    "E2":["Second Hard Disk Drive", "2 TB HDD",89.99],
    "E3":["Second Hard Disk Drive", "4 TB HDD",129.99],
    "F1":["Optical Drive", "DVD/Blu-Ray Player",50.00],
    "F2":["Optical Drive", "DVD/Blu-Ray Re-writer",100.00],
    "G1":["Operating System", "Standard Version",100.00],
    "G2":["Operating System", "Professional Version",175.00],
        }

# Task 1
print(fr"Case options are : A1 : ", ItemsDictionary["A1"] , "A2 : ", ItemsDictionary["A2"])
chosen = input("Please pick a code ")
while chosen != "A1" and chosen != "A2":
    chosen = input("Please pick a valid code ")

tot+=ItemsDictionary[chosen][2]

print(fr"RAM options are : B1 : ", ItemsDictionary["B1"] , "B2 : ", ItemsDictionary["B2"], "B3 : ", ItemsDictionary["B3"])
chosen = input("Please pick a case ")
while chosen != "B1" and chosen != "B2" and chosen != "B3":
    chosen = input("Please choose a valid RAM code ")

tot+=ItemsDictionary[chosen][2]

print(fr"Main Hard Disk Drive options are C1 : ", ItemsDictionary["C1"] , "C2 : ", ItemsDictionary["C2"], "C3 : ", ItemsDictionary["C3"])
chosen = input("Please pick an HDD ")
while chosen != "C1" and chosen != "C2" and chosen != "C3":
    chosen = input("Please choose a valid HDD code ")

tot+=ItemsDictionary[chosen][2]

# Task 2

extraitemsf = input("Please enter Y if you would like any extra items, and N if you would like to checkout ")
while extraitemsf != "Y" and extraitemsf != "N":
    extraitemsf = input("Please choose a valid Choice ")

if extraitemsf == "Y":
    extraitemsf = input("Would you like to buy an SSD? Enter Y for yes and N for no ")
    while extraitemsf != "Y" and extraitemsf != "N":
        chosen = input("Please choose a valid Choice ")
    if extraitemsf == "Y":
        print(fr"SSD options : D1 : ", ItemsDictionary["D1"] , "D2 : ", ItemsDictionary["D2"])
        chosen = input("Please pick an SSD ")
        while chosen != "D1" and chosen != "D2":
            chosen = input("Please choose a valid SSD code ")
        tot+=ItemsDictionary[chosen][2]
        added += 1

    extraitemsf = input("Would you like to buy an extra HDD? Enter Y for yes and N for no ")
    while extraitemsf != "Y" and extraitemsf != "N":
        chosen = input("Please choose a valid Choice ")
    if extraitemsf == "Y":
        print(fr"HDD options : E1 : ", ItemsDictionary["E1"] , "E2 : ", ItemsDictionary["E2"], "E3 : ", ItemsDictionary["E3"])
        chosen = input("Please pick an HDD")
        while chosen != "E1" and chosen != "E2" and chosen != "E3":
            chosen = input("Please choose a valid HDD code" )
        tot+=ItemsDictionary[chosen][2]
        added += 1

    extraitemsf = input("Would you like to buy an Optical Drive? Enter Y for yes and N for no")
    while extraitemsf != "Y" and extraitemsf != "N":
        chosen = input("Please choose a valid Choice")
    if extraitemsf == "Y":
        print(fr"Optical options : F1 ", ItemsDictionary["F1"] , "F2 : ", ItemsDictionary["F2"])
        chosen = input("Please pick an Optical Drive")
        while chosen != "F1" and chosen != "F2":
            chosen = input("Please choose a valid Optical Drive code ")
        tot+=ItemsDictionary[chosen][2]
        added += 1

    extraitemsf = input("Would you like to buy an Operating System? Enter Y for yes and N for no")
    while extraitemsf != "Y" and extraitemsf != "N":
        chosen = input("Please choose a valid Choice ")
    if extraitemsf == "Y":
        print(fr"Operating System options : G1 ", ItemsDictionary["G1"] , "G2 : ", ItemsDictionary["G2"])
        chosen = input("Please pick an Optical Drive ")
        while chosen != "G1" and chosen != "G2":
            chosen = input("Please choose a valid OS code ")
        tot+=ItemsDictionary[chosen][2]
        added += 1

# Task 3
if added  == 1:
    newtot =tot-0.05*tot
elif added  > 1:
    newtot =tot-0.1*tot
else: newtot = tot

print(fr"total price is : {newtot} , you have saved {tot-newtot} dollars")
