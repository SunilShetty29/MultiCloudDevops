MULTI CLOUD WITH DEVOPS :->
*******************************
CONCEPTS : ->
---------------------------------------------
	1. AWS CLOUD :
		1. Introduction to Cloud
		2. Create an AWS free tier account
		3. AWS Regions and Zones
		4. AWS Console Overview
		5. EC2 :
			Virtual Servers = Imaginary Server which is available in Cloud.
			On-demand Server (instantly we can create the servers)
		6. Key Pairs :
			Cloud Server having Keypairs.
			Extra Authentication
		7. Security Groups :
			Virtual firewall - it is a network security system which will allow and deny the traffic as per the firewall rules.
		8. AMI
		9. Free tier servers and paid servers
		10. Linux
		11. Linux Architecture and Folder Structure
		12. Linux User Management
		13. Linux File Permissions
		14. Linux File Editors
		15. Linux Basic/Advanced/Deployment Commands
		16. Linux Families (Debian and Redhat)
		17. AWS Storages
		18. EBS = BLock Level Storage, We can create 1gb to 16gb data Block by Block and we can attach it to EC2.
		19. S3 = Object Level Storage or Global Storage or Public Storage, We can store any type of files.
		20. EFS = File Level Storage
		21. Glacier = Mainly for backups and Archieve, fast glacier licence.
		22. Snapshots = backup copy or Replica.
		23. AWS Backup = dialy, weekly, monthly and on-demand
		24. CloudWatch = infrastructure monitoring tool
		25. CloudTrail = AWS console monitoring tool
		26. IAM
		27. MFA ('Multi Factor Authentication') = Extra Layer for Security
		28. VPC
		29. VPC Peering
		30. AutoScaling = Maintain and adjust resources for performance. Horizantal = increase EC2 and Vertical = increase compute resources.
		31. RDS ('Relational Database Service')
		32. AWS CLI ('Command Line Interface')
		33. ELB ('Elastic Load Balancer') = App Load balancer
		34. Elastic BeanStalk = We can create environement and deploy the applications
		35. AWS Lambda = service which will operate our infrastructure
		36. Route 53 = It will check the shortest path to access our servers.
		37. Cloud Formation = which will create Infrastructure Automation Service
		38. SNS ('Simple Notification Service')
		39. SQS ('Simple Queue Service')
		40. SES ('Simple Email Service')
		41. EKS ('Elastic Kubernetes Service')
		42. IP addresses (Public, Private and Elastic IP addresses)
	2. MICROSOFT AZURE
    3. GOOGLE CLOUD
    4. LINUX BASICS
    5. GIT
    5. GITHUB
    7. JENKINS
    8. MAVEN
    9. ANSIBLE
    10. DOCKER
    11. KUBERNETES
    12. TERRAFORM
    13. APACHE TOMCAT
    14. GRAFANA
    15. JFROG
    16. PROMETHEUS
    17. SONARQUBE
    18. '15' LIVE PROJECTS

What is DevOps ???
	It is a Set of practices that combines Software Development and IT Operations.
	Where the Multiple Tools are connected to each other to perform automation of all activities.
	It is a Continuous Deployment, Continuous Integration, Continuous Testing and Continuous Monitoring.

                DevOps  Origin  2008

Puppet :->
•	It was one of the old tools used to perform deployments.
•	But it was old tool and not much being used today.
	Developers People develop the code and Create applications.
	Operations  These people will prepare the Infrastructure and Maintain the Infrastructure.

Ex : JAVA PROJECT :->
Server Setup :
•	Admins will do Server Setup  Local Servers, Dev, UAT, Pre-Prod, Production Server. Admins nothing but Operations Team.
 Developers :
•	work on Local Servers.

Install Java on 1000 Servers (Manually) :
	Connect Server  RDP/Putty.
	Login Server  Username & Password.
	Check JAVA installed or Not.
	Copy JAVA software from shared folders.
	Install JAVA.
	Set Environment Variables.
	Reboot or Restart the Server.
	Ex : 2 – 3 Years  30 Mins
	 15 Mins
	10 * 1000 = 10000 Mins
	Ticketing Tools  JIRA, Service Now, BMC Remedy
	SLA (Service Level Agreement) timeline
	 P1  1 Hr
	 P2  4 Hrs
	 P3  24 Hrs
	 P4  48 Hrs
KPI  (Key Performance Indication)

Install Java on 1000 Servers (Automatically) :->
	Depends upon Servers requirements we will prepare Inventory Group.
	To install JAVA at a time we will run Playbook (automation) yml script
	Why should I go with ANSIBLE  IDEMPOTENCY
	Installed server are not disturbed by ANSIBLE.

INTODUCTION TO CLOUD COMPUTING :->
	Cloud Computing is an On-Demand availability of Computer System resources, Storage and Computing Power, without direct active management by the User.
	Sprint ==> Timeline ( 1week to 1 month)
	User  will access the Cloud or Cluster with the help of Internet Connection).

# CLOUD ADVANTAGES #
1. Cost and Time Saving
2. Ease to use
3. Automation
4. High Performance
5. Largest Cloud Infrastructure

* DATA CENTER or SERVER ROOM or HUB ROOM or NETWORK ROOM ==> Servers, Network, Switches, Routers, Backup devices, Load balancers.

# Example to maintain project manually without Cloud
1. POC (Proof of Concept) --> 45 days
2. Configure 3 tgypes of Servers ' 2 Dev Servers ' [used for 30 days], ' 2 QA Servers ' [used for 31-40 days] and ' 2 Prod Servers ' [used for 41-45 days]
3. Need to procure licence
4. Require 1 admin
5. Require Server room
6. Require Central AC
7. Require Security
8. Require Network

# Example to maintain project via Cloud
1. POC --> 45 days
2. Servers :
	1. 2 Dev Servers
	2. 2 QA Servers
	3. 2 Prod Servers
3. No license reuired
4. No Server room required
5. No admin required
6. No Central AC reuired
7. No Security
8. No Network

# CLOUD COMPUTING AT GLANCE :
	There are 5 Essential Characteristics :
		1. On - demand
		2. Broad Network access
		3. Resource Pooling
		4. Rapid Elasticity
		5. Measured Service
	
	There are 3 Service Models :
		1. 

AMAZON WEBSERVICES :->

    Introduction:->
        Amazon Web Services is a Cloud service from Amazon, which provides Services in the form of building blocks can be used to Create and deploy any type of
		application in the Cloud.
        These Services or building blocks are designed to work with each other, and result in applications which are sophisticated and highly scalable.
        Each type of service in this "What is AWS" blog is categorized under a domain, the few domains which are widely used are:
            1. Compute :->
                This domain includes services related to compute workloads.
                It includes the following services.
                    1. EC2 (Elastic Cloud Compute)
            2. Storage:->
                This domain includes services related data storage.
                It includes the following services.
                    1. S3 (Simple Storage Service)
                    2. EBS (Elastic Block Store)
                    3. Amazon Glacier
            3. Database :->
                This domain is used for Database related workloads
                It includes
                    1. Amazon RDS
            4. Network and Content Delivery :->
                This domain is used for isolating your Network infrastructure and content delivery is used for faster delivery of content.
                It includes
                    1. Amazon VPC
                    2. Amazon Route 53
            5. Management Tools :->
                This domain consists of services which are used to manage other services in AWS.
                It includes
                    1. AWS CloudWatch
                    2. AWS CloudFomation
                    3. AWS CloudTrail
            6. Security and Identity Compliance :->
                This domain consists of services which are used to manage to authenticate and provides security to your AWS resources.
                It consists of
                    1. AWS IAM
            7. Messaging :->
                Services which are used for Querying, Notifying and Emailing messages.
                It includes
                    1. Amazon SOS
                    2. Amazon SNS
                    3. Amazon SES

AMAZON ELASTIC CLOUD COMPUTE :->
    * Provides scalable computing capacity in the AWS Cloud.
    * Using EC2 eliminates your need to invest in hardware upfront, so you can develop and deploy applications faster.
    * You can use EC2 to launch as many or as few virtual servers as you need, configure security and networking and manage storage.
    * Enables you to scale up or down to handle changes in requirements or spikes in popularity, reducing your need to forecast traffic.
    Features :->
        1) Virtual computing environments >> Instances.
        2) preconfigured templates for instances >> Amazon Machine Image AMI's.
            that package the bits you need for your server (including the OS and additional software).
        3) Various configurations of CPU, Memory, Storage, and Networking capacity for your instances known as Instance types.
        4) Secure login information for your instances by using Keypairs (AWS stores the public key, and you store the private key in a secure place).
        5) Storage volumes for temporary data thats deleted when you stop or terminate your instance, known as Instance Store Volumes.
        6) Persistent storage cvolumes for your data using AMAZON ELASTIC BLOCK STORE (Amazonn EBS) known as Amazon EBS volumes.
        7) Multiple physical locations for your resources, such a s instances and Amazon EBS volumes known as Regions & Availability Zones.
        8) A firewall that enables you to specify the protocols, ports and source IP ranges that can reach your instance using security groups.
        9) Static IPV4 addresses for dynamic cloud computing known as Elastic IP Addresses.
        10) Metadata known as tags that you can create and assign to your Amazon EC2 resources.
        11) Virtual networks you can create that are logically isolate from the rest of the AWS cloud and that you can optionally connect to your own network known 
		as
		Virtual Private Cloud (VPC's).

SIGNUP FOR AWS :->
---------------------------------------
    * When you signup for AWS your AWS account is automatically signed up for all services in AWS, including Amazon EC2. You charged only for the services 
	that
	you use.
    * With Amazon EC2, you pay only for what you use. If you are a new AWS customer, you can get started with Amazon EC2 for free.
    * If you already have AWS account already, skip to the next task. If you dont have an AWS accoun, use the following procedure to create one.

    To create AWS account :->
        1) Open aws.amazon.com
        2) Choose Create AWS Account
            Note :- If you previously signed in to the AWS Management Console using AWS account root user credentials, Choose sign in to a different account.
                        If you previously signed to the console using IAM credentials, choose Sign-in using root account credentials. Then choose "Create a new AWS
						account".
        3) Follow the Online Instructions.
            a) Part of Sign-up procedure involves receiving a phone call and entering a verification code using the phone keypad.
            b) Sign-in into aws console by using aws account credentials that is account id and password in aws console signin page.

CREATING EC2 INSTANCE :->
--------------------------------------------
    1. Select EC2 service and Click on that.
    2. Click on Launch instance
    3. Choose AMI :-> Select any AMI from list of AMI's Here I select ubuntu 16 version.
    4. AMI simply called as OS for our launching machine.
    5. Click on Next.
    6. Choose Instance type:-> Select Instance type "t2.micro" for FREE TIER ELIGIBLE.
    7. Click on Next Configure details.
    8. Number of Instances :->
            Enter the Number for how many instances are launched.
    9. Network :->
            Select the type to launch that instances.
    10. Subnet :->
            Select the subnet to launch that instances.
    11. Auto Assign Public IP :->
            Use subnet setting Enable for assign public IP address to that instance.
    12. IAM Role :->
            Select IAM Role for that instance.
    13. Shutdown Behavious :-> Stop
    14. Click on Next Add Storage
        1. Enter the required memory size, volume type is "GP2"
        2. Click on Add tags.
        3. Add the tags :-> ZEnter Key and Value pair.
    15. Next Configure Security Group.
        1. By default "ssh" prptocol is included in that security group.
        2. Add required protocols by Click on Add Rule.
        3. Type :-> Select Protocol,
        4. Port Range :-> Enter Port number or Range.
        5. Source :-> Select from anywhere option.
    16. Click on Review and Launch.
    17. Click on Launch.
        1. Key pair :-> Select existing Key pair or Choose new key pair options.
        2. Enable Acknowledgement.
        3. Enter key pair name and Click download key pair.
        4. Click on Launch Instances.
        5. Click on View Instances.
    18. CONNECT TO INSTANCE :->
        1. Open gitbash in private key download location that is downloads or open Putty.
        2. Select particular EC2 instance which instance do you want to connect and Click on connect option.
        3. Copy Example ssh command and Click on Close.
        4. Paste in gitbash and make Enter.
        5. Enter Yes.
        6. Connected to EC2 instance and you can do any operations on that EC2 instance terminal.
    19. CREATE TEMPLATE FROM INSTANCE :->
        1. Select EC2 instance and goto actions and select Create Template from Instance option.
        2. Launch Template :-> Enter name for that template.
        3. Click on create template from instance.
    20. INSTANCE STATE :->
        1. Select EC2 instance and goto actions and select instance state option.
        2. Select start if instance is stopped and do you want to start.
        3. Select stop if do you want  to stop the instance.
        4. Select reboot option for reboot your machine.
        5. Select terminate for terminate your instance or machine
    21. CREATE IMAGE FROM INSTANCE :->
        1. Select instance and goto actions and click on image and select create image option.
        2. Enter image name and Click on Create image.
    22. CHANGE SECURITY GROUP :->
        1. Select instance goto actions and Click on Network and Select change Security Group option.
    23. CLOUD WATCH MONITORING :->
        1. Select instance goto actions and click on cloud watch monitoring option and select Enable detailed monitoring.
        2. Click on yes Enable.
        3. Click on close.
    24. INSTANCE SETTINGS :->
        1. Instance settings used for attach to auto scaling group, attach/replace IAM role, change termination protection, View or change user data, change shutdown
		behaviour.......etc
        2. After completion of work terminate the instance by using above terminate option.

ELASTIC BLOCK STORAGE :->
    * Provides BLOCK LEVEL STORAGE volumes for use with EC2 instances.
    * EBS volumes are highly available and reliable storage volumes that can be attached to any running instance that is in the same Availability zone.
    * EBS volumes that are attached to an EC2 instance are exposed as Storage volumes that persist independently from the life of the instance.
    * EBS is recommended when data must be quickly accessible and requires long-term persistance.
    * EBS volumes are particularly well-suited for use as the primary storage for file systems, databases, pr for any applications that require fine granular updates and
	access to raw, unformatted, block-level storage.
    * EBS is well suited to both database-style applications that rely on random reads and writes, and to throughput-intensive applications that perform long,
	continuous reads and writes.
    * You can attach multiple volumes to the same instance within the limits specified by your AWS account.
    * Your account has a limit on the number of EBS volumes that you can use, and the total storage available to you.

* Ubuntu is not allowed EFS in Some regions.

Monitoring Tools :->
    *


IDENTITY and ACCESS MANAGEMENT (IAM) :->

VIRTUAL PRIVATE CLOUD (VPC) :->
	* Isolated Virtual Network.

TASK 1_EBS Volumes :->
    1. Create an instance with default volume.
    2. Create Multiple Files and Folders.
    3. Delete the Server and take the Snapshot of the Volume.
    4. Take the Snapshot for Available Volume.
    5. Delete the Volume.
    6. Create a Test Instance with Default Volume.
    7. Check the Files and Folders Available or Not ??
    8. Stop the Server and detach the New Volume and Attach the Old Valume.
    9. Connect the Server and Check the Files and Folders.

Task_VPC :->
	1. Create a VPC (Custom).
	2. Create an Instance with Public Subnet.
	3. Create an Instance with Private Subnet.
	4. Try to Access the both Instances via Putty/MobaXterm/Gitbash.
		Note : Instance with Privaye Subnet should through Network Error.
Task_VPC Peering Connection :->
	Sub Task 1 :-> Create a Peering Connection between default VPC and Custom VPC with in the Same AWS account.
	Sub Task 2 :-> Create a Peering Connection between Custom VPC from your A/C to Cutom VPC in another A/C.
	Sub Task 3 :-> Create a Peering Connection between default VPC from your A/C to default VPC in another A/C.
	Sub Task 4 :-> Create a Peering Connection between Custom VPC from your A/C to default VPC in another A/C.

@ NAT gateway is reuired to establish communication between Private Subnet and Public Subnet @
@ Don't delete default VPC @
@ customization is possible for both IPV4 and IPV6 CIDR block @
@ When we select Custom VPC >> auto assign Public IP will be automatically disabled >> enable the option manually @
VPC and the internet

Steps to Create VPC :->
1. Services >> Network and content Delivery >> VPC.
2. Click on Your VPC's and Check any VPC's is available or not ??
	* Every Region will have one default VPC.
3. Click on Create VPC.
4. Resources to Create
	* VPC only
	* VPC and More >> Combination of VPC and Subnets.
5. Name tag auto generation >> enable >> Enter Name.
6. IPV4 CIDR block >> We can Customize the IP addresses range.
7. IPV6 CIDR block >> disable.
8. Tenancy >> default or dedicated.
	* Tenancy is nothing but a dedicated space virtually.
	* Please select default option because dedicated is not a free of cost.
9. Number of Availability Zones --> 2 (We can select any option).
10. Number of Public Subnets --> 2  (We can select any option).
11. Number of Private Subnets --> (We can select any option).
12. NAT gateway >> None.
13. VPC end points >> Select S3 gateway.
14. DNS options >> enable the both DNS hostnames and DNS resolution.
15. Create VPC.
16. View VPC's.
17. goto your VPC's and Check the created VPC.
18. Navigate to Subnets and Check the created Public and Private Subnets.
19. Create an Instance with Public Subnet.
	1. While launching Instance.
	2. Network Settings >> edit >> Select custom VPC >> Select Public Subnet >> Create a Security group >> Launch Instance.
20. Create an Instance with Private Subnet.
	1. While launching Instance.
	2. Network Settings >> edit >> Select custom VPC >> Select Private Subnet >> Create a Security group >> Launch Instance.
21. Access the Public Server via Putty / MobaXterm / Gitbash.
22. Access the Private Server via Putty / MobaXterm / Gitbash.
	@ We can't access the Server with Private Subnet because VPN is required to Connect the Private Server @
	@ Usually Server with Private Subnet is used internally within Organization @


Steps to Create VPC peering :->
1. We have two VPC >> 1 - default VPC and 2 - Custom VPC (which created by own).
2. try to establish the connection between two VPC.
3. Select Peering Connections.
4. Click on Create Peering Connections.
5. enter Name.
6. VPC ID requester >> Select default VPC.
7. Select another VPC to peer with >> Select My account.
	@ We have two options My account and Another account @
	@ if you select another account you need to enter the another AWS account id.
8. Region >> Select this Region ( IP adresses are different if the VPC are in same region).
	@ We have two option "this region" and "another region" @
	@  if you select another region you need to enter VPC id and select the Region @
9. Acceptor VPC id >> select custom VPC.
10. Click on create peering connections.
	@ Peering Connection is created but we need to accept the connection to establish communication between two VPC @
11. Select the created peering connection >> actions >> accept request.
	@ Request is accepted and Connection is established hut Traffis is not allowed @
@ To enable the Traffic for peering connection we need to enable 'Route Tables'
12. To enable Route Tables :
	1. Select Route Tables.
	2. Select default VPC >> actions >> Edit Routes.
	3. Enter the custom VPC range.
	4. Tagret >> Select VPC peering.
	5. Save changes.
	6. Select custom VPC >> actions >> Edit Routes.
	7. Enter the default VPC range.
	8. Tagret >> Select VPC peering.
	9. Save changes.
13. finally remove all the created VPC, Subnets, peerings connection and Route Tables.
@ Free Tier account >> Server Communication is not allowed ( it is chargeble) @
@ North Virginia region is working for VPC peering @


AWS AUTO SCALING :->
    *

Steps to Create Auto Scaling :->
1. Services >> Managing and Governance.
2. Click on Auto Scaling or Navigate to EC2 >> Auto Scaling >> Auto Scaling groups.
3. Click on Auto Scaling Group.
4. Enter Name (any name).
@ To Create "Auto Scaling Group" we need a "Template" @
@ Template --> Image, Template required "AMI" to add the Servers @
5. Click on Launch Instance.
    1. Click on Create Template and Enter the Name and description.
    2. Application and OS image.
        * Select recently launched AMI or Browse AMI.
    3. Select the AMI.
    4. Keypair --> Select Existing or Create New Keypair.
    5. Network Settings --> Select Existing Security Group.
    6. Volume --> Select default Volume.
    7. Click on Create Template.
6. Select the Created Template.
7. Version --> Select any option (Latest or default or 1).
    * Select the option as "1".
8. Click on Next and under VPC --> Select default VPC.
9. Availability Zones and Subnets --> Select all Subnets and Click on Next.
10. Load Balancing --> There are 3 options (No Load balancer or Attach to an Existing Load balancer or Attach to New Load balancer)
    * Select "No Load balancer" option because for remaining options charges may apply.
11. VPC Lattice Integration --> 2 options (No VPC Lattice Service or Attach to VPC Lattice Service).
    * Select "No VPC Lattice Service" because for remaining options charges may apply.
12. Health Checks --> Set 300 secs.
    * Health Checks is nothing but a "GRACE PERIOD" --> When Server is down another instance will be created with in the grace period (with in 300 secs).
13. Monitoring --> if you want CloudWatch --> Enable it. (but charges may apply). So dont enable the CloudWath services and Click on Next.
14. Group Size --> desired capacity = 2 and Minimum desired capacity = 2 and Maxium desired capacity = 5.
    * both desired capacity and Minimum desired capacity values should be same.
    * These values will change depends upon the Project Requirement.
15. Auto Scaling (optional) --> dont change anything let it be default value.
16. Instance Maintainance policy --> dont change anything let it be default value.
17. Instance Scale-in Protection --> dont enable (charges may Apply) and Click on Next.
18. Add Notifications --> Click on Add Notifications --> SNS is reuired.
19. Create a Topic.
20. Send a Notifications to Topic --> Name (Group Name).
21. with these receipents to --> Enter Mail id (Enter Group mail on Live).
22. Event Types.
    - Launch
    - Terminate
    - Fail to Launch
    - Fail to Terminate
23. Click on Next and Enter Tag Name and Value (Automatic Instances will be created with tag names).
24. Enable Tag New instances and Click on Next.
25. Create a Auto Scaling Group.
26. Two Instances will be created automatically.
27. To Test Auto Scaling --> delete 1 Server and Check.
28. Terminate the both Instances and Check.
@ To check the Positive Scenario we need Threshold So we are Checking with Negative Scenario @

Task :->
1. Create an Auto Scaling Group with desired capacity = 2 and Minimum desired capacity = 2 and Maxium desired capacity = 5.
2.  To Test Auto Scaling --> delete 1 Server and Check.
3. Terminate the both Instances and Check.

VIRTUAL SCALING :-> "INCREASE COMPUTE SERVICES (RAM, CPU, HDD)"
    if you want to perform Virtual Scaling you need to stop or shutdown the Server first.

1. Select 1 instance and Stop instance.
2. Select Server --> Actions --> Instance Settings --> Change Instance Type.
3. Select t2.medium --> Charges may Apply.
4. Start the Server and Check the Performance.
    "THIS IS A FAILED CONCEPT"
    # BECAUSE WE NEED TO STOP THE SERVER --> IN LIVE WE SHOULD NOT STOP THE SERVER #


AMAZON RDS (RELATIONAL DATABSE SERVICE) :->
What is Database :->
	It is and organized collection of structured information, or data, typically stored electronically in a computer.
	A database is usually controlled by a "Database Management System (DBMS)".

What is Amazon RDS :->
	It is a managed SQL database services provided by AWS.
	Supports an array of database engine to store and organize data.
	It also helps in relational database management tasks like data migration, backup, recovery and patching.

RDS Supports 8 types of Engines :
	1. Aurora (MySQL Compatible) : Charges may apply
		Amazon Propritary database.
	2. MySQL : Free
	3. PostgreSQL : Free
	4. Microsoft SQL Server
	5. Aurora (PostgreSQL Compatible) : Charges may apply
	6. MariaDB : Free
	7. Oracle
	8. IBM Db2

Why we need to choose RDS :
	It is a cloud-based platform that makes it easy to set up and operate a relational database in the cloud.
	In Real time we wont get chance to create RDS --> because Architects will Manage this RDS.

How to create MySQL Database with Amazon RDS :
	1. Search with RDS.
	2. Query Editor --> We can edit the data.
	3. Click on Create Database >> Choose a database method --> 2 options is available. ( Select Standard Create)
		1. Standard Create
		2. Easy Create. --> it is very easy to create like by next next ...,
	4. Engine Options --> select MySQL
	5. Observe the Engine Version.
	6. Template >> Select Free tier.
	7. When we select free tier availability and durability will be greyedout --> Not available for free tier
	8. Observe the engine version.
	9. dB instance identifier --> we can give any name.
	10. Master username --> admin (don't change any thing).
	11. Manage master  credentials in AWS secret manager  --> don't enable >> charges may apply.
	12. Auto generate password --> don't enable.
	13. Master password & Confirm master password --> enter any password.
	14. Instance Configuration --> When we are creating a dB backend 1 instance will be created with t3.micro configuration. (So dont change any thing)
	15. Storage :
		1. storage type --> we have 2 options 'General purpose SSD (gp2)' and 'Allocated Storage' (we can customize both storages).
		2. storage auto scaling --> if u enable upto 1000 GB it will increase >> if u modify the value (charges may apply) so dont enable.
	16. Connectivity :
		1. Compute resources --> we have 3 options ' dont connect to EC2' , 'connect to an EC2 compute resources' and select defualt dont connect EC2.
		2. Ntwork type --> 2 options available ' IPV4 ' and ' dual stack mode ' --> Select IPV4.
			dual stack mode = combination of IPV4 and IPV6.
		3. VPC --> Select default VPC. (if u want u can use custom VPC).
		4. dB subnet group --> select default.
		5. Public access --> select yes option.
		6. VPC security group firewall --> 2 option are there 'choose existing' and 'create new' >> select existing security group (All TCP, default).
		7. Availabilty zone --> select No proxy.
		8. RDS proxy --> dont enable any thing.
		9. Certificate Authority - optional --> dont select anything.
		10. Database Authentication --> select Password Authentication.
		11. Click on Additional settings --> Database port should be 3306.
	17. Monitoring --> if u want we can enable the monitoring but charges may apply.
	18. Click on create database.
	19. Check backend server is created or not ??
	@ We need 1 interface to check the database @
	20. Open the database and Copy the Endpoint URL.
	21. Download the MySQL workbench.
	22. Open MySQL workbench >> MySQL Connections >> Click on '+' symbol.
	23. Enter any name in connection name.
	24. Connection method --> select standard (TCP/IP).
	25. Hostname --> Paste endpoint URL.
	26. username --> admin.
	27. password --> enter the created password.
	28. Click on Test connection and After SQL connected successfully. Click on OK.
	29. Click on OK in setup new connection screen.
	30. One menu will be observed under MySQL Connections.
	31. Click on the Menu under MySQL Connections.
	32. Now u can create databases and u can practice.
	33. Once practice completes --> Finally delete the database from actions.

# for example take Employee data --> Store in a structured format.
# data is arranged in rows and columns format
# Name, EMP ID, Role, Department



AWS CLI  ( Command Line Interface ) :
	without login to the AWS console we can check all the reports of AWS console.

	AWS CLI Configuration :
		1. goto browser and search with --> download AWS CLI for windows.
		2. Open the first link >> scroll down and expand the Windows option.
		3. Click on the .msi url >> file will get downloded.
		4. Open the downloaded file and install the CLI.
		5. Open Command Prompt >> type aws --version (To check the installed aws version)
		@ To perform AWS CLI --> we need 1 IAM user @
		@ We need to generate 1 Access key @
		6. Open AWS console >> Navigate to IAM and check anu users available or not.
		7. if u already have created IAM user open the user if not Create an IAM user.
		8. Open existing user >> Navigate to Security Credentials >> Access key.
		9. Click on Create Access Key :
			1. use case --> select CLI option and Acknowledge the agreement and click on next.
			2. open the access key and copy the access key.
			3. Open Command prompt and type 'aws configure' and press enter.
			4. paste the copied access key and press enter.
			5. copy the secret access key from console and paste it in the cmd.
			6. Region --> default region name [us-east-2] --> dont change any thing --> press enter.
			7. Outpt --> default output format [None] --> dont change any thing --> press enter.
			8. goto S3 buckets and check whether any S3 buckets available or not ??
			9. In cmd --> type 'aws s3 ls' and press enter.
			10. type 'aws ec2 describe-instances' and press enter (it will list all the instances available in aws console with details).
			11. type 'aws iam list-users' and press enter (it will give list all the users present in aws console with details).
			@ for the list of CLI commands  please use this link 'https://www.bluematador.com/learn/aws-cli-cheatsheet' @


AWS ELB (ELastic Load Balancer) :
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

ELASTIC BEAN STACK :
	* It is an AWS-managed service for Web Applications.
	* It is a pre-configured server that can directly take up your application code and environment configurations and use it automatically provision and deploy the
	required resources with in AWS to run the Web applications.
	* Without using 'Waterfall' or 'Agile' methods we can deploy the code by using 'BeanStalk'.

Waterfall :
	code will be developed in sequentialy way.
		developers develop the code in local repo.
		From local repo code will move to different environments (dev --> QA --> Prod).
	Here we wont use any devops tools
	Old trend currently no one is using this method.
	In this method development wont go forward.
	In case any bugs raised in the middle of the code. whole development need to stop for that.

Agile :
	First piece of code will deploy once after testing completed again they will deploy the code.
	developer develop the code in thier local git repo and they will push the code into remote repo.
	Once the development and testing completed then only we will push the code into remote repository.
	Remote repo to deploy the code via jenkins with help of plugin.
	By using Jenkins we will deploy the code.
	Raw code will not be understand by app server so we use Maven to convert 'RAW code' to 'war file'.

HOW ELASTIC BEANSTALK WORKS ??? :
	* It is a fully managed service provided by AWS that makes it easy to deploy and manage apps in the cloud without worrying about the underlying infrastructure.
	* First create an app and select an environment, configure the environment and deploy the application.
		There are 4 stages :
			1. CREATE APPLICATION
			2. UPLOAD VERSION
			3. LAUNCH ENVIRONMENT
			4. MANAGE ENVIRONMENT
			* Manage Env requests to update new version.
			* Upload version will update the new version and push to manage env.
	* Supports apps developed in 'Go, Java, .Net, Node.Js, PHP, Python, Ruby' .
	* When you deploy your app, Elastic BeanStalk builds the selected supported platform version and provisions one or more AWS resources such as Amazon EC2
	instances to run your app.
	* Once we created this service backend 1 instance will be created (t2.micro and t3.small).

ON-INSTANCE CONFIGURATION :
	* There are 5 Stages in config :
		1. Code
			Focus on building your application.
		2. HTTP Server
		3. App Server, Language Interpretor
		4. OS
		5. Host
	* Configures each EC2 instance in your env with components necessary to run apps for the selected platform. No more worrying about about logging into 
	instances
	to install and configure your application stack.
	* Provided and managed by Elastic BeanStalk.

DEPLOY YOUR APPLICATION :
	1. Open AWS console >> Search Elastic BeanStalk.
	2. Click on Applications >> Click on Create application.
	3. Enter app name, description and tags and Click on create application.
	4. Open the created application >> Click on create environment.
		1. Environment tier --> 2 option available, Please select web server env.
			1. Web Server Env --> To access the app via internet.
			2. Worker Env --> To access the app via internal ogranization.
		2. Application Information --> Observe the details.
		3. Enviroment Information
			1. Env Name --> Enter any name.
			2. domain --> Used to access our application
				Click on Check availablity >> domain will come automatically.
			3. Env description --> Enter the description.
		4. Platform
			1. Platform type --> 2 options available >> ' Managed Platform' and ' Custom Platform' >> Please select managed platform.
			2. Pltform --> there is a list of available langugaes supported for Elastic BeanStalk >> We need to select the language depends upon the app language >> 
			Here
			we are selecting 'PHP' because coding is not there in PHP and we can deploy live apps quickly and easily.
			3. platform branch --> PHP 8.2 running on 64 bit AC 2023.
			4. platform version --> 4.10 recommended >> if u want we can change the version.
		5. Application code --> 3 options are available
			1. Sample app (Select this option) --> it will create a sample application.
			2. Existing version --> if u have already code so u can enter the version and code path.
			3. upload your code --> we need to upload the code from local path (war file) or s3 bucket URL and we need to enter Version and Labels.
		6. Presets : Please select Single instance option because option is free.
			1. Single instance
			2. Single instance (using spot instance)
			3. High Availablity
			4. High Availablity (using spot and On-demand instance)
			5. Custom configuration.
		7. Click on Next
		8. Service access --> service role
			1. create and use new service role (select)
			2. use an existing service role.
		9. by default 1  one will be observed --> if u want we can modify or u can use exiting role.
		10. Key pair --> select existing key pair.
		11. To create role :
			from IAM create a role and select EC2, policy --> elastic web tier, select trusted entities and create a role.
		12. select the created role and click on Next.
		13. select default VPC.
		14. Select all the listed subnets.
		15. db subnet --> not required because we are not using any databases for this app. if ur using db so u can enable the db subnet.
		16. COnfigure Instance Traffic and Scaling :
			1. Root volume --> root volume type --> container (default) 'we can change if needed'.
			2. remaining options let it be dont change anything.
		17. Amazon Cloudwatch Monitoring --> 5 mins
		18. Instance Metadata services --> deactivated (if u enable charged may apply)
		19. EC2 security group --> select security group.
		20. Auto Scaling Group --> we can enable if needed.
		21. Click on Next.
		22. Monitoring --> health reporting --> basic and enhanced (select enhanced option).
		23. Email Notifications --> u need to enter group mail internally within org.
		24. Proxy Server --> nginx (default)
		25. Click on Next and Click on Submit --> one PHP app deployed.
		@ One Elatic IP is also created at the backend @
		26. Open Environment and copy the domain and paste it in browser and observe the PHP app deployed.
		27. Finally delete all the created configurations.

AWS LAMBDA FUNCTION :
	* it is a compute service that lets you run code without provisioning and managing servers.
	* Lambda runs your code on a high availability compute infra structure and performs all of the administration of the compute resources, including server and OS
	maintainance, capacity provisioning and automatic scaling and logging with lambda. All you need to do is supply your code in one of the language run time that
	lambda.
	* Used to Start and Stop the EC2 instances.
	* lambda uses python code.
	* example : Keep EC2 running only Mon-Fri 6 AM.
	* It is a service which whill operate Infrastructure.

CREATING AWS LAMBDA :
	1. Open Console >> Launch 3 instances with default settings (3 instances is only for example purpose. We can run N number of instances).
	2. Some script will run in background.
	3. Script : we are using python code. ('That is called boto code').
		import boto3				# 'boto 3' is a python library
		region='us-east-2'			# we need to enter the region we are creating AWS lambda
		instances=['Instance ID 1', 'Instance ID 2', 'Instance ID 3']	# we need to enter created 3 instances id's
		ec2=boto3.client('ec2',region_name=region)

		def lambda_handler(event,context):
			ec2.stop_instances(InstanceIds=instances)
	4. Search lambda >> functions >> click on create function.
		We have 3 options :
			1. Author from scratch (Please select this option)
			2. Use a Blueprint
			3. Container Image
	5. Basic Information :
		1. Enter function name.
		2. Runtime --> Select python 3.11
	6. Permissions --> change default execution role --> navigate to execution role --> We have 3 options (' create new role with basic lambda expression', 'use an
	existing role', 'create new role from AWS policy template'). Select ' create new role with basic lambda expression'.
		1. dont change any settings.
		2. Navigate to Advance settings
		3. dont change anything. and click on Next.
	7. Create function and Navigate to code.
	8. Remove the default code and paste the python code.
	9. click on deploy.
	10. goto configuration >> permissions >> select IAM role created.
	@ if IAM role is not available. Create an IAM role @
	11. Open IAM role >> required full permissions >> Add permissions >> attach policy >> select EC2 full permissions and adminstrator access >> click on add
	policy.
	12. Now schedule lambda --> for that we need ClodWatch --> Events >> event rules >> event buses >> create rule >> enter name and description  >> select 
	default
	event bus >> rule type >> rule with event pattern schedule >> select schedule >> continue to create rule >> schedule pattern >> A free grained schedule that runs
	>> cron pattern >> Enter the timings depends upon ur current time (Mins=15, hours=6, day of month=?, month=*, day of week=tue, year=*) >> change local time
	zone >> adjust time as per requirement >> Next >> Select target >> lambda function >> select function name (while scheduling region may change sometimes so
	we need to change the region manually) >> next >> next >> Change local time >> Create rule >> Navigate to EC2 and Observe the created instances state.
	@ We have Cron Pattern examples from 'https://crontab.guru.com' website @
	13. Create the same lambda function for start service @ replace 'ec2.stop_instances(InstanceIds=instances)' this line with 
	'ec2.start_instances(InstanceIds=instances)'
	@
	14. Open functions >> Actions >> delete the functions.
	15. delete the created servers.
	16. IAM roles and CloudWatch schedules are NOT MANDATORY to delete.


AWS ROUTE 53 :
    * It is highly available, reliable and scalable cloud DNS web services globally.
    * Purpose is to provide an extremely reliable and cost effective way for developers and business to route end users effectively and successfully to internet
	applications.
    * 53 --> DNS port number.

MAIN FUNCTIONS :
    1. Register domain names.
	2. Route internet traffic to the resources for your domain.
	3. Check the health of your resources.

@ Real time we wont get chance to create Route 53 @
@ We need 1 instance to create Route 53 @

Create an Instance :
	1. t2.micro
	2. 2nd AMI
	3. Select an existing key pair
	4. Network Settings >> select existing security group.
	5. Advance Settings >> User data ( used to deploy an app and host a website).
	6. USER DATA :
		#!/bin/bash
		yum update -y
		yum install httpd -y
		service httpd start
		systemctl enable httpd
		echo " WELCOME SUNIL " > /var/www/html/index.html
	7. launch instance.
	8. Copy and paste the Public IP address in any browser.

Create a Route 53 :
	1. Search Route 53 >> Registered domains >> Click on Registered domains.
	2. Search for domain >> Search with random domain and check the domain available or not.	# but charges may apply
	3. Navigate to Route 53 >> Hosted zones >> create hosted zone.
	4. Configuration :
		1. enter any domain name and description.
		2. Type >> We have 2 options 'public' and 'private'.
			select 'private' option because we dont have real registrations.
			@ if u have a real domain u can select public option @
	5. VPCs to associate with Hosted Zone :
		1. Region --> any region (Mumbai).
		2. VPC --> default VPC
	6. Click on create Hosted zone.
	@ We need to create one record to Map our IP address @
	7. Click on Create Record.
	8. Record name --> enter any name.
	9. Value --> Enter the created instance public IP address.
	10. Record Type --> list of option available --> select ' A Routes traffic to an IPV4 address and some AWS Resources '
	11. Routing Policy --> We can customize the policy --> select ' Simple Routing '
	12. TTL Seconds --> 300 (default value)
	13. Click on Create Records.
	14.

AWS SQS:
Configuring SQS :
	1. We need queue for SQS.
	2. Click on create queue
	3. Details :
		1. Queue type --> 2 options available ' Standard' and 'FIFO' >> Select Standard option.
		2. Enter any name.
	4. Configuration : dont change anything. Let it be default values.
	5. Encryption :
		1. Server Side Encryption = Enabled
		2. Encryption Key Type = Amazon SQS Key (SSE-SQS)
	6. Access Policy :
		1. Choose method --> 2 options available 'Basic' and 'Advanced'  >> Select Basic option.
	7. Retrieve Allow Ploicy = disabled
	8. Dead-letter Queue = disabled.
	9. Enter the tag name and Click on Create Queue.
	10. Create 1 lambda function (SQS requires) :
		1. Select Use a blueprint option.
		2. Blueprint name = Process message in an SQS queue.
		3. Enter function name.
		4. Runtime = nodejs18.x (by default this will selected automatically)
		5. Policy Template = Amazon SQS poller permission (default)
		6. SQS Trigger >> SQS Queue >> Select the created queue.
		7. Active Trigger = dont enable this (used for transaction messages will be processed automatically).
		8. Batch size = 10
		9. Click on create function name.
	11. SQS option should be visible after opening the lambda function.
	12. Click on SQS option --> SQS will be disabled because we are enabled the Active Trigger while creating lambda function.
	13. Naviagte to  Queues and Create 10 requests.
	14. Open the created queue and Click on Send test messages.
	15. Enter the message body and Click on Send message (like same create 10 requests).
	16. Now we need to Process the created requests.
	17. Open the created lambda function and Click on SQS and Select the Trigger >> Edit >> Enable the Active Trigger option and Save.
	18. Once SQS is enabled --> Message requests should become 0 in Queue.
	19. We can check requests processed or not with the help of cloudwatch.
	20. Navigate to Cloudwatch >> logs >> Log groups.
	21. Search with created SQS and check the logs.
	22. Finally delete all the created functions and Queue.
@ We can process bulk transactions @
@ For every transactions backend SQS service is configured in Real time @

# SHELL SCRIPTING #
==================
what is scripting :
	1. Group of commands to Perform tasks.
	2. scripting is a way of providing instructions to a computer so you can tell it what to do and when to do it.

What is Shell Scripting :
	1. A shell script is a computer program designed to be run by the Unix/Linux shell.
	2. A shell is a command-line interpreter and typical operations performed by shell scripts include file manipulation, program execution, and printing text.
	3. The process of executing set of commands available in the file ushing shell.

What is SHELL :
	A shell is a program that act as an interface between USER and KERNEL.

What is KRNEL :
	Kernel is a Central Compute of an Operating System that manages operations of Computer Hardware.

Types of KERNELS :
	1. MONOLITHIC KERNEL :
		A monolithic kernel is an operating system architecture where the entire system runs in kernel mode. In this design, the kernel consists of a single, large 
		executable that includes various services such as memory management, device drivers, file system management, and process management, among others.

	2. HYBRID KERNEL :
		* Hybrid kernels combine aspects of both monolithic and microkernel architectures. 
		* They run some core services in kernel mode and others in user mode, offering a balance between performance and modularity. 
		* Hybrid kernels can adapt their design according to specific requirements, incorporating the best aspects of both architectures.
		* Hybrid kernels offer flexibility in design, allowing for adaptation based on specific requirements and use cases. 
		* They can achieve a balance between performance and modularity by combining the best aspects of monolithic and microkernel architectures. 
		* Developers can also customize which components run in kernel mode and user mode, providing more control over system design.
	3. EXO KERNEL :
		An Exokernel OS design pushes the boundaries of minimalism. Applications are given direct access to hardware resources, allowing them to manage resources 
		and make decisions that the kernel previously made.

# LINUX ARCHITECTURE #
======================
There are four Major componenets :
	1. ARCHITECTURE LAYER = application programs 
	2. SHELL
	3. KERNEL = Core Component of an Operating System
	4. HARDWARE LAYER = Peripheral (CPU, RAM, Storage)

* Kernel is responsible to communicate with hardware components.
* Shell is mediator between user and hardware.
*  Shell Scripting is used to automate our dialy tasks.
* File Extension --> '.sh'
* When we execute any command in Linux then shell will process our command execution.
* Shell will verify command syntax is valid or not.
* Shell will convert our command into kernel understandable format.

# COMMANDS #
=============
1. To print all shells of Linux ==> cat /etc/shells
2.  Print default shell of Linux ==> echo $SHELL
3. To execute shell scripting file ==> sh <filename>

' 1. Script to run Commands '
#! /bin/bash			# This line is called "SHABANG" This line is not mandatory.
whoami
pwd
date

' 2. Script to Print Messages'
#! /bin/bash
echo 'Hello World'
echo 'Welcome Sunil'

' 3. Script to Print Name and Message '
#! /bin/bash
echo 'ENTER YOUR NAME'
read sunil		# read command is used to read a string from Keyboard
echo "GOOD MORNING $ SUNIL"

' 4. Sum of Two Numbers '
#! /bin/bash
a = 10
b = 20
c = $(($a+$b))
echo " SUM is : $c "

' 5. IF - ELSE Statement example '
#! /bin/bash
echo "ENTER YOUR NAME"
read name
if [$name == 'Sunil']
then
	echo "Hi"
else
	echo "Bye"
fi		# fi indicates the END OF IF STATEMENT

# REAL TIME TASK
' 6. Script is used to print the reports of AWS resources and output moved to Text file'
@ To check the AWS resources we need AWS CLI @

'We need AWS resouces reports on Every day 6 PM'
#! /bin/bash
# List of S3 buckets

echo "print list of S3 buckets"
aws s3 ls
echo "print list of S3 buckets" > S3_Report
aws s3 ls

echo " print list of EC2 instances "
aws ec2 describe-instances
echo " print list of EC2 instances " > EC2_Report
aws ec2 describe-instances

echo " Print list of IAM Users"
aws iam list-users
echo " Print list of IAM Users" > IAM_Report
aws iam list-users

echo " Print Lambda functions "
aws lambda list-functions
echo " Print Lambda functions " > Lambda_Report
aws lambda list-functions

* A Shell provides you with an interface to the Unix system. It gathers input from you and executes programs based on that input. When a program finishes 
executing, it displays that program's output.
* Each Flovour has their set of commands.
* $, which is called the command prompt, is issued by the shell. While the prompt is displayed, you can type a command.
* Shell reads your input after you press Enter. It determines the command you want executed by looking at the first word of your input. A word is an unbroken set of 
characters. Spaces and tabs separate words.

# Shell Types #
===========
In Unix, there are two major types of shells :
	1. Bourne shell − If you are using a Bourne-type shell, the $ character is the default prompt.
		Bounce Shell Types :
			1. Bourne shell (sh)
			2. Korn shell (ksh)
			3. Bourne Again shell (bash)
			4. POSIX shell (sh)
	2. C shell − If you are using a C-type shell, the % character is the default prompt.
		C Shell Types :
			1. C shell (csh)
			2. TENEX/TOPS C shell (tcsh)

* # --> Used to Comment Lines

Example - To execute commands
#!/bin/bash
pwd		# Command for Present Working Directory
ls			# List of files and folders
' To make the file to executable '
$chmod +x test.sh
' To run thr file which is in current directory '
$./test.sh
output :
	/home/amrood
	index.htm  unix-basic_utilities.htm  unix-directories.htm  
	test.sh    unix-communication.htm    unix-environment.htm

Example - To print date
$date

Example - Read a Name from Keyboard
#!/bin/sh
echo "What is your name?"
read PERSON
echo "Hello, $PERSON"

# VARIABLE NAMES #
------------------------------
* The name of a variable can contain only letters (a to z or A to Z), numbers ( 0 to 9) or the underscore character ( _).
* By convention, Unix shell variables will have their names in UPPERCASE.
Example :
	_ALI
	TOKEN_A
	VAR_1
	VAR_2
	2_VAR
	-VARIABLE
	VAR1-VAR2
	VAR_A!

# DEFINING VARIABLES #
------------------------------------
" variable_name=variable_value "
Example :
	NAME="Zara Ali"	# Variables of this type are called scalar variables. A scalar variable can hold only one value at a time.
	VAR1="Zara Ali"
	VAR2=100

# ACCESSING VARIABLES #
*  To access the value stored in a variable, prefix its name with the dollar sign ($).
Example :
	#!/bin/sh
	NAME="Zara Ali"
	echo $NAME

# READ - ONLY VARIABLES #
-----------------------------------------
* Shell provides a way to mark variables as read-only by using the read-only command. After a variable is marked read-only, its value cannot be changed.
Example :
	#!/bin/sh
	NAME="Zara Ali"
	readonly NAME
	NAME="Qadiri"

output : /bin/sh: NAME: This variable is read only.

# UNSETTING VARIABLES #
--------------------------------------
* Unsetting or deleting a variable directs the shell to remove the variable from the list of variables that it tracks. Once you unset a variable, you cannot access the 
stored value in the variable.

Syntax : unset variable_name

Example
#!/bin/sh
NAME="Zara Ali"
unset NAME
echo $NAME

# VARIABLE TYPES #
------------------------------
There are 3 types :
	1. Local Variables : 
		A local variable is a variable that is present within the current instance of the shell. It is not available to programs that are started by the shell. They are set at 
		the command prompt.
	2. Environment Variables :
		An environment variable is available to any child process of the shell. Some programs need environment variables in order to function correctly. Usually, a shell 
		script defines only those environment variables that are needed by the programs that it runs.
	3. Shell Variables :
		A shell variable is a special variable that is set by the shell and is required by the shell in order to function correctly. Some of these variables are environment 
		variables whereas others are local variables.

# SPECIAL UNIX VARIABLES #
------------------------------------------
1. $0 : The filename of the current script.
2. $n : These variables correspond to the arguments with which a script was invoked. Here n is a positive decimal number corresponding to the position of an				
			argument (the first argument is $1, the second argument is $2, and so on).
3. $# : The number of arguments supplied to a script.
4. $* : All the arguments are double quoted. If a script receives two arguments, $* is equivalent to $1 $2.
5. $@ : All the arguments are individually double quoted. If a script receives two arguments, $@ is equivalent to $1 $2.
6. $? : The exit status of the last command executed.
7. $$ : The process number of the current shell. For shell scripts, this is the process ID under which they are executing.
8. $! : The process number of the last background command.

#  COMMAND LINE ARGUMENTS #
------------------------------------------------

# AWS - DEVOPS DEMO #
=====================
" INTRODUCTION TO DEVOPS "
--------------------------------------------
