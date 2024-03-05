@ Don't delete default VPC @
@ customization is possible for both IPV4 and IPV6 CIDR block @
@ When we select Custom VPC >> auto assign Public IP will be automatically disabled >> enable the option manually @

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