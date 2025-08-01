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

