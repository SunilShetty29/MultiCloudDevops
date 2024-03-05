#!/bin/bash
sudo su
yum update -y
yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service
echo "<!DOCTYPE html><html><body style="background-color:yellow"><h1>Welcome to Harsha Trainings --> Server1</h1></body></html>" >> /var/www/html/index.html
