Installation on Windows
=======================================

What is EPICS about?
-----------------------------------
We assume that you know more or less what EPICS is. Here we want to start 
from scratch and get to the point where we have a working server, then you 
get on other how-tos to take you further. 

Prepare your system
-------------------

You need ``make``, ``c++`` and ``libreadline`` to compile from source. 
On Windows these dependencies can be installed by using msys2 tool. 
This tool is available windows 7 onwards only. Currently this Installation is 
tested only on windows 8.1. It should work for all the version of windows.
In case we test it for other version, We will update the document.

Install Tools
-------------------
1) MSYS2 provides a bash shell, Autotools, revision control systems and the like for building native Windows applications using MinGW-w64 toolchains. Tool can be installed from official website <https://www.msys2.org>. Download and run the installer - "x86_64" for 64-bit, "i686" for 32-bit Windows. Currently we go for 64 bit system. Installation procedure is well explained on website.

Once instalaltion in complete, Open "MSYS2 MSYS" or "MSYS MinGW 64-bit". It shall provide you bash which resembles linux command shell.

2)make

