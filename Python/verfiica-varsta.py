varsta = input("Care esta varsta ta? ")
varsta = int(varsta)

if varsta >= 18:
    print(f"Esti major . Poti aplica pt permis")
else:
    print(f"Esti minor . Revino peste {18 - varsta} ani")