# Exercitiul 2
# Scrieti un program in python care:
# ● Citește o variabila cu numele “parolă” introdusă de utilizator, folosind metoda input()
# ● Verifica dacă variabila are aceeași valoare ca o variabila de mediu cu numele
# PAROLA_SECRETA
# ● Dacă are aceeași valoare, printati “Parola corecta”, în caz contrar afișați parola
# greșită.
# ● Rulați programul cu mai multe valori și verificati ca face ce trebuie.

import os 

#print(os.environ)

os.environ["PAROLA_SECRETA"] = "abc123" # setare variabila de mediu acelasi lucru cu export din terminal 
parola = input("Introdu o parola: ")

parola_secreta = os.environ.get("PAROLA_SECRETA")

if parola == parola_secreta:
    print("Parola corecta! ")
else:
    print("Parola gresita ! Byee")



