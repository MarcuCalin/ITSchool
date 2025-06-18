# Faceti un script in python care primeste 2 parametrii (numele utilizatorului și varsta
# acestuia):
# 1. Importa libraria sys
# 2. Dacă nu au fost pasati parametrii, aruncati o exceptie.
# 3. Dacă au fost pasati parametrii:
# a. printati mesajul “Au fost pasati <n> parametrii”.
# b. daca varsta este mai mare de 18 ani, creati un subdirector pe disk cu numele
# utilizatorului.

import sys
import os

#sys.argv[0] este scriptul 
user = sys.argv[1]
varsta = sys.argv[2]
varsta = int(varsta)


if not user and varsta:
        sys.exit(2)
else:
        print(f"Au fost pasati {len(sys.argv)-1} parametrii.") # primul argument e scriptul 

if varsta > 18:
    if os.path.exists(user):
            print(f"Directorul '{user}' există deja.")
    else:
            os.makedirs(user)
            print(f"Directorul '{user}' a fost creat.")
else:
        print("Utilizatorul este minor. Directorul nu a fost creat.")
