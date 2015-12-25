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

Append the hostname to the local host line in `/etc/hosts`.

```bash
root@ip-10-20-26-132:~# hostname
ip-10-20-26-132
root@ip-10-20-26-132:~# vi /etc/hosts
```

```bash
# /etc/hosts
127.0.0.1 localhost ip-10-20-26-132
```

Add a user `grader` and give user sudo access. `grader` can run any command from any terminal as any user without providing a password.

```bash
root@ip-10-20-26-132:~# adduser grader
root@ip-10-20-26-132:~# echo "grader ALL=(ALL) NOPASSWD:ALL" >/etc/sudoers.d/grader
root@ip-10-20-26-132:~# su -l grader
grader@ip-10-20-26-132:~$ ls -a /root
ls: cannot open directory /root: Permission denied
grader@ip-10-20-26-132:~$ sudo !!
sudo ls -a /root
.  ..  .bash_history  .bashrc  .cache  .profile  .ssh  .viminfo
```

Resources
---------

* [Sudoers File](https://www.garron.me/en/linux/visudo-command-sudoers-file-sudo-default-editor.html)
