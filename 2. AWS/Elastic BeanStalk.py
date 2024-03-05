 ELASTIC BEAN STACK :
	* It is an AWS-managed service for Web Applications.
	* It is a pre-configured server that can directly take up your application code and environment configurations and use it automatically provision and deploy the required resources with in AWS to run the Web applications.
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
	* When you deploy your app, Elastic BeanStalk builds the selected supported platform version and provisions one or more AWS resources such as Amazon EC2 instances to run your app.
	* Once we created this service backend 1 instance will be created (t2.micro and t3.small).

ON-INSTANCE CONFIGURATION :
	* There are 5 Stages in config :
		1. Code
			Focus on building your application. 
		2. HTTP Server
		3. App Server, Language Interpretor
		4. OS
		5. Host
	* Configures each EC2 instance in your env with components necessary to run apps for the selected platform. No more worrying about about logging into instances to install and configure your application stack.
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
			2. Pltform --> there is a list of available langugaes supported for Elastic BeanStalk >> We need to select the language depends upon the app language >> Here we are selecting 'PHP' because coding is not there in PHP and we can deploy live apps quickly and easily.
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