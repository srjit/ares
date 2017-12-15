
#### Installing and configuring Git on Windows

 - Download the latest Git for Windows installer.
 - open command prompt and type in
   	```
		git config --global user.name "User Name"
		git config --global user.email "email@mailserver.edu"
	```
 - Generating SSH Keys

    1. Open 'Git Bash'
    2. Enter the command ``` ssh-keygen -t rsa -b 4096 -C "your_email@example.com"  ```
    3. When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.
    4. Hit enter two more times when the passphrase is asked.
    5. The default location of keys is
        + HOME_FOLDER\\.ssh
    6. Add the pulic key generated to [https://github.com/settings/keys](https://github.com/settings/keys)

 - Cloning a repo
    1. Documentation for cloning a repo is mentioned [here](https://help.github.com/articles/cloning-a-repository/)
    2. When new changes are made in the git repo by another user, execte ``` git pull ``` in
       the git bash shell to collect the changes
    