Exercitiul 8

Faceți un script Python (app.py) care scrie loguri atât în consolă, cât și într-un fișier la calea /log/app.log. Scriptul trebuie să printeze, la fiecare secundă, un mesaj însoțit de un timestamp.
Împachetați scriptul într-un Docker image și porniți-l. Directorul în care se scriu logurile trebuie montat ca volum Docker (deci va trebui să creați mai întâi un volum cu numele loguri  folosind docker volume create și să îl folosiți la rularea containerului).
Porniți un al doilea container Docker cu Nginx, care folosește același volum și expune fișierul de loguri, astfel încât acesta să poată fi accesat din browser (montați volumul la calea /usr/share/nginx/html).
Verificați în browser că puteți accesa fișierul de loguri și că acesta este actualizat cu mesaje noi la fiecare secundă.



Instructions 

1. Construieste imaginea Docker

docker build -t logger-app .

2.Creeaza volumul Docker

docker volume create loguri

3.Ruleaza containerul pentru logger

docker run -d --name logger -v loguri:/log logger-app

4.Ruleaza containerul NGINX care expune fisierul

docker run -d --name nginx-logs -p 8080:80 -v loguri:/usr/share/nginx/html nginx

5.Verifica in browser local 

http://localhost:8080/app.log

