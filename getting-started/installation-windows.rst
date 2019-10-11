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
MSYS2 provides a bash shell, Autotools, revision control systems and the like for building native Windows applications using MinGW-w64 toolchains. Tool can be installed from official website <https://www.msys2.org>. Download and run the installer - "x86_64" for 64-bit, "i686" for 32-bit Windows. Currently we go for 64 bit system. Installation procedure is well explained on website.

Once instalaltion in complete, Open "MSYS2 MSYS" or "MSYS MinGW 64-bit". It shall provide you bash which resembles linux command shell. 
Update MSYS2 with following command

::

    $ pacman -Syu
  
After finished Close the bash (do not exit). Open bash again and run the same command again to finish the updates.

``tar`` is also needed to unpack the EPICS base

::

    $ pacman -S tar
Install ``perl``

::

    $ pacman -S perl

Install ``make``


::

    $ pacman -S make

Install ``gcc`` for 64-bit environment


::

    $ pacman -S mingw-w64-x86_64-gcc
    resolving dependencies...
    looking for conflicting packages...

    Packages (14) mingw-w64-x86_64-binutils-2.32-3
                  mingw-w64-x86_64-crt-git-7.0.0.5524.2346384e-1
                  mingw-w64-x86_64-gcc-libs-9.2.0-2  mingw-w64-x86_64-gmp-6.1.2-1
                  mingw-w64-x86_64-headers-git-7.0.0.5524.2346384e-1
                  mingw-w64-x86_64-isl-0.21-1  mingw-w64-x86_64-libiconv-1.16-1
                  mingw-w64-x86_64-libwinpthread-git-7.0.0.5522.977a9720-1
                  mingw-w64-x86_64-mpc-1.1.0-1  mingw-w64-x86_64-mpfr-4.0.2-2
                  mingw-w64-x86_64-windows-default-manifest-6.4-3
                  mingw-w64-x86_64-winpthreads-git-7.0.0.5522.977a9720-1
                  mingw-w64-x86_64-zlib-1.2.11-7  mingw-w64-x86_64-gcc-9.2.0-2

    Total Download Size:    58.53 MiB
    Total Installed Size:  428.12 MiB

    :: Proceed with installation? [Y/n] y
    
    
Check everything is installed properly,

::

    $ pacman -Q make perl mingw-w64-x86_64-gcc
    make 4.2.1-1
    perl 5.30.0-1
    mingw-w64-x86_64-gcc 9.2.0-2
    
Install EPICS
-------------

::

    $ cd $HOME
    $ wget https://epics-controls.org/download/base/base-7.0.3.tar.gz
    $ tar -xvf base-7.0.3.tar.gz
    $ cd base-7.0.3
    $ export EPICS_HOST_ARCH=windows-x64-mingw
    $ make

There should be lots of warnings, but no error. 

Test EPICS
----------

Run ``softIoc`` and, if everything is ok, you should see an EPICS prompt.

::

    softIoc
    epics>

You can exit with ctrl-c or by typing exit.

Voilà.

Ok, now you know that EPICS is installed correctly.
