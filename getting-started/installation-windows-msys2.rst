Installation using MSYS2 
========================

Here we will use MSYS2, as it has all the required tools available through an easy-to-use package manager, and its bash shell looks and feels like working on Linux. Most Bash commands are similar to their Linux versions. MSYS2 is available for Windows 7 and up only. The following procedure is verified on Windows 8.1 (64 bit) and Windows 10 (64 bit). Please report any unexpected behavior, so we can keep these instructions up-to-date.

Install Tools
-------------
MSYS2 provides a Bash shell, Autotools, revision control systems and other tools for building native Windows applications using MinGW-w64 toolchains. It can be installed from its official `website <https://www.msys2.org>`_. Download and run the installer - "x86_64" for 64-bit, "i686" for 32-bit Windows. The installation procedure is well explained on the website. These instructions assume you are running on 64-bit Windows.

Once installation is complete, you have three options available for starting a shell. The difference between these options is the preset of the environment variables that select the compiler toolchain to use.
Launch the "MSYS MinGW 64-bit" option to use the MinGW 64bit toolchain, producing 64bit binaries that run on 64bit Windows systems. The "MSYS MinGW 32-bit" option will use the MinGW 32bit toolchain, producing 32bit binaries that will run on 32bit and 64bit Windows systems.

Again: you have a single installation of MSYS2, these different shells are just setups to use different compilers. Installation and update of your MSYS2 system only has to be done once - you can use any of the shell options for that.

Update MSYS2 with following command

::

    $ pacman -Syu
  
After this finishes, close the bash (do not exit). Open bash again and run the same command again to finish the updates.

Install the necessary tools

::

    $ pacman -S tar make perl python

Packages with such "simple" names are part of the MSYS2 environment and work for all compilers/toolchains that you may install on top on MSYS2.

Install compiler toolchains
---------------------------

Packages that are part of a mingw toolchain start with the prefix "mingw-w64-x86_64-" for the MinGW 64bit toolchain or "mingw-w64-i686-" for the MinGW 32bit toolchain.
(The "w64" part will be different when using a 32bit MSYS2 environment, e.g. on a 32bit Windows host.)

Install the MinGW 32bit and/or MinGW 64bit toolchains

::

    $ pacman -S mingw-w64-x86_64-toolchain
    $ pacman -S mingw-w64-i686-toolchain
    
Each toolchain needs about 600MB of disk space.
      
If you are not sure, check your set of tools is complete and everything is installed properly.

::

    $ pacman -Q
    ...
    make 4.3-1
    perl 5.32.0-2
    python-3.8.5-6
    mingw-w64-x86_64-...
    mingw-w64-i686-...
    ...

Update your installation regularly
----------------------------------

At any time, you can update your complete installation (including all tools and compiler toolchains) using

::

    $ pacman -Syu

You should do this regularly.

Download and build EPICS Base
-----------------------------

::

    $ cd $HOME
    $ wget https://epics-controls.org/download/base/base-7.0.4.1.tar.gz
    $ tar -xvf base-7.0.4.1.tar.gz
    $ cd base-R7.0.4.1
    $ export EPICS_HOST_ARCH=windows-x64-mingw
    $ make

When using the MinGW 32bit toolchain, the "MSYS MinGW 32-bit" shell must be used and EPICS_HOST ARCH must be set to "win32-x86-mingw".

During the compilation, there will be warnings, but there should be no error. You can choose any EPICS Base version to build, the procedure remains the same.

Using EPICS from MSYS2 Bash
---------------------------

As long as you haven't added the location of your programs to the `%PATH%` environment variable (see below), you will have to provide the whole path to run commands or `cd` into the directory they are located in and prefix "./".

Replace 'user' with the actual Windows user folder name existing in your Windows installation - MSYS2 creates your home directory using that name. We assume the default location for MSYS2 (`C:\msys64`).

Run ``softIoc`` and, if everything is ok, you should see an EPICS prompt.

::

    $ cd /home/'user'/base-R7.0.4.1/bin/windows-x64-mingw
    $ ./softIoc -x test
    Starting iocInit
    iocRun: All initialization complete
    dbLoadDatabase("C:\msys64\home\'user'\base-R7.0.4.1\bin\windows-x64-mingw\..\..\dbd\softIoc.dbd")
    softIoc_registerRecordDeviceDriver(pdbbase)
    iocInit()
    ############################################################################
    ## EPICS R7.0.4.1
    ## Rev. 2020-10-21T11:57+0200
    ############################################################################
    epics>

You can exit with ctrl-c or by typing exit.

Voilà.

Now you know that EPICS is installed correctly. If you type 'dbl' you should get a list of the `records` that your IOC provides as PVs (process variables).

Using EPICS from plain Windows
------------------------------

Open a shell, e.g., the Windows command prompt. Again, 'user' is the Windows user folder name.
The MSYS2 home folders are inside the MSYS2 installation.

If you built EPICS Base with dynamic (DLL) linking, you need to add the location of the C++ libraries to the `PATH` variable for them to be found. (Again, assuming a 64bit MSYS2 installation with default paths and the MinGW 64bit toolchain.)

::

    > set "PATH=%PATH%;C:\msys64\mingw64\bin"
    > cd C:\msys64\home\'user'\base-R7.0.4.1\bin\windows-x64-mingw
    > softIoc -x test
    Starting iocInit
    ############################################################################
    ## EPICS R7.0.4.1
    ## Rev. 2020-10-21T11:57+0200
    ############################################################################
    iocRun: All initialization complete
    epics>

As long as you are in the location of the EPICS Base binaries, they will all work using their simple names. Try commands like ``caput``, ``caget``, ``camonitor``, ...

Setting the system environment
------------------------------

In order to run all EPICS commands everywhere by using their simple name and to build more EPICS modules using the same setup, we will set three environment variables for the current user on the Windows system:

* EPICS_BASE
* EPICS_HOST_ARCH
* Path

Go to Start Manu, Type "environment" and select ``Edit the system Environment Variables``. 

1. Select ``Advance`` tab, navigate to ``Environment Variables`` button. That should open editable Tables of Path for Windows Environmet. 
2. In ``User Variable for 'user'`` option, Press NEW
3. Add EPICS BASE path here. In ``Variable Name``, Put "EPICS_BASE". In ``Variable Path``, put "C:\msys64\home\'user'\base-R7.0.4.1"
4. One more variable to describe host architecture. In ``Variable Name``, put EPICS_HOST_ARCH. In ``Variable Value``, put "windows-x64-mingw"
5. Navigate to the variable called ``Path``. Press Edit. 
6. To add the path for the MinGW64 DLLs, press New again and put ``C:\msys64\mingw64\bin`` Press ok.
7. To add the path for the EPICS commands, Press New again and put ``%EPICS_BASE%\bin\%EPICS_HOST_ARCH%``. Alternatively you can also put the whole path as ``C:\msys64\home\'user'\base-7.0.4.1\bin\windows-x64-mingw`` Press ok twice and you are done.
8. Restart the Machine and check if EPICS commands like ``caget`` and ``camonitor`` are being recognised as valid commands in any location.

This should finish setting up EPICS environment in your Windows machine.

To check if the architecture is properly set,

in Windows ``command prompt``,

::

    > set EPICS_HOST_ARCH
    EPICS_HOST_ARCH=windows-x64-mingw


in MSYS2 ``bash``

::

    $ echo $EPICS_HOST_ARCH
    windows-x64-mingw


Simple Check for Process Variables
----------------------------------

Let's test some basic commands and a simple Process Variable in the Windows ``command prompt``. Prepare a file ``test.db`` in ``C:\msys64\home\'user'\epics-test`` that reads like,

::

    record(ai, "temperature:water")
    {
        field(DESC, "Water temperature in the fish tank")
    }

This file defines a record instance called ``temperature:water``, which is an analog input (ai) record. Its DESC field defines a description. Now we start the `softIoc` again, but this time using our record database.

::

    > cd c:\msys64\home\'user'\epics-test
    > softIoc -d test.db
    dbLoadDatabase("C:\msys64\home\'user'\base-R7.0.4.1\bin\windows-x64-mingw\..\..\dbd\softIoc.dbd")
    softIoc_registerRecordDeviceDriver(pdbbase)
    dbLoadRecords("test.db")
    iocInit()
    Starting iocInit
    ############################################################################
    ## EPICS R7.0.4.1
    ## Rev. 2020-10-21T11:57+0200
    ############################################################################
    iocRun: All initialization complete
    epics>

  
From your EPICS prompt, you can list the available records with the ``dbl`` command and you will see something like

::

    epics> dbl
    temperature:water

Open a second terminal to monitor the value of that variable.

::

    camonitor temperature:water
    
Open a third terminal and try to change the value of the PV using ``caput``. you can also read the value back using ``caget``.

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

Monitor the changes in the second terminal:

::

    temperature:water              2020-10-23 12:59:05.064052 23
    temperature:water              2020-10-23 12:59:09.292389 24
    temperature:water              2020-10-23 12:59:15.472274 27
    temperature:water              2020-10-23 12:59:23.519760 28.1

This concludes the installation of EPICS Base, setting the Windows environment variables and some basic tests of your EPICS installation. We can use MSYS2 for building EPICS and IOCs. Executables created from that process can be run on Windows using the MSYS2 Bash shell or the command prompt.

Create a demo/test IOC
----------------------

Although ``softIoc`` can be used with multiple instances with different db files, you may need to create your own IOC at some point. We will create one test ioc from existing templates using ``makeBaseApp.pl`` script.

Let's create one IOC, which takes the values of 2 process variables (PVs), adds them and stores the result in 3rd PV.

We will use ``MSYS2`` for building the IOC. Open ``MSYS2 Mingw 64-bit``. Create a new directory ``testioc``.

::

    $ mkdir testioc
    $ cd testioc
    
From that ``testioc`` folder run the following.

::

    $ makeBaseApp.pl -t ioc test
    $ makeBaseApp.pl -i -t ioc test
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
    
Now create a ``db`` file which describes PVs for your ``IOC``. Go to ``testApp\Db`` and create ``test.db`` file with following record details.

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
    
Now open ``Makefile`` and navigate to

::

    #DB += xxx.db

Remove # and change this to ``test.db``.

::

    DB += test.db

Go to back to root folder for IOC ``testioc``. Go to ``iocBoot\ioctest``. Modify the ``st.cmd`` startup command file.

Change

::

    #dbLoadRecords("db/xxx.db","user=XXX")

to

::

    dbLoadRecords("db/test.db","user=XXX")

Save all the files and go back to the MSYS2 Bash terminal. Make sure the architecture is set correctly.

::

    $ echo $EPICS_HOST_ARCH
    windows-x64-mingw

Change into the testioc folder and run ``make``. 

::

    $ cd ~/testioc
    $ make

This should create all the files for the test IOC.

::
    
    $ ls
    bin  configure  db  dbd  iocBoot  lib  Makefile  testApp

Go to ``iocBoot/ioctest`` . Open the ``envPaths`` file and change the MSYS2 relative paths to full Windows paths

::

    epicsEnvSet("IOC","ioctest")
    epicsEnvSet("TOP","C:/msys64/home/'user'/testioc")
    epicsEnvSet("EPICS_BASE","C:/msys64/home/'user'/base-7.0.4.1")

**Note: You absolutely have to use Linux style forward slash characters for this file.**

At this point, you can run the IOC from either an MSYS2 Bash shell or from a Windows command prompt, by changing into the IOC directory and running the test.exe binary with your startup command script.

In the Windows ``command prompt``:

::

    >cd C:\msys64\home\'user'\testioc\iocBoot\ioctest    
    >..\..\bin\windows-x64-mingw\test st.cmd

In the MSYS2 shell:
    
::

    >cd ~/testioc/iocBoot/ioctest    
    >../../bin/windows-x64-mingw/test st.cmd


In both cases, the IOC should start like this

::

    Starting iocInit
    iocRun: All initialization complete
    #!../../bin/windows-x64-mingw/test
    < envPaths
    epicsEnvSet("IOC","ioctest")
    epicsEnvSet("TOP","C:/msys64/home/'user'/testioc")
    epicsEnvSet("EPICS_BASE","C:/msys64/home/'user'/base-R7.0.4.1")
    cd "C:/msys64/home/'user'/testioc"
    ## Register all support components
    dbLoadDatabase "dbd/test.dbd"
    test_registerRecordDeviceDriver pdbbase
    Warning: IOC is booting with TOP = "C:/msys64/home/'user'/testioc"
              but was built with TOP = "/home/'user'/testioc"
    ## Load record instances
    dbLoadRecords("db/test.db","user='user'")
    cd "C:/msys64/home/'user'/testioc/iocBoot/ioctest"
    iocInit
    ############################################################################
    ## EPICS R7.0.4.1
    ## Rev. 2020-10-21T11:57+0200
    ############################################################################
    ## Start any sequence programs
    #seq sncxxx,"user='user'"
    epics>

Check if the database ``test.db`` you created is loaded correctly

::

    epics> dbl
    test:pv1
    test:pv2
    test:add

As you can see 3 process variable is loaded and available. Keep this terminal open and running. Test this process variable using another terminals.

Open another shell for monitoring ``test:add``.
::

    >camonitor test:add
    test:add                       2020-10-23 13:39:14.795006 100

That terminal will monitor the PV ``test:add`` continuously. If any value change is detected, it will be updated in this terminal. Keep it open to observe the behaviour.

Open a third shell. Using caput, modify the values of  ``test:pv1`` and ``test:pv2`` as we have done in the temperature example above. You will see changes of their sum in the second terminal accordingly.

At this point, you have one IOC ``testioc`` running, which loaded the database ``test.db`` with 3 records. From other processes, you can connect to these records using Channel Access. If you add more process variable in ``test.db``, you will have to ``make`` the `testioc` application again and restart the IOC to load the new version of the database.

You can also create and run IOCs like this in parallel with their own databases and process variables. Just keep in mind that each record instance has to have a unique name for Channel Access to work properly.
