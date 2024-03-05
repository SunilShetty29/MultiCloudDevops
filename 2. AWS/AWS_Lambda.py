AWS LAMBDA FUNCTION :
	* it is a compute service that lets you run code without provisioning and managing servers.
	* Lambda runs your code on a high availability compute infra structure and performs all of the administration of the compute resources, including server and OS maintainance, capacity provisioning and automatic scaling and logging with lambda. All you need to do is supply your code in one of the language run time that lambda.
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
	6. Permissions --> change default execution role --> navigate to execution role --> We have 3 options (' create new role with basic lambda expression', 'use an existing role', 'create new role from AWS policy template'). Select ' create new role with basic lambda expression'.
		1. dont change any settings.
		2. Navigate to Advance settings 
		3. dont change anything. and click on Next.
	7. Create function and Navigate to code.
	8. Remove the default code and paste the python code.
	9. click on deploy.
	10. goto configuration >> permissions >> select IAM role created.
	@ if IAM role is not available. Create an IAM role @
	11. Open IAM role >> required full permissions >> Add permissions >> attach policy >> select EC2 full permissions and adminstrator access >> click on add policy.
	12. Now schedule lambda --> for that we need ClodWatch --> Events >> event rules >> event buses >> create rule >> enter name and description  >> select default event bus >> rule type >> rule with event pattern schedule >> select schedule >> continue to create rule >> schedule pattern >> A free grained schedule that runs >> cron pattern >> Enter the timings depends upon ur current time (Mins=15, hours=6, day of month=?, month=*, day of week=tue, year=*) >> change local time zone >> adjust time as per requirement >> Next >> Select target >> lambda function >> select function name (while scheduling region may change sometimes so we need to change the region manually) >> next >> next >> Change local time >> Create rule >> Navigate to EC2 and Observe the created instances state.
	@ We have Cron Pattern examples from 'https://crontab.guru.com' website @ 
	13. Create the same lambda function for start service @ replace 'ec2.stop_instances(InstanceIds=instances)' this line with 'ec2.start_instances(InstanceIds=instances)' @
	14. Open functions >> Actions >> delete the functions.
	15. delete the created servers.
	16. IAM roles and CloudWatch schedules are NOT MANDATORY to delete.