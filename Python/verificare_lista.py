import sys

lista_colegi=["Ana", "Ionut", "Alin"]

coleg_nou=input("Introduceti numele noului coleg: ")

if not coleg_nou:
    print("Nu ati introdus un format corect!")
    sys.exit(2)

if coleg_nou  not in lista_colegi:
    print("Colegul nu este in lista!")
    lista_colegi.append(coleg_nou)

print("Lista colegilor este: \n",lista_colegi)