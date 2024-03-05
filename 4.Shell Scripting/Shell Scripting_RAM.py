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
		A monolithic kernel is an operating system architecture where the entire system runs in kernel mode. In this design, the kernel consists of a single, large executable that includes various services such as memory management, device drivers, file system management, and process management, among others.

	2. HYBRID KERNEL :
		* Hybrid kernels combine aspects of both monolithic and microkernel architectures. 
		* They run some core services in kernel mode and others in user mode, offering a balance between performance and modularity. 
		* Hybrid kernels can adapt their design according to specific requirements, incorporating the best aspects of both architectures.
		* Hybrid kernels offer flexibility in design, allowing for adaptation based on specific requirements and use cases. 
		* They can achieve a balance between performance and modularity by combining the best aspects of monolithic and microkernel architectures. 
		* Developers can also customize which components run in kernel mode and user mode, providing more control over system design.
	3. EXO KERNEL :
		An Exokernel OS design pushes the boundaries of minimalism. Applications are given direct access to hardware resources, allowing them to manage resources and make decisions that the kernel previously made.

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
read sunil		# read command is used to read a string from Command Line
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

What is Shell Scripting ?
============================
=&gt; Shell will act as mediator between Users and Kernel. Shell will convert
commands into kernal understandable format.
=&gt; Scripting means executing set of commands using a file.
##### The process of executing set of commands available in the file using
SHELL is called as Shell Scripting #####
=&gt; Shell Scripting is used to automate our daily routine works.
=&gt; Shell Script file will have .sh extension
=&gt; Below is the command to execute shell script file
$ sh &lt;filename&gt;
====================
Script-1 : work.sh
====================
#! /bin/bash
whoami
pwd
date
#### Run : sh work.sh ####
=====================
Script-2 : msg.sh
=====================
#! /bin/bash
echo &#39;Hello World&#39;
echo &#39;Welcome to DevOps World&#39;
echo &#39;DevOps is very intresting&#39;
========================
Script-3 : NameDemo.sh
========================
#! /bin/bash
echo &#39;Enter Your Name&#39;
read a
echo &quot;Good Evening $a&quot;
===================
Script-4 : Sum.sh
===================
#! /bin/bash
a=10
b=20

c=$(($a+$b))
echo &quot;Sum is : $c&quot;
============================
Script-5 : DynamicValSum.sh
============================
#! /bin/bash
echo &quot;Enter First Number&quot;
read a
echo &quot;Enter Second Number&quot;
read b
c=$(($a+$b))
echo &quot;Result : $c&quot;
============
Variables
============
=&gt; Variables are used to store the data
=&gt; Variables are key-value pairs
id = 101
name = ram
gender = male
=&gt; Variables are divided into 2 types
1) Environment Variables ( System Variables - Already Defined )
2) User Defined Variables (We will create these variables)
Note: To access value of variable we will use &#39;$&#39; symbol.
Ex: $SHELL $USER
=======================
Command Line Arguments
=======================
=&gt; The arguments which we we will pass to script file at the time of
execution.
Ex: sh demo.sh ramit 30
=&gt; We can access command-line args in script file like below
$# - No.of args
$0 - script file name
$1 - First Cmd arg

$2 - Second Cmd arg
$3 - Third Cmd Args
$* - All cmd args
============================
Script-6 : DynamicValSum.sh
============================
#! /bin/bash
result=$(($1+$2))
echo &quot;Sum is : $(($1+$2))&quot;
Run : sh DynamicValSum.sh 10 20
==================================================================
=&gt; We have 2 options to pass dynamic values to shell script file
1) Using &#39;read&#39; command
2) Using cmd args
==================================================================
1) Conditional Statements ( if - elif - else )
2) Loops ( for &amp; while )
3) Functions
===========================
Conditional Statements
==========================
=&gt; Conditional Statements are used to execute &#39;commands&#39; one time based on
condition
Ex : if - else / if - elif - else
Syntax:
if [ condition ]
then
statements
else
statements
=======================
Script-7 : if-else.sh
=======================
#! /bin/bash
echo &quot;Enter Name&quot;
read name

if [ $name == &#39;john&#39; ]
then
echo &quot;Hi&quot;
else
echo &quot;Bye&quot;
fi
===============================
Script - 8 : if-elif-else.sh
===============================
#! /bin/bash
echo &quot;Enter Name&quot;
read name
if [ $name == &#39;john&#39; ]
then
echo &quot;Hi $name&quot;
elif [ $name == &#39;smith&#39; ]
then
echo &quot;Hello $name&quot;
else
echo &quot;Bye $name&quot;
fi
=====================================
Script - 9 : if-elif-else.sh
=====================================
#! /bin/bash
echo &quot;Enter first number&quot;
read a
echo &quot;Enter second number&quot;
read b
if [ $a -gt $b ]
then
echo &quot;$a is greater than $b&quot;
elif [ $b -gt $a ]
then
echo &quot;$b is greater than $a&quot;
else
echo &quot;Both are equal&quot;
fi
====================
Loops
====================
=&gt; To print &quot;hi&quot; 5 times we will write script like below

echo &quot;hi&quot;
echo &quot;hi&quot;
echo &quot;hi&quot;
echo &quot;hi&quot;
echo &quot;hi&quot;
=&gt; If we want to print &quot;hi&quot; for 1000 times, can we write echo for 1000
times ? Not recommended
=&gt; To execute same command multiple times then we will use &quot;Loops&quot;
=&gt; We have 2 types of loops
1) Range Based Loop ( Ex: for loop )
2) Conditional Based Loop ( Ex: while loop )
=&gt; Print &quot;hi&quot; message 10 times (Here we know the range to print msg - we
can use &#39;for&#39; loop)
=&gt; Print &quot;good night&quot; message till 10 PM (Here we don&#39;t range but we know
condition - we can use while loop)
=========================
Script-10 : for-loop1.sh
=========================
#! /bin/bash
for (( i=1 ; i&lt;=10; i++ ))
do
echo &quot;hi&quot;
done
=========================
Script-11 : for-loop2.sh
=========================
#! /bin/bash
for (( i=1; i&lt;=10; i++ ))
do
echo &quot;$i&quot;
done
============================
Script-12 : while-loop.sh
============================
#! /bin/bash
i=10
while [ $i -ge 1 ]
do
echo &quot;$i&quot;
let i--;
done

=====================
Functions / Methods
====================
=&gt; Functions are used to perform some action / task
=&gt; The big task can be divided into smaller tasks using functions
=&gt; Using functions we can divide our tasks logically
=&gt; Functions are re-usable
Syntax:
-------
# writing function
function functionName ( ) {
// function body
}
# calling function
functionName
=======================
Script - 13 : fun1.sh
=======================
#! /bin/bash
function welcome ( ) {
echo &quot;this is line 1&quot;
echo &quot;this is line 2&quot;
echo &quot;this is line 2&quot;
}
# calling function
welcome
=============================================================
Script - 14 : Read File name then print content of that file
=============================================================
#! /bin/bash
function readFileData ( ) {
echo &quot;Enter file name to read&quot;
read filename
cat $filename
}
# calling function
readFileData
========================================================================
Script - 15 : Read File name as cmd arg then print content of that file
========================================================================
#! /bin/bash

filename=$1
function readFileData ( ) {
cat $filename
}
# calling function
readFileData
================================
Script-16: Check file presence
================================
#! /bin/bash
echo &quot;enter filename&quot;
read filename
if [ -f &quot;$filename&quot; ] ; then
echo &quot;File already exist&quot;
else
echo &quot;File not exist, hence creating...&quot;
touch $filename
echo &quot;file created....&quot;
fi
====================================
Script-17: Check directory presence
====================================
#! /bin/bash
echo &quot;Enter directory name&quot;
read dirname
if [ -d &quot;$dirname&quot; ] ; then
echo &quot;Directory exist&quot;
else
echo &quot;directory not available, hence creating..&quot;
mkdir $dirname
echo &quot;directory created&quot;
fi
======================================
Shell Script Programs For Assignment
======================================
1) Write shell script to check given number is even number or odd number
(take number from user)
2) Write shell script to check given number is prime number or not
(take number from user)
3) Write shell script to check given year is leap year or not
(take year from user)
4) Write shell script to check given string is palindrome or not
(take string from user)
5) Write shell script to print table of given number (take number from
user)

2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
..
2 * 10 = 20
====================
What is CRON ?
====================
=&gt; Cron is a utility in Linux which is used to schedule jobs execution
=&gt; In Realtime we will have several jobs for execution on daily / weekly /
monthly / yearly basis
1) Take Backup of files
2) Delete temp files
3) System Maintanence
========
Usecase
========
=&gt; Execute shell script file for every 5 minutes.
Note: Instead of human executing script file for every 5 mintues we can
schedule script file execution using CRON.
=================
What is CROND ?
================
=&gt; In Linux machine CROND is a daemon process ( background ) which will
check scheduled CRON JOBS for every minute.
=&gt; If any job is scheduled then CROND will execute that job based on given
schedule.
=================
CRON JOB Syntax
=================
* * * * * &lt; command / script-file &gt;
Note: Read CRON expression from left side
=&gt; first * will represent minutes ( 0 - 59 )
=&gt; second * will represent hour ( 0 - 23 )
=&gt; third * will represent day of month ( 1 - 31 )
=&gt; fourth * will represent month of year ( 1 - 12 )
=&gt; fifth * will represent day of week ( 0 - 6, mon - sun )
=========================
Sample Cron Expressions

=========================
Run for every 15 mins : */15 * * * * task.sh
Run every day @5 am : 0 5 * * * task.sh
Run every day @5 pm : 0 17 * * * task.sh
Run every month first day @9 am : 0 9 1 * * task.sh
=====================
What is crontab file
=====================
=&gt; In linux for every user account one crontab file will be available
=&gt; crontab file is used to configure cronjobs for execution
# Open crontab file
$ crontab -e
# Display cronjobs schedules
$ crontab -l
# Remove crontab file
$ crontab -r
==================
Check Cron Status
==================
$ sudo systemctl status cron
==================
CRON JOB Practice
==================
1) Launch Linux Machine with Ubuntu AMI
2) Connect with Ubuntu VM using MobaXterm
3) Create shell script file (task.sh) like below
$ vi task.sh
Note: keep below content in shell script file
touch /home/ubuntu/f1.txt
touch /home/ubuntu/f2.txt
4) Provide execute permission for script file
$ chmod +x task.sh
5) Open crontab file and configure job schedule
$ crontab -e
Note: Enter below cron job in crontab file

*/1 * * * * /bin/bash /home/ubuntu/task1.sh
6) Save and close crontab file ( ctrl + x )
7) Check files creation in pwd
$ ls -l
Note: We can observer f1.txt and f2.txt files got created.
========================
What is inode number ?
========================
=&gt; Inode is one unique number that will be assigned for every file in linux
=&gt; Linux will use inode number to map our files with its name in the linux
db
==========================
Hard Links and Soft Links
===========================
=&gt; In linux we can create link files ( similar to shorcut files in windows
)
=&gt; We have 2 types of link files in linux
1) Hard Link
2) Soft Link
--------------------------------
Syntax To create Hard Link:
--------------------------------
$ ln &lt;orginal-file&gt; &lt;link-file&gt;
Ex:
$ touch m1.txt
$ ln m1.txt m11.txt
Note: m11.txt is hard link file for m1.txt
$ ls -li
Note: m1.txt and m11.txt files are having same inode number
Note: If we write some data to m1.txt that data will reflect in m11.txt
file also
Note: If we delete m1.txt file still there is no effect on m11.txt
------------------------------
Syntax To create Soft Link :
------------------------------
$ ln -s &lt;orginal-file&gt; &lt;soft-link-file&gt;
Note: Soft Link is like shortcut in windows

Ex:
$ touch s1.txt
$ ln -s s1.txt s11.txt
$ ls -li
Note: Original file and soft link file having different inode numbers
$ cat &gt;&gt; s1.txt
Note: Data writing in original file will reflect in soft link file also
$ rm s1.txt
Note: When we remove original file then soft link file will become dangling
file. We can&#39;t access that.
=======================
Process management
=======================
=&gt; Process represents a running program/application in OS
=&gt; We can see the running process using &#39;Task Manager&#39; in Windows

(CTRL + SHIFT + ESC)

=&gt; We can see the running process in linux using below command

$ ps

Note: For every process one unique PID will be available (Process ID)
ps : display all runnig processes
top : Display dynamic view of system processes
=&gt; For every process there will be a state (Process state)
Running ( R ) : Currently executing
Sleeping ( S ) : Waiting for event / source
Stopped ( T ) : Stopped execution
Zombie ( Z ) : Finished execution but it waiting for exit status.
Note: we can use kill command to kill a process
$ kill -9 &lt;pid&gt;