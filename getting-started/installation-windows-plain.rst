Installation on plain Windows
=============================

Install Tools
-------------

Perl
^^^^

Install Strawberry Perl or ActivePerl using the Windows installers available on their download pages.

Make sure their locations are added to the system environment variable Path. Inside a shell (command prompt) they should be callable using their simple name, e.g.

::

    >perl --version

    This is perl 5, version 26, subversion 1 (v5.26.1) built for MSWin32-x64-multi-thread
    (with 1 registered patch, see perl -V for more detail)

    Copyright 1987-2017, Larry Wall

    Binary build 2601 [404865] provided by ActiveState http://www.ActiveState.com
    Built Dec 11 2017 12:23:25
    ...

GNU Make
^^^^^^^^

Strawberry Perl contains a suitable version of GNU Make. Otherwise, you can download a Windows executable that Andrew provides at https://epics.anl.gov/download/tools/make-4.2.1-win64.zip. Unzip it into a location (path must not contain spaces or parentheses) and add it to the system environment, so that

::

    >make --version
    GNU Make 4.2.1
    Built for x86_64-w64-mingw32
    Copyright (C) 1988-2016 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

Python
^^^^^^

Same procedure: install using the official downloader and put the location in the Path, so that you can call it as

::

    >python --version
    Python 3.8.6

Install the compiler
--------------------

Get the Visual Studio Installer and install. Make sure you enable the Programming Languages / C++ Development options.

In VS 2019, you also have the option to additionally install the Visual C++ 2017 compilers, if that is interesting for you.
    
Install EPICS
-------------

1. Download the distribution from e.g. https://epics-controls.org/download/base/base-7.0.4.1.tar.gz.
2. Unpack it into a work directory.
3. Open a shell (command prompt, MSYS2 bash, ...) and change into the directory you unpacked EPICS Base into.

   **Note: The current directory mustn't contain any spaces or parentheses. If it does, you can do another cd into the same directory, replacing every component containing spaces or parentheses with its Windows short path (can be displayed with ``dir /x``).**
4. Set the EPICS host architecture (windows-x86 for 64bit builds, win32-x86 for 32bit builds).
5. Run the ``vcvarsall.bat`` script of your installation (exact path depends on the type and language of installation) to set the environment for your build.
6. Run ``make``.

::

    >cd base-R7.0.4.1
    >set EPICS_HOST_ARCH=windows-x64
    >"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
    **********************************************************************
    ** Visual Studio 2019 Developer Command Prompt v16.6.2
    ** Copyright (c) 2020 Microsoft Corporation
    **********************************************************************
    [vcvarsall.bat] Environment initialized for: 'x64'

    >make

There will probably be warnings, but there should be no error. You can choose any EPICS base to install, the procedure remains the same.

Using EPICS from MSYS2 Bash
---------------------------

As long as you haven't added the location of your programs to the `%PATH%` environment variable (see below), you will have to provide the whole path to run commands or `cd` into the directory they are located in and prefix "./".

Replace 'user' with the Windows user folder name existing in your Windows installation.

Run ``softIoc`` and, if everything is ok, you should see an EPICS prompt.

::

    $ cd /c/Users/'user'/base-R7.0.4.1/bin/windows-x64
    $ ./softIoc -x test
    Starting iocInit
    iocRun: All initialization complete
    dbLoadDatabase("C:\Users\'user'\base-R7.0.4.1\bin\windows-x64\..\..\dbd\softIoc.dbd")
    softIoc_registerRecordDeviceDriver(pdbbase)
    iocInit()
    ############################################################################
    ## EPICS R7.0.4.1
    ## Rev. 2020-10-21T12:17+0200
    ############################################################################
    epics>

You can exit with ctrl-c or by typing exit.

Voilà.

Now you know that EPICS is installed correctly. If you type 'dbl' you should get a list of the `records` that your IOC provides as PVs (process variables).

Using EPICS from plain Windows
------------------------------

Open a shell, e.g., the Windows command prompt. Again, 'user' is the Windows user folder name.

::

    >cd C:\Users\'user'\base-R7.0.4.1\bin\windows-x64
    >softIoc -x test
    dbLoadDatabase("C:\Users\'user'\base-R7.0.4.1\bin\windows-x64\..\..\dbd\softIoc.dbd")
    softIoc_registerRecordDeviceDriver(pdbbase)
    iocInit()
    Starting iocInit
    ############################################################################
    ## EPICS R7.0.4.1
    ## Rev. 2020-10-21T12:17+0200
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
3. Add EPICS BASE path here. In ``Variable Name``, Put "EPICS_BASE". In ``Variable Path``, put "C:\Users\'user'\base-R7.0.4.1"
4. One more variable to describe host architecture. In ``Variable Name``, put EPICS_HOST_ARCH. In ``Variable Value``, put "windows-x64"
5. Navigate to the variable called ``Path``. Press Edit. 
6. To add the path for the EPICS commands, Press New again and put ``%EPICS_BASE%\bin\%EPICS_HOST_ARCH%``. Press ok twice and you are done.
7. Restart the Machine and check if EPICS commands like ``caget`` and ``camonitor`` are being recognized as valid commands in any location.

This should finish setting up EPICS environment in your Windows machine.

To check if the architecture is properly set,

in Windows ``command prompt``,

::

    > set EPICS_HOST_ARCH
    EPICS_HOST_ARCH=windows-x64


in MSYS2 ``bash``

::

    $ echo $EPICS_HOST_ARCH
    windows-x64


Simple Check for Process Variables
----------------------------------

Let's test some basic commands and a simple Process Variable in the Windows ``command prompt``. Prepare a file ``test.db`` in ``C:\Users\'user'\epics-test`` that reads like,

::

    record(ai, "temperature:water")
    {
        field(DESC, "Water temperature in the fish tank")
    }

This file defines a record instance called ``temperature:water``, which is an analog input (ai) record. Its DESC field defines a description. Now we start the `softIoc` again, but this time using our record database.

::

    > cd epics-test
    > softIoc -d test.db
    dbLoadDatabase("C:\Users\'user'\base-R7.0.4.1\bin\windows-x64\..\..\dbd\softIoc.dbd")
    softIoc_registerRecordDeviceDriver(pdbbase)
    dbLoadRecords("test.db")
    iocInit()
    Starting iocInit
    ############################################################################
    ## EPICS R7.0.4.1
    ## Rev. 2020-10-21T12:17+0200
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

    temperature:water              2020-10-23 13:21:57.739281 23
    temperature:water              2020-10-23 13:22:02.639010 24
    temperature:water              2020-10-23 13:22:06.184726 27
    temperature:water              2020-10-23 13:22:10.590232 28.1

This concludes the installation of EPICS Base, setting the Windows environment variables and some basic tests of your EPICS installation. We can use this toolchain for building EPICS and IOCs. Executables created from that process can be run on Windows using the MSYS2 Bash shell or the command prompt.
