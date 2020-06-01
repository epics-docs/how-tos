Installation on Windows
=======================================

Introduction
-----------------------------------
We assume that you know more or less what EPICS is. You can get basic idea from https://epics-controls.org/about-epics/. Here we want to start from scratch on windows system and get to the point where we have a working server, then you get on other how-tos to take you further. 

Prepare your system
-------------------

You Need 'C++ Libraries', 'GNU make'  and 'GCC' to compile from source. On Windows these dependencies can be installed by using msys2 tool. This tool is available windows 7 onwards only. Currently this procedure is verified on windows 8.1 (64 bit) and Windows 10 (64 bit). But, It should work for all the version of windows. In case we test it for other versions, We will update the document.

Install Tools
-------------------
MSYS2 provides a bash shell, Autotools, revision control systems and the like for building native Windows applications using MinGW-w64 toolchains. Tool can be installed from official website <https://www.msys2.org>. Download and run the installer - "x86_64" for 64-bit, "i686" for 32-bit Windows. Currently we go for 64 bit system. Installation procedure is well explained on website.

Once installation in complete, you have three options available. Launch "MSYS MinGW 64-bit" option (MSYS2 and 32-bit option fails to compile EPICS). It shall provide you bash which resembles linux command shell. 
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

Install ``mingw-gcc`` for 64-bit environment


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
    
Install ``gcc`` 


::

    $ pacman -S gcc
        
Check everything is installed properly,

::

    $ pacman -Q make perl mingw-w64-x86_64-gcc gcc
    make 4.2.1-1
    perl 5.30.0-1
    mingw-w64-x86_64-gcc 9.2.0-2
    gcc 9.1.0-2
    
Install EPICS
-------------

::

    $ cd $HOME
    $ wget https://epics-controls.org/download/base/base-7.0.3.1.tar.gz
    $ tar -xvf base-7.0.3.1.tar.gz
    $ cd base-7.0.3.1
    $ export EPICS_HOST_ARCH=windows-x64-mingw
    $ make

There should be lots of warnings, but no error. 

Test EPICS in Msys environment
------------------------

Run ``softIoc`` and, if everything is ok, you should see an EPICS prompt. You need to provide whole path here, as newly executables is yet not recognised as commands by widnows. That is need to be set by windows "edit the system environment variables". After that it directly works as commands. Replace 'user' with actual windows user name folder existing in your windows installation.

::

    $ /home/'user'/base-7.0.3.1/bin/windows-x64-mingw/softIoc
    epics>

You can exit with ctrl-c or by typing exit.

Voilà.

Ok, now you know that EPICS is installed correctly.

Test EPICS in Windows
---------------------

Exit or minimise Msys2 environment. Open windows command prompt. Here 'user' is windows-user/account folder name.

::

    > cd c:\msys64\home\'user'\base-7.0.3.1\bin\windows-x64-mingw
    > softIoc.exe -x test
        Starting iocInit
        ############################################################################
        ## EPICS R7.0.3.1
        ## EPICS Base built Apr 16 2020
        ############################################################################
        iocRun: All initialization complete
        epics>

Normal EPICS commands like caget, caput will still not work, as windows doesn't recognise them as valid commands. You have to add those paths in windows Environment Variable. Go to Start Manu, Type "environment" and select ``Edit the system Environment Variables``. 

1. Select ``Advance`` tab, navigate to ``Environment Variables`` button. That should open editable Tables of Path for Windows Environmet. 
2. In ``User Variable for 'user'`` option, Press NEW
3. Add EPICS BASE path here. In ``Variable Name``, Put "EPICS_BASE". In ``Variable Path``, put ``C:\msys64\home\'user'\base-7.0.3.1``
4. One more variable to describe host architecture. In ``Variable Name``, put EPICS_HOST_ARCH. In ``Variable Value``, put "windows-x64-mingw"
5. Now, Navigate to Variable called ``Path``. Press Edit. 
6. To add new Path for EPICS commands, Press New again and put ``%EPICS_BASE%\bin\%EPICS_HOST_ARCH%``. Alternatively you can also put whole path as ``C:\msys64\home\'user'\base-7.0.3.1\bin\windows-x64-mingw`` Press ok two times and you are done.
7. Restart the Machine and check if ``caget`` and ``camonitor`` is being recognised as valid commands.

This should finish setting up EPICS environment in your windows machine. Let's test some basic commands and simple Process variable in windows ``command prompt``.

prepare a file ``test.db`` in ``C:\msys64\home\'user'\base-7.0.3.1\bin\windows-x64-mingw`` that reads like,

::

    record(ai, "temperature:water")
    {
        field(DESC, "Water temperature in the fish tank")
    }

This file defines a record instance called ``temperature:water``, which is an analog input (ai) record. As you can imagine DESC stays for Description. Now we start softIoc again, but this time using this record database.

::

    > cd cd c:\msys64\home\'user'\base-7.0.3.1\bin\windows-x64-mingw
    > softIoc -d test.db
    iocInit()
    Starting iocInit
    ############################################################################
    ## EPICS R7.0.3.1
    ## EPICS Base built Apr 16 2020
    ############################################################################
    iocRun: All initialization complete
    
Now, from your EPICS prompt, you can list the available records with the ``dbl`` command and you will see something like

::

    epics> dbl
    temperature:water

Open one more terminal (call it t2),

::

    camonitor temperature:water
    
Open a new terminal (call it t3) and try to change value of PV using ``caput``. you can also readback using ``caget``.

::

    >caput temperature:water 23
    Old : temperature:water              0
    New : temperature:water              23
    
    >caput temperature:water 24
    Old : temperature:water              23
    New : temperature:water              24
    
    >caput temperature:water 27
    Old : temperature:water              24
    New : temperature:water              27
    
    >caput temperature:water 28.1
    Old : temperature:water              27
    New : temperature:water              28.1

    >caget temperature:water
    temperature:water              28.1

Monitor changes in terminal t2,

::

    temperature:water              2020-04-22 17:52:58.752021 23
    temperature:water              2020-04-22 17:53:03.008201 24
    temperature:water              2020-04-22 17:53:06.053267 27
    temperature:water              2020-04-22 17:53:09.003619 28.1

This concludes EPICS installation, Windows Environment variable settings and EPICS basic testing. We can ``MSYS2`` for building EPICS and IOCs. Files and EPICS executable created from that process can be run in windows environment using ``command prompt``.

Create a demo/test ioc
----------------------

All though ``softIoc`` can be used with multiple instances with different db files, you may need to create your own ``ioc`` for any number of reasons. We will create one test ioc from existing templates using ``makeBaseApp.pl`` script.

Let's create one IOC, which takes value of 2 process variables and add it and store it in 3rd process variable.

We will need ``MSYS2`` for building ``ioc``. Open ``MSYS2 Mingw 64-bit``. Go to EPICS base and create a new directory ``testioc`` below EPICS base.

::

    $ cd /home/'user'/base-7.0.3.1/
    $ mkdir testioc
    $ cd testioc
    
from ``testioc`` folder run following,

::

    $ ../bin/windows-x64-mingw/makeBaseApp.pl -t ioc test
    $ ../bin/windows-x64-mingw/makeBaseApp.pl -i -t ioc test
    Using target architecture windows-x64-mingw (only one available)
    The following applications are available:
        test
    What application should the IOC(s) boot?
    The default uses the IOC's name, even if not listed above.
    Application name?
    
Accept the default name and press enter. That should generate a skeleton for your ``testioc``.

::

    $ ls
    configure  iocBoot  Makefile  testApp
    
Now create a ``db`` file which describes PVs for your ``IOC``. Go to ``testApp\db`` and create ``test.db`` file with following record details.

::

    record(ai, "test:pv1")
    {
        field(VAL, 49)
    }

    record(ai, "test:pv2")
    {
        field(VAL, 51)
    }
    record(calc,"test:add")
    {
        field(SCAN,"1 second")
        field(INPA, "test:pv1")
        field(INPB, "test:pv2")
        field("CALC", "A + B")
    }
    
Now open ``Makefile`` and navigate to,

::

    #DB += xxx.db``

Remove # and change this to ``test.db`` ,

::

    DB += test.db``

Go to back to root folder for IOC ``testioc``. Go to ``iocBoot\ioctest``. Modify ``st.cmd`` file.

Change

::

    #dbLoadRecords("db/xxx.db","user=XXX")``

to

::

    dbLoadRecords("db/test.db","user=XXX")``

Save all the files and go back to ``MSYS2`` terminal,

go to ioc root folder and run ``make``,

::

    $ cd /base-7.0.3.1/testioc
    $ export EPICS_HOST_ARCH=windows-x64-mingw
    $ make

It should create all the files required for test ioc,

::
    
    $ ls
    bin  configure  db  dbd  iocBoot  lib  Makefile  testApp

Now we go back to windows. Go to ``\testioc\iocBoot\ioctest`` . Open ``envPaths`` file and change relative paths to full paths

from,

::

    epicsEnvSet("IOC","ioctest")
    epicsEnvSet("TOP","/home/'user'/base-7.0.3.1/testioc")
    epicsEnvSet("EPICS_BASE","/home/'user'/base-7.0.3.1/testioc/..")

to

::

    epicsEnvSet("IOC","ioctest")
    epicsEnvSet("TOP","C:/msys64/home/'user'/base-7.0.3.1/testioc")
    epicsEnvSet("EPICS_BASE","C:/msys64/home/'user'/base-7.0.3.1")

Save file.

go back to windows ``command prompt``,

::

    > cd C:\msys64\home\'user'\base-7.0.3.1\testioc\iocBoot\ioctest
    > C:\msys64\home\'user'\base-7.0.3.1\testioc\iocBoot\ioctest>..\..\bin\windows-x64-mingw\test.exe st.cmd
    #!../../bin/windows-x64-mingw/test
    < envPaths
    epicsEnvSet("IOC","ioctest")
    epicsEnvSet("TOP","C:/msys64/home/'user'/base-7.0.3.1/testioc")
    epicsEnvSet("EPICS_BASE","C:/msys64/home/'user'/base-7.0.3.1")
    cd "C:/msys64/home/'user'/base-7.0.3.1/testioc"
    ## Register all support components
    dbLoadDatabase "dbd/test.dbd"
    test_registerRecordDeviceDriver pdbbase
    Warning: IOC is booting with TOP = "C:/msys64/home/'user'/base-7.0.3.1/testioc"
              but was built with TOP = "/home/'user'/base-7.0.3.1/testioc"
    ## Load record instances
    dbLoadRecords("db/test.db","user='user'")
    cd "C:/msys64/home/'user'/base-7.0.3.1/testioc/iocBoot/ioctest"
    iocInit
    Starting iocInit
    ############################################################################
    ## EPICS R7.0.3.1
    ## EPICS Base built Apr 16 2020
    ############################################################################
    iocRun: All initialization complete
    ## Start any sequence programs
    #seq sncxxx,"user='user'"
    epics>

Check if database ``test.db`` you created is loaded correctly

::

    epics> dbl
    test:add
    test:pv1
    test:pv2

Open other ``commad prompt`` (call it t2) for monitoring  ``test:add``. type "camonitor test:add"

::

    > camonitor test:add
    > test:add                       2020-04-22 18:47:59.692169 100

Open one ``command prompt`` (call it t3). using caput modify values of  ``test:pv1`` and ``test:pv2``. You shall see changes in terminal t2 accordingly
  
