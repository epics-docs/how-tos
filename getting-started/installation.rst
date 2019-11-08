Installation on Linux/UNIX/DARWIN (Mac)
=======================================

What is EPICS about?
-----------------------------------
We assume that you know more or less what EPICS is. Here we want to start
from scratch and get to the point where we have a working server, offering some
PVs for reading (caget or pvget) and writing
(caput or pvput), and we read and write on them from
another terminal, either on the same machine or on another one in the same
network. If you are going to use two different machines, you will have to
repeat the steps for installing EPICS for both of them.

Prepare your system
-------------------

You need ``make``, ``c++`` and ``libreadline`` to compile from source. On macOS these
dependencies can be installed by using e.g. ``homebrew``. On Linux you
can use ``apt-get install``.

Install EPICS
-------------

::

    mkdir $HOME/EPICS
    cd $HOME/EPICS
    git clone --recursive https://github.com/epics-base/epics-base.git
    cd epics-base
    make

After compiling you should put the path into ``$HOME/.profile`` or into ``$HOME/.bashrc`` 
by adding the following to either one of those files:

::

    export EPICS_BASE=${HOME}/EPICS/epics-base
    export EPICS_HOST_ARCH=$(${EPICS_BASE}/startup/EpicsHostArch)
    export PATH=${EPICS_BASE}/bin/${EPICS_HOST_ARCH}:${PATH}

EpicsHostArch is a program provided by EPICS that returns the architecture 
of your system. 
Thus the code above should be fine for every architecture.

Test EPICS
----------
Now log out and log in again, so that your new path is set correctly.
Alternatively, you can execute the three lines above beginning with export 
directly from the terminal.

Run ``softIoc`` and, if everything is ok, you should see an EPICS prompt.

::

    softIoc
    epics>

You can exit with ctrl-c or by typing exit.

Voilà.

Ok, that is not very impressive, but at least you know that EPICS is
installed correctly. So now let us try something more complex, which will
hopefully suggest how EPICS works.

In whatever directory you like, prepare a file test.db that
reads like

::

    record(ai, "temperature:water")
    {
        field(DESC, "Water temperature in the fish tank")
    }

This file defines a record instance called temperature:water, which
is an analog input (ai) record. As you can imagine DESC stays for
Description. Now we start softIoc again, but this time using this
record database.

::

    softIoc -d test.db

Now, from your EPICS prompt, you can list the available records with the
dbl command and you will see something like

::

    epics> dbl
    temperature:water
    epics>

Open a new terminal (we call it nr. 2) and try the command line tools
caget and caput. You will see something like
::

    your prompt> caget temperature:water
    temperature:water              0
    your prompt> caget temperature:water.DESC
    temperature:water.DESC         Water temperature in the fish tank
    your prompt> caput temperature:water 21
    Old : temperature:water              0
    New : temperature:water              21
    your prompt> caput temperature:water 24
    Old : temperature:water              21
    New : temperature:water              24
    your prompt> caget temperature:water 
    temperature:water              24
     ... etc.

Now open yet another terminal (nr. 3) and try ``camonitor`` as

::

    camonitor temperature:water

First, have a look at what happens when you change the temperature:water
value from terminal nr. 2 using caput. Then, try to change the
value by some tiny amounts, like 15.500001, 15.500002, 15.500003… You will
see that camonitor reacts but the readings do not change. If you
wanted to see more digits, you could run

::

    camonitor -g8 temperature:water

For further details on the Channel Access protocol, including documentation
on the ``caput``, ``caget``, ``camonitor``...
command line tools, please refer to the `Channel Access Reference Manual <https://epics.anl.gov/base/R3-14/8-docs/CAref.html>`_.

In real life, however, it is unlikely that the 8 digits returned by your
thermometer (in this example) are all significant. We should thus limit the
traffic to changes of the order of, say, a hundredth of a degree. To do this,
we add one line to the file ``test.db``, so that it reads

::

    record(ai, "temperature:water")
    {
        field(DESC, "Water temperature in Lab 10")
        field(MDEL, ".01")
    }

MDEL stands for Monitor Deadband. If you now run

::

    softIoc -d test.db

with the new ``test.db`` file, you will see that
``camonitor`` reacts only to changes that are larger than 0.01.

This was just a simple example. Please refer to the `Record Reference Manual <https://epics.anl.gov/EpicsDocumentation/AppDevManuals/RecordRef/Recordref-1.html>`_ for further
information.

Create a demo/test ioc to test ca and pva
-----------------------------------------

::

    mkdir -p $HOME/EPICS/TEST/testIoc
    cd $HOME/EPICS/TEST/testIoc
    makeBaseApp.pl -t example testIoc
    makeBaseApp.pl -i -t example testIoc
    make
    cd iocBoot/ioctestIoc
    chmod u+x st.cmd
    ioctestIoc> ./st.cmd
    #!../../bin/darwin-x86/testIoc
    < envPaths 
    epicsEnvSet("IOC","ioctestIoc") 
    epicsEnvSet("TOP","/Users/maradona/EPICS/TEST/testIoc") 
    epicsEnvSet("EPICS_BASE","/Users/maradona/EPICS/epics-base") 
    cd "/Users/maradona/EPICS/TEST/testIoc" 
    ## Register all support components 
    dbLoadDatabase "dbd/testIoc.dbd" 
    testIoc_registerRecordDeviceDriver pdbbase 
    ## Load record instances dbLoadTemplate "db/user.substitutions" 
    dbLoadRecords "db/testIocVersion.db", "user=junkes" 
    dbLoadRecords "db/dbSubExample.db", "user=junkes" 
    #var mySubDebug 1 
    #traceIocInit 
    cd "/Users/maradona/EPICS/TEST/testIoc/iocBoot/ioctestIoc" 
    iocInit 
    Starting iocInit 
    ############################################################################ 
    ## EPICS R7.0.1.2-DEV 
    ## EPICS Base built Mar 8 2018 
    ############################################################################ 
    iocRun: All initialization complete 
    2018-03-09T13:07:02.475 Using dynamically assigned TCP port 52908. 
    ## Start any sequence programs 
    #seq sncExample, "user=maradona"
    epics> dbl
    maradona:circle:tick
    maradona:compressExample
    maradona:line:b
    maradona:aiExample
    maradona:aiExample1
    maradona:ai1
    maradona:aiExample2
    ... etc. ...
    epics>

Now in another terminal, one can try command line tools like

::

    caget, caput, camonitor, cainfo (Channel Access)
    pvget, pvput, pvlist, eget, ... (PVAccess)

Add the asyn package
--------------------
::

    cd $HOME/EPICS
    mkdir support
    cd support
    git clone https://github.com/epics-modules/asyn.git
    cd asyn

Edit ``$HOME/EPICS/support/asyn/configure/RELEASE`` and set
``EPICS_BASE`` like

::

    EPICS_BASE=${HOME}/EPICS/epics-base

Comment ``IPAC=...`` and ``SNCSEQ=...``, as they are not
needed for the moment. The whole file should read:

::

    #RELEASE Location of external products
    HOME=/Users/maradona
    SUPPORT=$(HOME)/EPICS/support
    -include $(TOP)/../configure/SUPPORT.$(EPICS_HOST_ARCH)
    # IPAC is only necessary if support for Greensprings IP488 is required
    # IPAC release V2-7 or later is required.
    #IPAC=$(SUPPORT)/ipac-2-14
    # SEQ is required for testIPServer
    #SNCSEQ=$(SUPPORT)/seq-2-2-5
    # EPICS_BASE 3.14.6 or later is required
    EPICS_BASE=$(HOME)/EPICS/epics-base
    -include $(TOP)/../configure/EPICS_BASE.$(EPICS_HOST_ARCH)

Now, run
::

    make

Install StreamDevice (by Dirk Zimoch, PSI)
------------------------------------------

StreamDevice does not come with its own top location and
``top/configure`` directory. It expects to be put into an already
existing top directory structure. We can simply create one with
``makeBaseApp.pl``

::

    cd $HOME/EPICS/support
    mkdir stream
    cd stream/
    makeBaseApp.pl -t support
    git clone https://github.com/paulscherrerinstitute/StreamDevice.git
    cd StreamDevice/
    rm GNUmakefile

Now we must edit the
``$HOME/EPICS/support/stream/configure/RELEASE``. The not-commented
lines must read

::

    # Variables and paths to dependent modules:
    MODULES = ${HOME}/EPICS/support
    # If using the sequencer, point SNCSEQ at its top directory:
    #SNCSEQ = $(MODULES)/seq-ver
    # EPICS_BASE should appear last so earlier modules can override stuff:
    EPICS_BASE = ${HOME}/EPICS/epics-base
    # These lines allow developers to override these RELEASE settings
    # without having to modify this file directly.
    -include $(TOP)/../RELEASE.local
    #-include $(TOP)/../RELEASE.$(EPICS_HOST_ARCH).local
    -include $(TOP)/configure/RELEASE.local
    ASYN=$(MODULES)/asyn

Remember that ``$(NAME)`` works if it is defined within the same
file, but ``${NAME}`` with curly brackets must be used if a shell
variable is meant. It is possible that the compiler does not like some of the
substitutions. In that case, replace the ``${NAME}`` variables with
full paths, like ``/Users/maradona/EPICS...``.

Finally run ``make`` (we are in the directory ``...EPICS/support/stream/StreamDevice``)
