eu@Ubuntu2204:~$ docker network create public
b8df2bf457cbeebb0c487ac3ff6c75af48c20aa698f42f835847f98f227cf94d
eu@Ubuntu2204:~$ docker network ls
NETWORK ID     NAME            DRIVER    SCOPE
ab4ca6b37752   bridge          bridge    local
3c27ced90a3e   host            host      local
520cd53e497a   none            null      local
b8df2bf457cb   public          bridge    local
b811a6ede9ed   retea-interna   bridge    local

docker network create --internal private
ea0ec915b5f783ccb04b0d0e34e3cffaeabee177478dbd4de556874827b52c01
eu@Ubuntu2204:~$ docker network ls
NETWORK ID     NAME            DRIVER    SCOPE
ab4ca6b37752   bridge          bridge    local
3c27ced90a3e   host            host      local
520cd53e497a   none            null      local
ea0ec915b5f7   private         bridge    local
b8df2bf457cb   public          bridge    local
b811a6ede9ed   retea-interna   bridge    local

eu@Ubuntu2204:~$ docker run -d --network public --name frontend tools
494bd05cba7f1c4f651512102c7b48c0280344d0e2dcafc005eb9ec514e16de8

eu@Ubuntu2204:~$ docker run -dit --name backend --network public tools
docker network connect private backend
5dcb2721b1b38ac29b185dbd5791f24e65b2b797b041871939a293cea7e5246a

docker run -dit --name database --network private tools
a0750ecd47d80f3a9bb9a1f79174eab4a955adbd8b6a6f8021cbe8ddddfe78ad


docker exec -it <nume_container> bash

frontend :
ping backend       # trebuie să meargă 
ping database      # trebuie să eșueze 

backend :

ping frontend      # trebuie să meargă 
ping database      # trebuie să meargă 

database :
ping backend       # trebuie să meargă 
ping frontend      # trebuie să eșueze 
ping 8.8.8.8       # trebuie să eșueze (fără internet) 



