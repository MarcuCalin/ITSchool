# Pornind de la un fișier text numit logs.txt în care sunt stocate mesaje de log de la mai
# multe servere, fiecare mesaj pe o linie, vrem să identificăm toate liniile care conțin cuvântul
# ERROR și să le afisam împreună cu numărul liniei.
# 1. Folosește o buclă for pentru a parcurge fiecare linie din fișier.
# 2. Verifică dacă linia conține cuvântul ERROR.
# 3. Afișează linia și numărul acesteia dacă conține ERROR.

# # logs.txt
# INFO: Server started successfully.
# WARNING: Disk space low.
# ERROR: Unable to connect to database.
# INFO: Scheduled backup completed.
# ERROR: Failed to send email.

import os

if not os.path.exists("logs.txt"):
    with open("logs.txt", "w") as log:
        log.write("""INFO: Server started successfully.
WARNING: Disk space low.
ERROR: Unable to connect to database.
INFO: Scheduled backup completed.
ERROR: Failed to send email.
""")
        
linie_numar = 1  # indexare linie

with open("logs.txt", "r") as log:
    for linie in log:
        if "ERROR" in linie:
            print(f"Linia {linie_numar}: {linie.strip()}")
        linie_numar += 1  # Incrementezi manual numărul liniei