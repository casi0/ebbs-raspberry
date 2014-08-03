Welcome to Eagles BBS 3.1.1

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2, or (at your option)
any later version. See the COPYING file for further information.

Eagles BBS 3 is a standalone, screen-oriented bulletin board package. 
It is the successor to Eagles BBS version 2, which was built upon Ed Luke's
Pirates BBS package. The user interface from those programs has been kept
intact for the most part, and some code has been reused. For the most part
this is a complete rewrite though, to correct some basic limitations and
inefficiencies present in Pirates and Eagles 2.x. 

This software has a fairly full-featured message posting and private mail
system, its own IRC-like chat system, and private talk facility. It has
configurable menus allowing custom arrangement of the builtin functions 
and any external programs you care to hook in.

One thing Eagles BBS is not suited for quite yet is as a fancy shell. 
All BBS users run as a single user, so things like shell access and
news do not integrate very well. You should probably look elsewhere if
BBS users are to be anything more than guests on your system.

One improvement over Pirates and old Eagles is much greater runtime
configuration. A lot of stuff you used to have to recompile to change is
now in config files read in at runtime. All of these files are ASCII so
they may be patched with an editor if needed. The stock config files are
in the config directory and reside in ~bbs/etc at runtime.

ebbs-raspberry
==============

Ebbs for rapsberry pi

Installation:

* Fresh install of raspbian

* curl -O https://raw.githubusercontent.com/casi0/ebbs-raspberry/master/install.py

* sudo python install.py
