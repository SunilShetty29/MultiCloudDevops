# INTRODUCTION TO GIT & GITHUB #
----------------------------------------------------
" What is Git " :
	* It is a Repository or Version Control tool.
	* Repository --> Where we can store our data.
	* Version Control --> Will track individaual data by using different version.
	* Git is used for source code management. It is free and open-source version control system used to handle small to very large projects efficiently.
	* Git is used for tracking changes in the source code, enabling multiple developers to work together.

" What is a Repository " :
	* 'Repo' = Repository
	* Usually used to organize a single project.
	* repos can contain folders and files, images, videos, spreadsheets and data sets - anything your project needs.

" What is a Version Control System " :
	* A way to manage files and directories.
	* Track changes over time.
	* Recall previous versions.
	* 'source control' is a subset of a VCS.

" GIT " :
	* Created by Linus Torvalds, April 2005.
	* Replacement for BitKeeper to manage Linux Kernel changes.
	* A command line version control program.
	* uses checksums to ensure data integrity.
	* distributed version control (like BitKeeper).
	* Cross-platform support including windows.
	* Open source, free.

" Distributed Version Control " :
	* No Centeal Server.
	* Every developer is a client, the server and the repository.

" Git Support multiple languages " :
	1. HTML
	2. CSS
	3. JavaScript
	4. Python
	5. ASP
	6. Scala
	7. Shell Scripts
	8. PHP
	9. Ruby
	10. Ruby on rails
	11. Perl
	12. JAVA
	13. C
	14. C++
	15. C#
	16. OBJECTIVE C
	17. HASKELL
	18. COFFEESCRIPT
	19. ACTION SCRIPT

" GIT WORK FLOW " :
	@ Open git bash from created folder in local repo.
	1. git init --> to initialize local repo
	@ Once git initialized '.git' file will be generated automatically.
	@ developer need to create one user @ (LDAP)
	@ We need to craete the user for the first time alone @
	@ user is used for tracking the code and file status @
	2. git config --global user.name "Sunil" --> To create user.
	3. git config --global user.email "k.sunikumar0491@gmail.com" --> To create 
	User email.
	4. git config --list --> To check the users list
	@ For workspace = 1 user only @
	@ If u add one more user it will overwrite with the previous user @
	@ after creating the user developer will start developing the code @
	5. Creat a file with VI editor @
	6. git status --> To check the commits list
	@ once development completed file will move to the "Staging Area or 
	Indexing Area" @
	7. git add <filename> --> To move the file to staging area
	8. git rm --cache <filename> --> To revert back file to Local repo
	9. git add . --> To move all the files to staging area which are present in local 
	repo
	10. git commit -m "Commit Message" --> To move file to commit area
	11. git log --> To check the status
	12. Create GitHub account
	13. Create one Repository
	14. git remote add origin <created repo url> (" 
	https://github.com/SunilShetty29/MultiCloudDevops.git ")
	@ used to establish the connection between Local repo to Remote Repo @
	15. git remote --> To check the origin path is set or not
	16. git push -u origin master

