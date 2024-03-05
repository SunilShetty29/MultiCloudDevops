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