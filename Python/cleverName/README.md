0. [OPTIONAL] sudo usermod -aG docker $USER
	- adds user to docker group so 'sudo' no longer required /w docker commands
1. ./dockerReset.sh
2. ssh python0@172.16.10.10 (challenege 0)
   ssh python1@172.16.10.30 (challenge 1)

   NOTE: ssh python1@172.16.10.20 (for the server, no need to connect unless troubleshooting) 
