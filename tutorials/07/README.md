---
layout: default
permalink: /tutorials/07/
---

# Network Security

A new startup in Toronto is setting up its office network and asks for your help.

The company has 4 employees, each with a laptop, and 3 servers: a web server and a mail server that must be accessible from the internet, and a NAS (Network-Attached Storage) server used internally for file sharing among employees.

Initially, assume that all laptops and servers are connected to a Wi-Fi network and each device has a public IP address (to simplify).
All employees work exclusively from the office for now.

1. **Securing the Wi-Fi Network:** The company wants a simple setup with an SSID and shared password. However, they also want to let guests use the same Wi-Fi network and password; even though guests are not fully trusted. What Wi-Fi protection mechanism would you recommend?

2. **Controlling Inbound and Outbound Traffic:** The company wants to prevent random internet users from scanning or accessing internal machines. Only HTTP (port 80/443) traffic to the web server, and IMAP (port 143/993) to the mail server should be reachable from the internet. All outbound traffic from internal hosts should be allowed. What security mechanism(s) should be deployed?

3. **Preventing Lateral Movement After a Breach:** The company fears that if an attacker compromises the web or mail server, they might move laterally to access the internal NAS. What network design would mitigate this risk?

4. **Allowing Remote Work Securely:** Now, the company wants employees to access the NAS from home or while traveling. How can employees securely connect to the internal network from remote locations?

5. **Connecting Two Offices Securely:** After expanding to Paris, the company now has an office in Toronto with public servers and a NAS, and  Paris office with employee laptops and a local NAS. Employees from both offices need seamless access to either NAS as if they were on the same local network. What do you recommend to securely connect the two offices?







