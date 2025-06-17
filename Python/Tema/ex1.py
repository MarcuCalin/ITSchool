# Scrieti un script de python care:
# 1. Defineste cate o variabila din fiecare tip invatat:

nume = "Calin" # string
varsta = 38 # number
boolean = True # boolean
x = None # None
lista = ["mar", "banana", "piersica"] # list
s = {10, 50, 20} # set
# Dictionary
dic = {
"nume_serial" : "freaks",
"durata episod " : 45,
"exista" : False
}
tup = (1, 2, 3, 4, 5) # Tuple

# 2. Pentru fiecare variabila afișați valoarea și tipul ei folosind metoda print

print(type(nume))
print(type(varsta))
print(type(boolean))
print(type(x))
print(type(lista))
print(type(s))
print(type(dic))
print(type(tup)) 

# 3. Creați o alta variabila cu numele documentație de tip string pe mai multe linii in care
# sa puneti pentru fiecare variabila ceva de genul:
# “””
# Variabila X1 este de tipul Y1 si are valoare Z1
# Variabila X2 este de tipul Y2 si are valoare Z2
# “””


documentatie = f"""\
Variabila nume este de tipul {type(nume).__name__} si are valoarea {nume}
Variabila nume este de tipul {type(varsta).__name__} si are valoarea {varsta}
Variabila nume este de tipul {type(boolean).__name__} si are valoarea {boolean}
Variabila nume este de tipul {type(x).__name__} si are valoarea {x}
Variabila nume este de tipul {type(lista).__name__} si are valoarea {lista}
Variabila nume este de tipul {type(dic).__name__} si are valoarea {dic}
""" # aici am cautat pe net cum se face 

# 4. Afisati si acest string documentatie in consola.
print(documentatie)