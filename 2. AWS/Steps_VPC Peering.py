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
