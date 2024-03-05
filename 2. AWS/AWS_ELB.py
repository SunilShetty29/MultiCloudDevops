#AWS ELB (ELastic Load Balancer) #
-----------------------------------------------
	* automatically distributes your incoming traffic multiple targets, such as EC2, containers and IP addresses in 1 or more availablityb zones.
	* It monitors the health of its registered targets and rotes traffic only to the healthy targets.
	* It scales your load balancer capacity automatically it response to changes in incoming traffic.
	BENEFITS :
		* distributes work loads across multiple compute resources such as Virtual Servers. Using a Load balancer increases the availabilty and fault tolerance of your 
		applications.
	Types :
		1. Application Load Balancer :
			* Functions at the application layer, it is a 7th layer of Open Systems Interconnection (OSI) model.
		2. Network Load Balancer :
			* Functions at the 4th layer of the OSI model.
			* it ca handle millions of requests per second.
		3. Gateway Load Balancer :
			* enable to deploy, scale and manage virtual appliances such as firewalls, intrusion detection and prevention systems and deep packet inspection systems.
		4. Classic Load Balancer :
			* distributes incoming application traffic cross multiple EC2 instances in multiple availability zones.
@ Load will be distributed to available healthy Servers @

Steps to Configure ELB :
	1. CREATE 2 SECURITY GROUPS --> 1 SG with ALL TCP and 2 SG with HTTP ports.
		1. Create a security group with config >> VPC = default >> SG --> outbound rules = all tcp >> inbound rules = add rule = all tcp port.
		2. Create a security group with config >> VPC = default >> SG --> outbound rules = all tcp >> inbound rules = add rule = http port.
	2. CREATE 2 INSTANCES WITH USER DATA.
		1. create an instance with created security group 1 (config = all tcp) and 
			* navigate to advance settings >> user data.
				#!/bin/bash
				sudo su
				yum update -y
				yum install -y httpd.x86_64
				systemctl start httpd.service
				systemctl enable httpd.service
				echo "<!DOCTYPE html><html><body style="background-color:yellow"><h1>Welcome to Harsha Trainings --> Server1</h1></body></html>" >> 
				/var/www/html/index.html
			* click on create instance.
			* once after creating an instance copy the public IP and paste it in browser and observe.
		2. create an instance with created security group 1 (config = all tcp) and 
			* navigate to advance settings >> user data.
				#!/bin/bash
				sudo su
				yum update -y
				yum install -y httpd.x86_64
				systemctl start httpd.service
				systemctl enable httpd.service
				echo "<!DOCTYPE html><html><body style="background-color:yellow"><h1>Welcome to Harsha Trainings --> Server1</h1></body></html>" >> 
				/var/www/html/index.html
			* click on create instance.
			* once after creating an instance copy the public IP and paste it in browser and observe.
	3. CREATE A TARGET GROUP WITH CREATED 2 INSTANCES.
		1. Navigate to EC2 >> Load balancing >> Target Groups.
		2. Click on Create Target Group >> Choose Target type --> Select instances option (dont select other IP address & Lambda functions charges may apply).
		3. Enter target group name.
		4. Protocol port --> http 80 default
		5. IPa address type --> IPV4
		6. VPC = def VPC
		7. Protocol version = http1
		8. health checks = dont change any thing and click on next.
		9. available instances = select created instances
		10. include os pending below = click the option.
		11. Review targets = check the instances and Click on create target group.
@ Once target group is created load balancer is not associated with target groups we need to associate the load balancer @
	4. CREATE AN ELB and ASSOCIATE WITH TARGET GROUPS.
		1. click on create load balancer.
		2. load balancer types --> select application load balancer.
		3. create
		4. enter the load balancer name 
		5. scheme --> 2 options available ' internet facing' and 'internal'
			select internet facing option.
			internal option = will use this within the organization.
		6. IPV4 address type --> 2 option available ' IPV4' and 'dualstack' 
			select IPV4 option.
		7. Network mapping = select def VPC and Select all the available subnets
		8. security group = existing = select def, all tcp, http.
		9. Listeners and routing = select target group as created target group.
		10. Create Load Balancer.
	5. TEST THE ELB BETWEEN BOTH THE SERVERS.
		1. Copy the DNS address from created load balancer and paste it in the browser.
		2. refresh the browser multiple times and observe the server switching with respect to the request.
	6. Finally delete all the created security groups, instances, target groups, load balancer.