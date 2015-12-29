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

**/etc/hosts**
```bash
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

**/etc/ssh/sshd_config**
```bash
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
0 0 * * 0 apt-get update && { date; apt-get -qy upgrade; } >>/var/log/apt/auto-updates.log
```

Install `fail2ban` to monitor unsuccessful login attempts and ban IP addresses with too many failures.

```bash
grader@ip-10-20-26-132:~$ sudo apt-get install fail2ban
grader@ip-10-20-26-132:~$ sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
grader@ip-10-20-26-132:~$ sudo vi /etc/fail2ban/jail.local
```

**/etc/fail2ban/jail.local**
```bash
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

Install and configure `postgres` database. By creating a `postgres` user and database with the name `grader`, we provide authentication for any connections from the same machine (which is all we need for this application). Also, add a password so that Apache can connect by URI.

```bash
grader@ip-10-20-26-132:~$ sudo apt-get install postgresql
grader@ip-10-20-26-132:~$ sudo -u postgres createuser --createdb grader
grader@ip-10-20-26-132:~$ sudo -u postgres createdb grader
grader@ip-10-20-26-132:~$ sudo -u postgres psql
psql (9.3.10)
Type "help" for help.

postgres=# \password grader
Enter new password: 
Enter it again: 
postgres=# \q
```

Install `Apache` and `mod-wsgi`, ensure `mod-wsgi` is enabled, and verify that server is reachable at port 80.

```bash
grader@ip-10-20-26-132:~$ sudo apt-get install apache2 libapache2-mod-wsgi
grader@ip-10-20-26-132:~$ sudo a2enmod wsgi 
Module wsgi already enabled
grader@ip-10-20-26-132:~$ exit
logout
Connection to 52.27.202.14 closed.
brenj@ubuntu:~$ curl -I http://52.27.202.14
HTTP/1.1 200 OK
Date: Mon, 28 Dec 2015 19:42:55 GMT
Server: Apache/2.4.7 (Ubuntu)
Last-Modified: Mon, 28 Dec 2015 18:34:39 GMT
ETag: "2cf6-527f98ec40c88"
Accept-Ranges: bytes
Content-Length: 11510
Vary: Accept-Encoding
Content-Type: text/html
```

Install [Tech Quote](https://github.com/brenj/udacity/tree/master/item_catalog) dependencies and application on server.

```bash
grader@ip-10-20-26-132:~$ sudo apt-get install git python-pip libpq-dev python-dev
grader@ip-10-20-26-132:~$ sudo pip install virtualenv
Downloading/unpacking virtualenv
  Downloading virtualenv-13.1.2-py2.py3-none-any.whl (1.7MB): 1.7MB downloaded
Installing collected packages: virtualenv
Successfully installed virtualenv
Cleaning up...
grader@ip-10-20-26-132:~$ git clone https://github.com/brenj/udacity.git
Cloning into 'udacity'...
remote: Counting objects: 3733, done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 3733 (delta 16), reused 0 (delta 0), pack-reused 3694
Receiving objects: 100% (3733/3733), 2.37 MiB | 0 bytes/s, done.
Resolving deltas: 100% (2214/2214), done.
Checking connectivity... done.
grader@ip-10-20-26-132:~$ sudo cp -r udacity/item_catalog /var/www/tq
grader@ip-10-20-26-132:~$ ls /var/www/tq/
bin  bower.json  docs  Makefile  manage.py  migrations  Procfile  README.md  requirements.txt  tech_quote
grader@ip-10-20-26-132:~$ rm -rf udacity/
grader@ip-10-20-26-132:~$ sudo chown -R grader:grader /var/www/tq
grader@ip-10-20-26-132:~$ cd /var/www/tq/
grader@ip-10-20-26-132:/var/www/tq$ virtualenv venv && . venv/bin/activate
New python executable in venv/bin/python
Installing setuptools, pip, wheel...done.
grader@ip-10-20-26-132:/var/www/tq$ vi .env 
```

**/var/www/tq/.env**
```bash
APP_SETTINGS=tech_quote.config.ProductionConfig
DATABASE_URI=postgresql+psycopg2:///tq
GITHUB_ID='<id>'
GITHUB_SECRET='<secret>'
TQ_SECRET='<secret>'
```

```bash
(venv)grader@ip-10-20-26-132:/var/www/tq$ . bin/set-env-vars.sh
(venv)grader@ip-10-20-26-132:/var/www/tq$ echo $APP_SETTINGS
tech_quote.config.ProductionConfig
(venv)grader@ip-10-20-26-132:/var/www/tq$ make install
(venv)grader@ip-10-20-26-132:/var/www/tq$ psql tq
psql (9.3.10)
Type "help" for help.

tq=> \d
                   List of relations
 Schema |           Name           |   Type   | Owner  
--------+--------------------------+----------+--------
 public | alembic_version          | table    | grader
 public | author                   | table    | grader
 public | author_author_id_seq     | sequence | grader
 public | category                 | table    | grader
 public | category_category_id_seq | sequence | grader
 public | quote                    | table    | grader
 public | quote_quote_id_seq       | sequence | grader
 public | role                     | table    | grader
 public | role_role_id_seq         | sequence | grader
 public | tq_user                  | table    | grader
 public | tq_user_user_id_seq      | sequence | grader
(11 rows)

tq=> \q
(venv)grader@ip-10-20-26-132:/var/www/tq$ make prod
# Starting web server (production)
honcho start prod_server
21:43:01 system        | prod_server.1 started (pid=25296)
21:43:02 prod_server.1 | /var/www/tq/venv/local/lib/python2.7/site-packages/flask_sqlalchemy/__init__.py:800: UserWarning: SQLA
LCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True to suppress
 this warning.
21:43:02 prod_server.1 |   warnings.warn('SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by defa
ult in the future.  Set it to True to suppress this warning.')
21:43:02 prod_server.1 |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
^C
(venv)grader@ip-10-20-26-132:/var/www/tq$ deactivate
```

Add and enable a new `Apache` virtual host.

```bash
(venv)grader@ip-10-20-26-132:/var/www/tq$ sudo vi /etc/apache2/sites-available/tq.conf
```

**/etc/apache2/sites-available/tq.conf**
```apache
<VirtualHost *:80>
  ServerName 52.27.202.14
  ServerAdmin grader@52.27.202.14
  WSGIScriptAlias / /var/www/tq/tq.wsgi
  <Directory /var/www/tq/tech_quote/>
        Order allow,deny
        Allow from all
  </Directory>
  Alias /static /var/www/tq/tech_quote/static
  <Directory /var/www/tq/tech_quote/static/>
        Order allow,deny
        Allow from all
  </Directory>
  ErrorLog ${APACHE_LOG_DIR}/error.log
  LogLevel warn
  CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
grader@ip-10-20-26-132:/var/www/tq$ sudo a2ensite tq
Enabling site tq.
To activate the new configuration, you need to run:
  service apache2 reload
```

Add WSGI application file. Include the `tech_quote` package, environment variables, secret key, and add reference to site packages directory for the virtual environment.

```bash
grader@ip-10-20-26-132:/var/www/tq$ vi tq.wsgi
```

```python
# /var/www/tq/tq.wsgi 
import logging
import os
import site
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.append('/var/www/tq/')

VIRTUAL_ENVIRONMENT = '/var/www/tq/venv'
site.addsitedir(
    os.path.join(VIRTUAL_ENVIRONMENT, 'lib/python2.7/site-packages'))

os.environ['APP_SETTINGS'] = 'tech_quote.config.ProductionConfig'
os.environ['DATABASE_URI'] = 'postgresql+psycopg2://grader:<password>@localhost/tq'
os.environ['GITHUB_ID'] = '<id>'
os.environ['GITHUB_SECRET'] = '<secret>'
os.environ['TQ_SECRET'] = '<secret>'

from tech_quote.app import create_app

application = create_app()
application.secret_key = 'secret'
```

Allow Apache to write to static directory and image uploads directory.

```bash
grader@ip-10-20-26-132:/var/www/tq$ sudo chmod -R 775 tech_quote/static/
grader@ip-10-20-26-132:/var/www/tq$ sudo chown -R grader:www-data tech_quote/static/
```

Update the Authorization callback URL on GitHub, restart the Apache server, and validate site is up.

```bash
grader@ip-10-20-26-132:/var/www/tq$ sudo service apache2 restart
 * Restarting web server apache2
AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.0.1. Set the 'ServerName' directive globally to suppress this message
   ...done.
```

Resources
---------

* [Sudoers File](https://www.garron.me/en/linux/visudo-command-sudoers-file-sudo-default-editor.html)
* [AWS NTP](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html)
* [Fail2Ban](https://help.ubuntu.com/community/Fail2ban)
* [Postgresql](https://help.ubuntu.com/community/PostgreSQL)
* [Apache+WSGI](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)
