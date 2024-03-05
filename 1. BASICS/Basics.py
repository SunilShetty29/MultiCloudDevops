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