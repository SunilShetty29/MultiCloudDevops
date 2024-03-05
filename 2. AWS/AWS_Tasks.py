Task_EFS:->
    1. Create two instances in 2 different regions.
    2. Create a Security Group by opening NFS port.
    3. Create a EFS storage by using Security Group.
    4. Mount EFS on 2 instances.
    5. Test EFS on instances.
    6. Check the File Transfer.

Task_S3:-> Static Webhosting.

TASK 1_EBS Volumes :->
    1. Create an instance with default volume.
    2. Create Multiple Files and Folders.
    3. Delete the Server and take the Snapshot of the Volume.
    4. Take the Snapshot for Available Volume.
    5. Delete the Volume.
    6. Create a Test Instance with Default Volume.
    7. Check the Files and Folders Available or Not ??
    8. Stop the Server and detach the New Volume and Attach the Old Volume.
    9. Connect the Server and Check the Files and Folders.

Task_AMI (Lauch 5 instances with the help of AMI):->
    1. Launch an Instance.
    2. Install 5 App's (JAVA, MAVEN,JENNKINS, APACHE TOMCAT, GIT).
    3. Create an AMI for the Instance.
    4. Launch 5 instances with the help of created AMI.

Task_VPC :->
	1. Create a VPC (Custom).
	2. Create an Instance with Public Subnet.
	3. Create an Instance with Private Subnet.
	4. Try to Access the both Instances via Putty/MobaXterm/Gitbash.
		Note : Instance with Private Subnet should through Network Error.


Task_VPC Peering Connection :->
	Sub Task 1 :-> Create a Peering Connection between default VPC and Custom VPC with in the Same AWS account.
	Sub Task 2 :-> Create a Peering Connection between Custom VPC from your A/C to Cutom VPC in another A/C.
	Sub Task 3 :-> Create a Peering Connection between default VPC from your A/C to default VPC in another A/C.
	Sub Task 4 :-> Create a Peering Connection between Custom VPC from your A/C to default VPC in another A/C.

Task_Auto Scaling :->
1. Create an Auto Scaling Group with desired capacity = 2 and Minimum desired capacity = 2 and Maxium desired capacity = 5.
2.  To Test Auto Scaling --> delete 1 Server and Check.
3. Terminate the both Instances and Check.

Task_AWS RDS :
	Create an AWS RDS 

Task_AWS CLI :
	Configure the AWS CLI and practice the commands with help of attached url.

Task_AWS ELB:
	1. CREATE 2 SECURITY GROUPS --> 1 SG with ALL TCP and 2 SG with HTTP ports.
	2. CREATE 2 INSTANCES WITH USER DATA.
	3. CREATE A TARGET GROUP WITH CREATED 2 INSTANCES.
	4. CREATE AN ELB and ASSOCIATE WITH TARGET GROUPS.
	5. TEST THE ELB BETWEEN BOTH THE SERVERS.

Task_Elastic BeanStalk:
	1. Deploy 1 PHP  app with the help of Elastic BeanStalk

Task_AWS Lambda function :
	1. Create a lambda function for start and stop EC2 instances.

@ 27-2-2024 Class Video @
https://transcripts.gotomeeting.com/#/s/9cfcc2484347d3ed265ca26f4882a1a4fc7ff5b71fabf7310519c3d63b556c99

@ 29-2-2024 Class Video @
https://transcripts.gotomeeting.com/#/s/d5572b70f047623d7659ec796a1443febb8647e322acfd354cbbac61c549c012



