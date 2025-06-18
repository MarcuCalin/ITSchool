# 1. Pentru acest exercițiu trebuie creat un fisier pe disk cu numele urls.txt ce conține
# pe fiecare linie cate o adresa url, de genul:
# ○ https://httpstat.us/201
# ○ https://httpstat.us/400
# ○ https://httpstat.us/500
# ○ https://httpstat.us/404
# ○ https://httpstat.us/201
# ○ https://httpstat.us/503
# ○ https://httpstat.us/200
# ○ https://httpstat.us/303
# 2. Citește linie cu line conținutul fișierului urls.txt
# 3. Folosește libraria requests pentru a face un call http catre fiecare url
# 4. Daca url-ul a intors un status de success (intre 200 si 299) adauga url-ul intr-un fisier
# cu numele success.txt
# 5. Daca url-ul a intors un status de eroare (orice status intre 300 si 599) adauga url-ul
# intr-un fisier cu numele errors.txt

import requests
import os 

#1.
if not os.path.exists("urls.txt"):
    with open("urls.txt", "w") as url_file:
        url_file.write("""
https://httpstat.us/201
https://httpstat.us/400
https://httpstat.us/500
https://httpstat.us/404
https://httpstat.us/201
https://httpstat.us/503
https://httpstat.us/200
https://httpstat.us/303
""")
    print("Fisierul 'urls.txt' a fost creat cu URL-uri default.")
else:
    print("Fisierul 'urls.txt' exista deja.")
                      
# 2. Citește fiecare URL din fișier
with open("urls.txt", "r") as url_file:
    urls = [line.strip() for line in url_file if line.strip()] # am cautat pe net cum se citeste linie cu linie cu lib requests

# 3. Trimite request pentru fiecare URL
for url in urls:
    try:
        response = requests.get(url)
        status = response.status_code

        # 4. Scrie în fișierul corespunzător
        if 200 <= status <= 299:
            with open("success.txt", "a") as success_file:
                success_file.write(f"{url} - {status}\n")
        elif 300 <= status <= 599:
            with open("errors.txt", "a") as error_file:
                error_file.write(f"{url} - {status}\n")
        else:
            print(f"Status necunoscut pentru {url}: {status}")
    except requests.RequestException as e:
        print(f"Eroare la URL-ul {url}: {e}")
        with open("errors.txt", "a") as error_file:
            error_file.write(f"{url} - EXCEPTIE\n")

#ceva nu merge aici -poate vedem la curs - ramane hanged (poate trebuie un timeout)