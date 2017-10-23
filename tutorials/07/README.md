---
layout: default
permalink: /tutorials/07/
---

# Network Security

- if the network is opened to the "outside", anybody could connect to their servers?

[comment] 
- Yes, anybody can scan and connect to servers with a public IP address. 
- However, having a firewall on each side might creates a logical defence parameter that filters out communications that are not coming from the other side. 
- For a better security, A and B could each create a DMZ within their respective network and place all shared servers into these DMZs. 

- someone outside of their network might be able to eavesdrop or hijack their communication?

[comment] 
- yes, however as we saw last week, someone outside A and B network could hijack communication either by being on the routing path or by using DNS or routing attacks. 
- To mitigate that risk risk, A and B could use TLS and DNS-sec to secure application level data exchange. However, if A and B uses multiple applications, it could be tedious to configure TLS for all of them, some might not be necessarily TLS ready. 

- people might suspect that the two are working on super secret project if they see the type of communication they have?

[comments] 
- yes, even if the application layer is encrypted, someone could see who talks to who (IP adresses) and what kind of data they exchange (port). 
- To avoid that, each side could deploy a VPN for the the other side to use. In that case, an attacker could see a bunch of hosts on one side talking to a VPN on the other side. A bit better but far from being ideal. 
- One of the best solution in that particular case is to deploy two IPsec routers on each side. All traffic going from one side to the other could be transparently encapsulated into an IP sec tunnel. With this solution, there is no need to configure TLS at the application level. Encryption and signature occurs at the IP level when the packet arrives at the IPsec router at the edge of the network. 







