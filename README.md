# INET 4031 Add User Script (Python)
  
**Python Script for Adding Users/Groups to a System**
  
## Description
  
This Python Script reads user/group data from an input file, processes the file line-by-line and adds each user to the system.

*. The program starts by looping through every line of the input file. The program utilizes regular expressions .match() in order to check if there is a commented-out line as well as split the input file line by the ":" .  After the line has been split and assigned to its corresponding value such as "password". Utilizing the os. system the user is created by executing the formatted line to the command line.*
  
## Operation
  
### Input File Specification
  
The input file should have the following format:

*** username:default_password:last_name:first_name:comma_separated_list_of_groups

For example:

user04:pass04:Last04:First04:group01,group03

The name of the input file is up to the user.  Convention is create-users.input

### Running the Script
* The program is formatted to be executed to be run as python 2. The file permissions should be changed to an executable using the command "chmod a+x create-users.py". running this file requires sudo access because you are dealing with users and groups. *
