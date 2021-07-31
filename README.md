# Project-Automation


This project aims to automate the creation of a new project. Based on information entered by the user in a file,
a template is created for a project (creating the directory, synchronizing with github, creating a new repository).
Download and Test:
```
https://github.com/dinuionica/Project_automation.git
```
For testing, you can try these commands:

```
$ sudo apt install python3
$ sudo apt install pip
$ pip install -r requirements.txt
```
Usage:
```
Enter the username and the password of github in informations.txt file
Then type:
chmod u+x create.sh
alias create="/path/create.sh"
create "The name of the project"
```
