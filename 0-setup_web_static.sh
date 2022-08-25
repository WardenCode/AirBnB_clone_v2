#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static
sudo apt -y update
sudo apt -y upgrade
sudo apt -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "New Content" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/

find_str="^\t\}$"
replace_str="\t\}\n\n\tlocation \/hbnb_static\/ \{\n\t\talias \/data\/web_static\/current\/;\n\t\}"

sudo sed -i "0,/$find_str/s//$replace_str/" /etc/nginx/sites-available/default
sudo service nginx start
