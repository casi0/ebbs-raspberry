ebbs-raspberry
==============

Ebbs for rapsberry pi

Installation:

* Fresh install of raspbian

* sudo raspi-config

* sudo apt-get update && apt-get upgrade

* sudo apt-get install libncurses5-dev

* git clone https://github.com/casi0/ebbs-raspberry.git /home/bbs/

* sudo nano /etc/passwd
bbs:x:1001:1004:Bulletin Board System,,,:/home/bbs:/home/bbs/bin/lbbs
bbsadm:x:1002:1004:BBS Administrator,,,:/home/bbs:/bin/bash

* sudo nano /etc/group
bbs:x:1004:bbs

* sudo nano /etc/sudoers
bbsadm ALL=(ALL) NOPASSWD: ALL

* sudo passwd bbs

* sudo passwd bbsadm

* sudo chown -R bbs /home/bbs

* sudo chgrp -R bbs /home/bbs

* sudo chmod 770 /home/bbs
