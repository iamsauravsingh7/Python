# Break Statement
'''
for i in "Devops":
    print(i)
    if i == "p":
        print("Found my data")
        break
print("Out of loop")

# Continue Statement
for i in "Devops":
    if i == "p":
        print("Found my data")
        continue
    print(f"Value of i is {i}")
print("Out of loop")

import random
VACCINES = ["Moderna", "Pfizer", "Sputnik", "Covaxing", "AstraZeneca"]

random.shuffle(VACCINES)
print(VACCINES)
LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"*******Testing Vaccine {vac}")
    if vac == LUCKY:
        print("************")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("************")
        break
    print("************")
    print("test Failed")
    print("************")
    print()'''
import random
VACCINES = ["Moderna", "Pfizer", "Sputnik", "Covaxing", "AstraZeneca"]

random.shuffle(VACCINES)
print(VACCINES)
LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"*******Testing Vaccine {vac}")
    if vac == LUCKY:
        print("************")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("************")
        continue
    print("************")
    print("test Failed")
    print("************")
    print()