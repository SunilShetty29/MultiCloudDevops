#!/bin/bash

yum update -y
yum install httpd -y
service httpd start
systemctl enable httpd
echo "Welcome to Harsha Trainings" > /var/www/html/index.html