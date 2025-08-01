Exercitiul 10
Creați o nouă rețea de tipul bridge cu numele retea-interna.
Porniti doua containere de tipul tools (vezi exercițiul 9) cu nume diferite.
Logati-va pe fiecare container și încercați sa dati ping la celalat container folosind ip-ul și apoi DNS-ul.
Deconectati DOAR primul container de la reteaua retea-interna. Incercati iar sa dati ping intre containere pe baza de IP si pe baza de DNS. 
Conectati ambele containere la reteaua bridge default. Inspectati ambele retele (bridge-ul default si bridge-ul retea-interna) si verificati ce containere sunt atasate. 
Inspectati si containerele si verificati la ce retele sunt conectate.

eu@Ubuntu2204:~$ docker network create retea-interna
b811a6ede9eda9e9e7148c8ba7efc656f73a5541146ea900fca9d8d666b68438
eu@Ubuntu2204:~$ docker network ls
NETWORK ID     NAME            DRIVER    SCOPE
1cfdad2b4505   bridge          bridge    local
3c27ced90a3e   host            host      local
520cd53e497a   none            null      local
b811a6ede9ed   retea-interna   bridge    local
eu@Ubuntu2204:~$ docker run -d --network retea-interna --name ex10_1 tools
f46e9eb945873f26a6ed16961795b551eb4093e9d0025c671ac407f618e44eb1
eu@Ubuntu2204:~$ docker ps
CONTAINER ID   IMAGE     COMMAND            CREATED         STATUS         PORTS     NAMES
f46e9eb94587   tools     "sleep infinity"   4 seconds ago   Up 3 seconds             ex10_1
eu@Ubuntu2204:~$ docker run -d --network retea-interna --name ex10_2 tools
eu@Ubuntu2204:~$ docker exec -it ex10_1 bash
root@f46e9eb94587:/# ping ex10_2
PING ex10_2 (172.18.0.3) 56(84) bytes of data.
64 bytes from ex10_2.retea-interna (172.18.0.3): icmp_seq=1 ttl=64 time=0.814 ms
64 bytes from ex10_2.retea-interna (172.18.0.3): icmp_seq=2 ttl=64 time=0.106 ms
64 bytes from ex10_2.retea-interna (172.18.0.3): icmp_seq=3 ttl=64 time=0.126 ms
64 bytes from ex10_2.retea-interna (172.18.0.3): icmp_seq=4 ttl=64 time=0.109 ms
64 bytes from ex10_2.retea-interna (172.18.0.3): icmp_seq=5 ttl=64 time=0.092 ms
^C
--- ex10_2 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4094ms
rtt min/avg/max/mdev = 0.092/0.249/0.814/0.282 ms
root@f46e9eb94587:/# exit
eu@Ubuntu2204:~$ docker network disconnect retea-interna ex10_1
eu@Ubuntu2204:~$ docker inspect ex10_1
eu@Ubuntu2204:~$ docker exec -it ex10_1 bash
root@f46e9eb94587:/# ping ex10_2
ping: ex10_2: Temporary failure in name resolution
root@f46e9eb94587:/# ping 172.18.0.3
ping: connect: Network is unreachable
root@f46e9eb94587:/# 

docker network disconnect retea-interna ex10_2
eu@Ubuntu2204:~$ docker network connect bridge ex10_1
eu@Ubuntu2204:~$ docker network connect bridge ex10_2
