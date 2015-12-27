Linux Server Configuration
==========================

About
-----

From Udacity:

> You will take a baseline installation of a Linux distribution on a virtual machine and prepare it to host your web applications, to include installing updates, securing it from a number of attack vectors and installing/configuring web and database servers.

Supporting Courses:

*  [Configuring Linux Web Servers](https://www.udacity.com/course/configuring-linux-web-servers--ud299)
*  [Linux Command Line Basics](https://www.udacity.com/course/linux-command-line-basics--ud595)

Server Details
--------------

Server Configuration
--------------------

Append the hostname to the localhost line in `/etc/hosts`.

```bash
root@ip-10-20-26-132:~# hostname
ip-10-20-26-132
root@ip-10-20-26-132:~# vi /etc/hosts
```

```bash
# /etc/hosts
127.0.0.1 localhost ip-10-20-26-132
```

Add a user `grader` and give user sudo access. `grader` can run any command from any terminal as any user without providing a password. It is a best practice to use `visudo` to edit the sudoers file, but we are leveraging Ubuntu's include directive and we have root access without sudo.

```bash
root@ip-10-20-26-132:~# adduser grader
root@ip-10-20-26-132:~# echo "grader ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/grader
root@ip-10-20-26-132:~# chmod 0440 /etc/sudoers.d/grader
root@ip-10-20-26-132:~# su -l grader
grader@ip-10-20-26-132:~$ ls -a /root
ls: cannot open directory /root: Permission denied
grader@ip-10-20-26-132:~$ sudo !!
sudo ls -a /root
.  ..  .bash_history  .bashrc  .cache  .profile  .ssh  .viminfo
```

Use `ssh-keygen` on host computer to generate private and public keys. Copy public key to the remote (AWS) server and include in `~/.ssh/authorized_keys` with the correct permissions, owner, and group.

```bash
brenj@ubuntu:~$ scp -i ~/.ssh/udacity_key.rsa /home/brenj/.ssh/id_rsa.pub root@52.27.202.14:/home/grader/
brenj@ubuntu:~$ ssh -i ~/.ssh/udacity_key.rsa root@52.27.202.14
root@ip-10-20-26-132:~# cd /home/grader/
root@ip-10-20-26-132:/home/grader# ls -a
.  ..  .bash_history  .bash_logout  .bashrc  id_rsa.pub  .profile  .viminfo
root@ip-10-20-26-132:/home/grader# chown grader:grader id_rsa.pub
root@ip-10-20-26-132:/home/grader# ls -l id_rsa.pub 
-rw-r--r-- 1 grader grader 388 Dec 26 19:56 id_rsa.pub
root@ip-10-20-26-132:/home/grader# mkdir .ssh
root@ip-10-20-26-132:/home/grader# chown grader:grader .ssh
root@ip-10-20-26-132:/home/grader# mv id_rsa.pub .ssh/authorized_keys
root@ip-10-20-26-132:/home/grader# chmod 700 .ssh/
root@ip-10-20-26-132:/home/grader# chmod 644 .ssh/authorized_keys
root@ip-10-20-26-132:/home/grader# exit
logout
Connection to 52.27.202.14 closed.
brenj@ubuntu:~$ ssh -i ~/.ssh/id_rsa grader@52.27.202.14
grader@ip-10-20-26-132:~$ whoami
grader
```

Update the SSH daemon configuration to improve security. Change the default to SSH port, set `PasswordAuthentication` and `PermitRootLogin` to `no`, and use `AllowUsers` to create a white-list of who (only `grader`) can log into the server via SSH. Then restart the SSH service to use new config settings.

```bash
grader@ip-10-20-26-132:~$ sudo vi /etc/ssh/sshd_config
```

```bash
# /etc/ssh/sshd_config updates
Port 2200
PasswordAuthentication no
PermitRootLogin no
AllowUsers grader
```

```bash
grader@ip-10-20-26-132:~$ sudo service ssh restart
ssh stop/waiting
ssh start/running, process 7251
grader@ip-10-20-26-132:~$ exit
logout
Connection to 52.27.202.14 closed.
brenj@ubuntu:~$ ssh -p 2200 -i ~/.ssh/udacity_key.rsa root@52.27.202.14
Permission denied (publickey).
brenj@ubuntu:~$ ssh -p 2200 -i ~/.ssh/udacity_key.rsa grader@52.27.202.14
grader@ip-10-20-26-132:~$ whoami
grader
```

Using `ufw`, the front-end to iptables on Ubuntu, configure the firewall to continue allowing remote administration as well as host a web server. All other incoming requests should be denied while still allowing all outgoing connections.

```bash
grader@ip-10-20-26-132:~$ sudo ufw status                                                                                   
Status: inactive
grader@ip-10-20-26-132:~$ sudo ufw default deny incoming
Default incoming policy changed to 'deny'
(be sure to update your rules accordingly)
grader@ip-10-20-26-132:~$ sudo ufw default allow outgoing
Default outgoing policy changed to 'allow'
(be sure to update your rules accordingly)
grader@ip-10-20-26-132:~$ sudo ufw allow 2200/tcp
Rules updated
Rules updated (v6)
grader@ip-10-20-26-132:~$ sudo ufw allow www
Rules updated
Rules updated (v6)
grader@ip-10-20-26-132:~$ sudo ufw show added
Added user rules (see 'ufw status' for running firewall):
ufw allow 2200/tcp
ufw allow 80/tcp
grader@ip-10-20-26-132:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
grader@ip-10-20-26-132:~$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
2200/tcp                   ALLOW       Anywhere
80/tcp                     ALLOW       Anywhere
2200/tcp (v6)              ALLOW       Anywhere (v6)
80/tcp (v6)                ALLOW       Anywhere (v6)

grader@ip-10-20-26-132:~$ exit
logout
Connection to 52.27.202.14 closed.
brenj@ubuntu:~$ ssh -p 2200 -i ~/.ssh/udacity_key.rsa grader@52.27.202.14
grader@ip-10-20-26-132:~$ whoami
grader
```


Resources
---------

* [Sudoers File](https://www.garron.me/en/linux/visudo-command-sudoers-file-sudo-default-editor.html)
