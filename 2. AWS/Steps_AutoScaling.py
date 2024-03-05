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