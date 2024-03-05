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