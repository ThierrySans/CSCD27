1. Start the network

`docker-compose up -d`

2. Start sniffing with mallory

`docker exec mallory tcpdump -i eth0 -U -s 0 -w - | wireshark -k -i -`

3. Generate traffic from  Alice

docker exec alice curl https://utoronto.ca/