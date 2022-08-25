#!/usr/bin/env bash                                              
# Sets up your web servers for the deployment of web_static      
sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data/
echo "New Content" | tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current

find_str="^\t\}$"
replace_str="\t\}\n\n\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/;\n\t\}"

sudo sed -i "0,/$find_str/s//$replace_str/" /etc/nginx/sites-available/default
sudo service nginx restart
