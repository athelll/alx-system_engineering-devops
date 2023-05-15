#!/usr/bin/env bash
# configures firewall to redirect port 8080/TCP to port 80/TCP.

# ------run at risk!

# backup
sudo cp /etc/ufw/before.rules /etc/ufw/before.rules.bak

# configuration
sudo ufw allow 8080/tcp
# sudo sed -i "s/COMMIT/*nat\n:PREROUTING ACCEPT [0:0]\n-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80\nCOMMIT/" /etc/ufw/before.rules

# restart ufw
sudo service ufw restart 
