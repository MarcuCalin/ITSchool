Exercitiul 9 (tools image)

Creați o imagine de docker cu numele tools plecand de la imaginea de baza ubuntu si instalati pe ea (în Dockerfile următoarele):
vim
curl (iputils-ping)
Puneti in CMD un sleep Infinity ca imaginea sa nu “moara” imediat ce a fost pornita. Fceti build la imagine si porniti un container de test (dati ping catre google.com) 
O sa folosim aceasta imagine in exercitiile urmatoare.


Dockerfile ---> 
FROM ubuntu

RUN apt-get update && apt-get install -y vim && apt-get install iputils-ping -y

CMD ["sleep", "infinity"]

Comenzi :

docker build -t tools .

docker run -d --name test tools

docker exec -it test /bin/bash

root@903eb4f65bfe:/# ping google.com
PING google.com (142.250.201.206) 56(84) bytes of data.
64 bytes from bud02s35-in-f14.1e100.net (142.250.201.206): icmp_seq=1 ttl=254 time=22.4 ms
64 bytes from bud02s35-in-f14.1e100.net (142.250.201.206): icmp_seq=2 ttl=254 time=13.7 ms
64 bytes from bud02s35-in-f14.1e100.net (142.250.201.206): icmp_seq=3 ttl=254 time=14.5 ms
64 bytes from bud02s35-in-f14.1e100.net (142.250.201.206): icmp_seq=4 ttl=254 time=17.6 ms
