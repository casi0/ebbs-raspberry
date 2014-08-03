#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :install.py
#description     :This will make instalation of ebbs-3.1.1 for raspberry-pi.
#author          :casi0
#date            :20140307
#version         :0.1
#usage           :sudo python installation.py

import os, sys

if not os.geteuid()==0:
    sys.exit("\nYou must be root to run this application, please use sudo and try again.\n")

print("* Update and upgrade raspbian\n")
os.system("apt-get update && apt-get upgrade")

print("* Install libncurses5-dev\n")
os.system("apt-get install libncurses5-dev")

print("* Install fail2ban\n")
os.system("apt-get install fail2ban")

bbs_account = "bbs:x:1001:1004:Bulletin Board System,,,:/home/bbs:/home/bbs/bin/lbbs"
test = ""

with open('/etc/passwd') as search:
    for line in search:
        line = line.rstrip()
        if bbs_account == line:
                        test = 0

if test != 0:
   with open('/etc/passwd', 'a') as test:
                test.write('\nbbs:x:1001:1004:Bulletin Board System,,,:/home/bbs:/home/bbs/bin/lbbs\n')
                test.write('bbsadm:x:1002:1004:BBS Administrator,,,:/home/bbs:/bin/bash\n')

bbs_account = "bbs:x:1004:bbs"
test1 = ""

with open('/etc/group') as search:
    for line in search:
        line = line.rstrip()
        if bbs_account == line:
                        test1 = 0

if test1 != 0:
   with open('/etc/group', 'a') as test:
                test.write('\nbbs:x:1004:bbs\n')
                test.write('\nbbsadm:x:1004:bbs\n')

sudo_owner = "bbsadm ALL=(ALL) NOPASSWD: ALL"
test2 = ""

with open('/etc/sudoers') as search:
    for line in search:
        line = line.rstrip()
        if sudo_owner == line:
                        test2= 0

if test2 != 0:
   with open('/etc/sudoers', 'a') as test:
                test.write('\nbbsadm ALL=(ALL) NOPASSWD: ALL\n')

print("\nFor connecting to the bbs add a password for this account for users.\n")
print("Enter the password for bbs account\n")
os.system("passwd bbs")

print("\nFor connecting to the bbsadm (bbs admin acoount) add a password for this account for administration of this bbs.\n")
print("Enter the password for bbsadm account\n")
os.system("passwd bbsadm")

print("* Create /home/bbs\n")
os.system("mkdir /home/bbs")
print("* Git clone ebbs rapsberry")
os.system("git clone https://github.com/casi0/ebbs-raspberry.git /home/bbs/")
print("* chmod 770 /home/bbs\n")
os.system("chmod 770 /home/bbs")
print("* chown -R bbs /home/\n")
os.system("chown -R bbs /home/")
print("* chgrp -R bbs /home/bbs\n")
os.system("chgrp -R bbs /home/bbs")
print("* Delete ssh printable headers")
os.system("touch /home/bbs/.hushlogin")
os.system("rm /etc/motd")
os.system("touch /etc/motd")


print ("* Installation finish\n")
