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

> Amazon Linux instances are set to the UTC (Coordinated Universal Time) time zone by default ...

Server time is already set to UTC by default. Install NTP and verify that the default NTP configuration is working correctly. Note that to query NTP there is no need to add any firewall rules; requests to UDP port 123 are already allowed.

```bash
grader@ip-10-20-26-132:~$ date
Sun Dec 27 22:41:13 UTC 2015
grader@ip-10-20-26-132:~$ sudo apt-get install ntp
grader@ip-10-20-26-132:~$ ls /etc/init.d/ntp 
/etc/init.d/ntp
grader@ip-10-20-26-132:~$ sudo service ntp start
 * Starting NTP server ntpd
   ...done.
grader@ip-10-20-26-132:~$ ps -ef |grep ntpd
ntp       9140     1  0 22:36 ?        00:00:00 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -u 106:111
grader@ip-10-20-26-132:~$ ntpdc -c peers                                                                                       
     remote           local      st poll reach  delay   offset    disp
=======================================================================
=juniperberry.ca 10.20.26.132     2   64  377 0.13980 -0.022473 0.07472
=jtsage.com      10.20.26.132     2   64  377 0.05084 -0.015281 0.03854
=utcnist2.colora 10.20.26.132     1   64  377 0.03374 -0.015065 0.04233
*time-a.timefreq 10.20.26.132     1   64  377 0.03178 -0.024041 0.05214
=time-c.nist.gov 10.20.26.132     1   64  227 0.14331  0.015765 0.04695
grader@ip-10-20-26-132:~$ ntpdc -c sysinfo
system peer:          time-a.timefreq.bldrdoc.gov
system peer mode:     client
leap indicator:       00
stratum:              2
precision:            -23
root distance:        0.03178 s
root dispersion:      0.04543 s
reference ID:         [132.163.4.101]
reference time:       da2aeabf.a089e515  Sun, Dec 27 2015 22:54:55.627
system flags:         auth monitor ntp kernel stats 
jitter:               0.005783 s
stability:            0.000 ppm
broadcastdelay:       0.000000 s
authdelay:            0.000000 s
```

Update all of the installed packages and set up a Cron job to periodically update software (every Sunday).

```bash
grader@ip-10-20-26-132:~$ sudo apt-get update
grader@ip-10-20-26-132:~$ sudo apt-get upgrade
grader@ip-10-20-26-132:~$ sudo crontab -e
```

```bash
# root crontab
0 0 * * 0 apt-get update && { date; apt-get -qy upgrade; } >>/var/log/apt/auto-updates.log
```

Install `fail2ban` to monitor unsuccessful login attempts and ban IP addresses with too many failures.

```bash
grader@ip-10-20-26-132:~$ sudo apt-get install fail2ban
grader@ip-10-20-26-132:~$ sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
grader@ip-10-20-26-132:~$ sudo vi /etc/fail2ban/jail.local
```

```bash
# /etc/fail2ban/jail.local updates
[ssh]

enabled  = true
port     = 2200
filter   = sshd
logpath  = /var/log/auth.log
maxretry = 6
```

```bash
grader@ip-10-20-26-132:~$ sudo service fail2ban restart
 * Restarting authentication failure monitor fail2ban
   ...done.
grader@ip-10-20-26-132:~$ sudo iptables -S |grep fail2ban
-N fail2ban-ssh
-A INPUT -p tcp -m multiport --dports 2200 -j fail2ban-ssh
-A fail2ban-ssh -j RETURN
```

Application Configuration
-------------------------

Install and configure `postgres` database. By creating a `postgres` user and database with the name `grader`, we provide authentication for any connections from the same machine (which is all we need for this application).

```bash
grader@ip-10-20-26-132:~$ sudo apt-get install postgresql
grader@ip-10-20-26-132:~$ sudo -u postgres createuser --createdb grader
grader@ip-10-20-26-132:~$ sudo -u postgres createdb grader
grader@ip-10-20-26-132:~$ psql
psql (9.3.10)
Type "help" for help.

grader=> \d
No relations found.
grader=> \q
```

Resources
---------

* [Sudoers File](https://www.garron.me/en/linux/visudo-command-sudoers-file-sudo-default-editor.html)
* [AWS NTP](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html)
* [Fail2Ban](https://help.ubuntu.com/community/Fail2ban)
* [Postgresql](https://help.ubuntu.com/community/PostgreSQL)
