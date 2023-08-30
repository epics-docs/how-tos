Getting EPICS 7 on RTEMS 5 (beatnik VMEbus board)
=================================================

Installation RTEMS and EPICS 7 incl. rtems tools, kernel, bsp and libext

ubuntu 20.04.1

packages needed

::

   apt install build-essential
   apt install bison flex
   apt install texi2html
   apt install texinfo
   apt install python3-dev

--------------

**Installing rtems source builder and build rtems-powerpc tools**

::

   mkdir MVME6100
   cd MVME6100
   git clone https://github.com/RTEMS/rtems-source-builder.git rsb
   cd rsb
   git checkout 5
   cd rtems
   cd rsb/rtems
   ../source-builder/sb-set-builder --prefix=$HOME/MVME6100/rtems/5 5/rtems-powerpc

Build Set: Time 0:31:20.847432

log-file:

::

   RTEMS Source Builder - Set Builder, 5 (803d42cda7b3)
   Command Line: ../source-builder/sb-set-builder --prefix=/home/junkes/MVME6100/rtems/5 5/rtems-powerpc
   Python: 2.7.18 (default, Aug  4 2020, 11:16:42) [GCC 9.3.0]
   Build Set: 5/rtems-powerpc
   Build Set: 5/rtems-autotools.bset
   Build Set: 5/rtems-autotools-internal.bset
   config: tools/rtems-autoconf-2.69-1.cfg
   package: autoconf-2.69-x86_64-linux-gnu-1
   script:  1: #!/bin/sh
   script:  2: # ___build_pre as set up in defaults.py
   script:  3: # Save the original path away.
   script:  4: export SB_ORIG_PATH=${PATH}
   script:  5: # Directories
   script:  6: SB_PREFIX="/home/junkes/MVME6100/rtems/5"
   script:  7: SB_PREFIX_CLEAN=$(echo "/home/junkes/MVME6100/rtems/5" | /bin/sed -e 's/^\///')
   script:  8: SB_SOURCE_DIR="/home/junkes/MVME6100/rsb/rtems/sources"
   script:  9: SB_BUILD_DIR="/home/junkes/MVME6100/rsb/rtems/build/autoconf-2.69-x86_64-linux-gnu-1"
   script: 10: # host == build, use build; host != build, host uses host and build uses build
   script: 11: SB_HOST_CPPFLAGS=""
   script: 12: # Optionally do not add includes to c/cxx flags as newer configure's complain
   script: 13: SB_HOST_CFLAGS="-O2 -g -pipe "
   script: 14: SB_HOST_CXXFLAGS="-O2 -g -pipe "
   script: 15: SB_HOST_LDFLAGS=" -L/home/junkes/MVME6100/rsb/rtems/build/tmp/sb-1000/5/rtems-autotools-internal/${SB_PREFIX_CLEAN}/lib"
   script: 16: SB_HOST_LIBS=""
   script: 17: SB_BUILD_CFLAGS="-O2 -g -pipe -I/home/junkes/MVME6100/rsb/rtems/build/tmp/sb-1000/5/rtems-autotools-internal/${SB_PREFIX_CLEAN}/i
   nclude"
   script: 18: SB_BUILD_CXXFLAGS="-O2 -g -pipe -I/home/junkes/MVME6100/rsb/rtems/build/tmp/sb-1000/5/rtems-autotools-internal/${SB_PREFIX_CLEAN}
   /include"
   script: 19: SB_BUILD_LDFLAGS=" -L/home/junkes/MVME6100/rsb/rtems/build/tmp/sb-1000/5/rtems-autotools-internal/${SB_PREFIX_CLEAN}/lib"
   script: 20: SB_BUILD_LBS=""
   script: 21: SB_CFLAGS="${SB_BUILD_CFLAGS} "

…

::

   cleaning: powerpc-rtems5-binutils-2.34-x86_64-linux-gnu-1
   removing: /home/junkes/MVME6100/rsb/rtems/build/tmp/powerpc-rtems5-binutils-2.34-x86_64-linux-gnu-1-1000
   removing: /home/junkes/MVME6100/rsb/rtems/build/powerpc-rtems5-binutils-2.34-x86_64-linux-gnu-1
   removing: /home/junkes/MVME6100/rsb/rtems/build/tmp/sb-1000/5/rtems-powerpc
   cleaning: powerpc-rtems5-gcc-7.5.0-newlib-7947581-x86_64-linux-gnu-1
   removing: /home/junkes/MVME6100/rsb/rtems/build/tmp/powerpc-rtems5-gcc-7.5.0-newlib-7947581-x86_64-linux-gnu-1-1000
   removing: /home/junkes/MVME6100/rsb/rtems/build/powerpc-rtems5-gcc-7.5.0-newlib-7947581-x86_64-linux-gnu-1
   removing: /home/junkes/MVME6100/rsb/rtems/build/tmp/sb-1000/5/rtems-powerpc
   cleaning: rtems-tools-4f5485eb51ffd7e091d92e3f95b720a9238c75fb-1
   removing: /home/junkes/MVME6100/rsb/rtems/build/tmp/rtems-tools-4f5485eb51ffd7e091d92e3f95b720a9238c75fb-1-1000
   removing: /home/junkes/MVME6100/rsb/rtems/build/rtems-tools-4f5485eb51ffd7e091d92e3f95b720a9238c75fb-1
   removing: /home/junkes/MVME6100/rsb/rtems/build/tmp/sb-1000/5/rtems-powerpc
   Build Sizes: usage: 7.966GB total: 1.842GB (sources: 144.476MB, patches: 20.103KB, installed 1.701GB)
   installing: 5/rtems-powerpc -> /home/junkes/MVME6100/rtems/5
   copy: /home/junkes/MVME6100/rsb/rtems/build/tmp/sb-1000-staging => /home/junkes/MVME6100/rtems/5
   clean staging: 5/rtems-powerpc
   Staging Size: 5.291MB
   Build Set: Time 0:31:20.847432

Add to $HOME/.bashrc:

::

   #RTEMS development
   export RTEMS_VERSION=5
   export RTEMS_ARCH=powerpc-rtems${RTEMS_VERSION}
   export RTEMS_BSP=beatnik
   export RTEMS_ROOT=${HOME}/MVME6100/rtems/${RTEMS_VERSION}
   export PATH=${RTEMS_ROOT}/bin:${PATH}
   export RTEMS_MAKEFILE_PATH=${RTEMS_ROOT}/${RTEMS_ARCH}/${RTEMS_BSP}
   export RTEMS_SHARE_PATH=${RTEMS_ROOT}/share/rtems${RTEMS_VERSION}

**Installing rtems kernel and bootstrap**

::

   cd; cd MVME6100
   git clone https://github.com/RTEMS/rtems.git kernel
   cd kernel;
   git checkout 5
   ./bootstrap -c && $HOME/MVME6100/rsb/source-builder/sb-bootstrap

output:

::

   removing automake generated Makefile.in files
   removing configure files
   removing aclocal.m4 files
   RTEMS Source Builder - RTEMS Bootstrap, 5 (803d42cda7b3)
     1/121: autoreconf: configure.ac
     2/121: autoreconf: testsuites/configure.ac
     3/121: autoreconf: testsuites/smptests/configure.ac
     4/121: autoreconf: testsuites/fstests/configure.ac
     5/121: autoreconf: testsuites/ada/configure.ac
     6/121: autoreconf: testsuites/benchmarks/configure.ac
     7/121: autoreconf: testsuites/libtests/configure.ac
   ...
   115/121: autoreconf: c/src/lib/libbsp/powerpc/mpc55xxevb/configure.ac
   116/121: autoreconf: c/src/lib/libbsp/powerpc/qoriq/configure.ac
   117/121: autoreconf: c/src/lib/libbsp/powerpc/gen5200/configure.ac
   118/121: autoreconf: c/src/lib/libbsp/powerpc/qemuppc/configure.ac
   119/121: autoreconf: c/src/lib/libbsp/powerpc/virtex/configure.ac
   120/121: autoreconf: c/src/lib/libbsp/powerpc/virtex4/configure.ac
   121/121: autoreconf: cpukit/configure.ac
   Bootstrap time: 0:00:29.161139

pax needed for make target

::

   sudo apt install pax

   cd; cd MVME6100
   mkdir -p build/b-beatnik
   cd build/b-beatnik
   ../../kernel/configure --prefix=$HOME/MVME6100/rtems/5 --target=powerpc-rtems5 --enable-rtemsbsp=beatnik --enable-posix --enable-c++ --enable-networking --enable-tests

config.log:

::

   This file contains any messages produced by compilers while
   running configure, to aid debugging if configure makes a mistake.

   It was created by rtems configure 5.0.0, which was
   generated by GNU Autoconf 2.69.  Invocation command line was

     $ ../../kernel/configure --prefix=/home/junkes/MVME6100/rtems/5 --target=powerpc-rtems5 --enable-rtemsbsp=beatnik --enable-posix --enab
   le-c++ --enable-networking --enable-tests

   ## --------- ##
   ## Platform. ##
   ## --------- ##

   hostname = Krikkit
   uname -m = x86_64
   uname -r = 5.8.0-34-generic
   uname -s = Linux
   uname -v = #37~20.04.2-Ubuntu SMP Thu Dec 17 14:53:00 UTC 2020

   /usr/bin/uname -p = x86_64
   /bin/uname -X     = unknown

   /bin/arch              = x86_64
   ...
   target_SUBDIRS=' powerpc-rtems5/c'
   target_alias='powerpc-rtems5'
   target_configdirs=' c'
   target_cpu='powerpc'
   target_os='rtems5'
   target_subdir='powerpc-rtems5'
   target_vendor='unknown'
   targetargs=''\''--host=powerpc-rtems5'\'' '\''--build=x86_64-pc-linux-gnu'\'' '\''--target=powerpc-rtems5'\''  '\''--enable-rtemsbsp=beat
   nik'\'' '\''--enable-posix'\'' '\''--enable-c++'\'' '\''--enable-networking'\'' '\''--enable-tests'\'''
   arget_SUBDIRS=' powerpc-rtems5/c'
   target_alias='powerpc-rtems5'
   target_configdirs=' c'
   target_cpu='powerpc'
   target_os='rtems5'
   target_subdir='powerpc-rtems5'
   target_vendor='unknown'
   targetargs=''\''--host=powerpc-rtems5'\'' '\''--build=x86_64-pc-linux-gnu'\'' '\''--target=powerpc-rtems5'\''  '\''--enable-rtemsbsp=beat
   nik'\'' '\''--enable-posix'\'' '\''--enable-c++'\'' '\''--enable-networking'\'' '\''--enable-tests'\'''

   ## ----------- ##
   ## confdefs.h. ##
   ## ----------- ##

   /* confdefs.h */
   #define PACKAGE_NAME "rtems"
   #define PACKAGE_TARNAME "rtems"
   #define PACKAGE_VERSION "5.0.0"
   #define PACKAGE_STRING "rtems 5.0.0"
   #define PACKAGE_BUGREPORT "https://devel.rtems.org/newticket"
   #define PACKAGE_URL ""
   target_SUBDIRS=' powerpc-rtems5/c'
   target_alias='powerpc-rtems5'
   target_configdirs=' c'
   target_cpu='powerpc'
   target_os='rtems5'
   target_subdir='powerpc-rtems5'
   target_vendor='unknown'
   targetargs=''\''--host=powerpc-rtems5'\'' '\''--build=x86_64-pc-linux-gnu'\'' '\''--target=powerpc-rtems5'\''  '\''--enable-rtemsbsp=beat
   nik'\'' '\''--enable-posix'\'' '\''--enable-c++'\'' '\''--enable-networking'\'' '\''--enable-tests'\'''
   arget_SUBDIRS=' powerpc-rtems5/c'
   target_alias='powerpc-rtems5'
   target_configdirs=' c'
   target_cpu='powerpc'
   target_os='rtems5'
   target_subdir='powerpc-rtems5'
   target_vendor='unknown'
   targetargs=''\''--host=powerpc-rtems5'\'' '\''--build=x86_64-pc-linux-gnu'\'' '\''--target=powerpc-rtems5'\''  '\''--enable-rtemsbsp=beat
   nik'\'' '\''--enable-posix'\'' '\''--enable-c++'\'' '\''--enable-networking'\'' '\''--enable-tests'\'''

   ## ----------- ##
   ## confdefs.h. ##
   ## ----------- ##

   /* confdefs.h */
   #define PACKAGE_NAME "rtems"
   #define PACKAGE_TARNAME "rtems"
   #define PACKAGE_VERSION "5.0.0"
   #define PACKAGE_STRING "rtems 5.0.0"
   #define PACKAGE_BUGREPORT "https://devel.rtems.org/newticket"
   #define PACKAGE_URL ""

   configure: exit 0
       configure: exit 0

   ## ----------- ##
   ## confdefs.h. ##
   ## ----------- ##

   /* confdefs.h */
   #define PACKAGE_NAME "rtems"
   #define PACKAGE_TARNAME "rtems"
   #define PACKAGE_VERSION "5.0.0"
   #define PACKAGE_STRING "rtems 5.0.0"
   #define PACKAGE_BUGREPORT "https://devel.rtems.org/newticket"
   #define PACKAGE_URL ""

   configure: exit 0


   make -j4 all
   make install

get libbspext

::

   cd; cd MVME6100
   git clone https://github.com/hjunkes/rtems-libbspext.git
   make

output:

::

   test -d o-optimize || mkdir o-optimize
   powerpc-rtems5-gcc --pipe -B/home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/lib/ -specs bsp_specs -qrtems   -Wall  -O2 -g -ffunction-sections -fdata-sections  -Winline -I/home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/beatnik/lib/include    -mcpu=7400 -Dmpc7455       -c   -o o-optimize/bspExt.o bspExt.c
   powerpc-rtems5-gcc --pipe -B/home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/lib/ -specs bsp_specs -qrtems   -Wall  -O2 -g -ffunction-sections -fdata-sections  -Winline -I/home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/beatnik/lib/include    -mcpu=7400 -Dmpc7455       -c   -o o-optimize/isrWrap.o isrWrap.c
   powerpc-rtems5-gcc --pipe -B/home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/lib/ -specs bsp_specs -qrtems   -Wall  -O2 -g -ffunction-sections -fdata-sections  -Winline -I/home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/beatnik/lib/include    -mcpu=7400 -Dmpc7455       -c   -o o-optimize/memProbe.o memProbe.c
   memProbe.c: In function '_bspExtMemProbeInit':
   memProbe.c:207:6: warning: implicit declaration of function 'BSP_panic'; did you mean 'rtems_panic'? [-Wimplicit-function-declaration]
         BSP_panic(__FILE__" bad value for mcp_hid");
         ^~~~~~~~~
         rtems_panic
   powerpc-rtems5-gcc --pipe -B/home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/lib/ -specs bsp_specs -qrtems   -Wall  -O2 -g -ffunction-sections -fdata-sections  -Winline -I/home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/beatnik/lib/include    -mcpu=7400 -Dmpc7455       -c   -o o-optimize/dabrBpnt.o dabrBpnt.c
   dabrBpnt.c: In function 'bspExtInstallDataBreakpoint':
   dabrBpnt.c:139:2: warning: #warning "FIXME: add run-time check for CPU type" [-Wcpp]
    #warning "FIXME: add run-time check for CPU type"
     ^~~~~~~
   rm -f o-optimize/libbspExt.a
   powerpc-rtems5-ar ruv o-optimize/libbspExt.a o-optimize/bspExt.o o-optimize/isrWrap.o o-optimize/memProbe.o o-optimize/dabrBpnt.o  
   powerpc-rtems5-ar: `u' modifier ignored since `D' is the default (see `U')
   powerpc-rtems5-ar: creating o-optimize/libbspExt.a
   a - o-optimize/bspExt.o
   a - o-optimize/isrWrap.o
   a - o-optimize/memProbe.o
   a - o-optimize/dabrBpnt.o
   powerpc-rtems5-ranlib o-optimize/libbspExt.a


   make install

output:

::

   install -m 644 o-optimize/libbspExt.a         /home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/lib/
   install -m 644 bspExt.h /home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/lib/include//bsp/
   install -m 644 o-optimize/libbspExt.a         /home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/lib/
   install -m 644 bspExt.h /home/junkes/MVME6100/rtems/5/powerpc-rtems5/beatnik/lib/include//bsp/

--------------

**Installing EPICS 7**

::

   cd; cd MVME6100
   mkdir EPICS; cd EPICS
   git clone --recursive https://github.com/hjunkes/epics-base.git
   cd epics-base

Define target in configure/CONFIG_SITE

::

   CROSS_COMPILER_TARGET_ARCHS=RTEMS-beatnik

In configure/os/CONFIG_SITE.Common.RTEMS define where rtems is installed

::

   # FHI:
   RTEMS_VERSION = 5
   RTEMS_BASE = /home/junkes/MVME6100/rtems/$(RTEMS_VERSION)

   make -j4

Copy libcomTestHarness.boot to th tftp-server:

::

   cd bin/RTEMS-beatnik
   scp -v libComTestHarness.boot root@141.14.128.9:/srv/tftp/

Connect to the console MVME6100, and reset card:

boot> c

::

   Copyright(C)2008-2009,Emerson Network Power-Embedded Computing,Inc.
   All Rights Reserved
   Copyright Motorola Inc. 1999-2007, All Rights Reserved
   MOTLoad RTOS Version 2.0,  PAL Version 2.3 RM01
   Fri Jan 23 14:47:54 MST 2009

   MPU-Type             =MPC74x7
   MPU-Int Clock Speed  =1266MHz
   MPU-Ext Clock Speed  =133MHz
   MPU-Int Cache(L2) Enabled, 512KB, L2CR =C0000000
   MPU-Ext Cache(L3) Enabled, 2MB, 211MHz, L3CR =DC026300

   PCI bus instance 0   =64 bit, 133 Mhz, PCI-X
   PCI bus instance 1   =64 bit, PCI

   Reset/Boot Vector    =Flash1

   Local Memory Found   =20000000 (&536870912)
   User Download Buffer =006B7000:008B6FFF

   MVME6100> tftpGet -s141.14.128.9 -c141.14.128.12 -a04000000 -fticker.exe
   Network Loading from: /dev/enet0
   Loading File: ticker.exe
   Load Address: 04000000
   Download Buffer Size = User Defined

   Client IP Address      = 141.14.128.12
   Server IP Address      = 141.14.128.9
   Gateway IP Address     = 141.14.128.253
   Subnet IP Address Mask = 255.255.255.0

   Network File Load in Progress...

   Bytes Received =&2577060, Bytes Loaded =&2577060
   Bytes/Second   =&2577060, Elapsed Time =1 Second(s)
   MVME6100-----------------------------------------
   config addr is 0xf1000cf8
   config data is 0xf1000cfc
   Welcome to RTEMS rtems-5.0.0 (PowerPC/Generic (classic FPU)/beatnik)
   CPU: MPC7457
   Board Type: MVME6100-0163 (S/N E173D27)
   Bus Clock Freq:   133333333 Hz
   CPU Clock Freq:  1266666654 Hz
   Memory:           536870912 bytes
   -----------------------------------------
   Now BSP_mem_size = 0x1fe00000
   Configuration.work_space_size = 201ac30
   Page table setup finished; will activate it NOW...
   Going to start PCI buses scanning and initialization
   Number of PCI buses found is : 3
   MSR 0x2003032
   Exit from bspstart
   unable to find the universe in pci config space
   Tundra Tsi148 PCI-VME bridge detected at 0x81100000, IRQ 84
   Tsi148 Outbound Ports:
   Port  VME-Addr   Size       PCI-Adrs   Mode:
   0:    0x20000000 0x0e000000 0x90000000 A32, SUP, D32, SCT
   1:    0x00000000 0x00ff0000 0x9f000000 A24, SUP, D32, SCT
   2:    0x00000000 0x00010000 0x9fff0000 A16, SUP, D32, SCT
   7:    0x00000000 0x01000000 0x9e000000 CSR, SUP, D32, SCT
   Tsi148 Inbound Ports:
   Port  VME-Addr   Size       PCI-Adrs   Mode:
   0:    0x90000000 0x1fe00000 0x00000000 A32, PGM, DAT, SUP, USR, MBLT, BLT
   vmeTsi148 IRQ manager: looking for registers on VME...
   Trying to find CSR on VME...
   vmeTsi148 - IRQ manager using VME CSR to flush FIFO
   Registering /dev/console as minor 0 (==/dev/ttyS0)

    initConsole --- Info ---
   stdin: fileno: 0, ttyname: /dev/console
   stdout: fileno: 1, ttyname: /dev/console
   stderr: fileno: 2, ttyname: /dev/console
   time set to : 04/14/14 07:30:06.000001049 UTC
   Startup.
   epicsThreadSetPriority called by non epics thread

   ***** RTEMS Version: rtems-5.0.0 (PowerPC/Generic (classic FPU)/beatnik) *****

   ***** Initializing network (Legacy Stack)  *****
   Link detected; attaching mve1
   bootpc_init: using network interface 'mve1'
   bootpc hw address is ec:9e:cd:1a:12:3f
   My ip address is 141 .14 .128 .12
   Domain Name Server is 141 .14 .128 .1
   Hostname is gonzo
   Ignoring BOOTP/DHCP option code 28
   Time Server is 141 .14 .142 .121
   Domain name is rz-berlin.mpg.de
   Server name is 1001.1001@141.14.128.9:/Volumes/Epics
   Boot file is /export/epics/felsis3316/bin/RTEMS-beatnik/felsis3316.boot
   Command line is /Volumes/Epics/myExample/iocBoot/iocmyExample/st.cmd
   Subnet mask is 255 .255 .240 .0
   Server ip address is 141 .14 .128 .1
   Gateway ip address is 141 .14 .128 .128
   Log server ip address is 141 .14 .128 .1

   ***** Network Status  *****
   ************ INTERFACE STATISTICS ************
   ***** lo0 *****
   Address:127.0.0.1       Net mask:255.0.0.0
   Flags: Up Loopback Running Multicast
   Send queue limit:50   length:0    Dropped:0
   ***** mve1 *****
   Ethernet Address: EC:9E:CD:1A:12:3F
   Address:141.14.128.12   Broadcast Address:141.14.143.255  Net mask:255.255.240.0
   Flags: Up Broadcast Running Simplex Multicast
   Send queue limit:50   length:0    Dropped:0
   mve1 Statistics:
     # IRQS:                 10
     Max. mbuf chain length: 1
     # repacketed:           0
     # packets:              1
   MIB Counters:
     GOOD_OCTS_RCVD:      11386
     BAD_OCTS_RCVD:       0
     INTERNAL_MAC_TX_ERR: 0
     GOOD_FRAMES_RCVD:    43
     BAD_FRAMES_RCVD:     0
     BCAST_FRAMES_RCVD:   18
     MCAST_FRAMES_RCVD:   31
     FRAMES_64_OCTS:      10
     FRAMES_65_127_OCTS:  20
     FRAMES_128_255_OCTS: 3
     FRAMES_256_511_OCTS: 9
     FRAMES_512_1023_OCTS:8
     FRAMES_1024_MAX_OCTS:0
     GOOD_OCTS_SENT:      64
     GOOD_FRAMES_SENT:    1
     EXCESSIVE_COLL:      0
     MCAST_FRAMES_SENT:   0
     BCAST_FRAMES_SENT:   1
     UNREC_MAC_CTRL_RCVD: 0
     FC_SENT:             0
     GOOD_FC_RCVD:        0
     BAD_FC_RCVD:         0
     UNDERSIZE_RCVD:      0
     FRAGMENTS_RCVD:      0
     OVERSIZE_RCVD:       0
     JABBER_RCVD:         0
     MAC_RX_ERR:          0
     BAD_CRC_EVENT:       0
     COLL:                0
     LATE_COLL:           0


   ************ MBUF STATISTICS ************
   mbufs:16384    clusters:2560    free:2520
   drops:   0       waits:   0  drains:   0
         free:16343         data:41          header:0           socket:0
          pcb:0           rtable:0           htable:0           atable:0
       soname:0           soopts:0           ftable:0           rights:0
       ifaddr:0          control:0          oobdata:0

   Destination     Gateway/Mask/Hw    Flags     Refs     Use Expire Interface
   default         141.14.128.128     UGS         0        0      0 mve1
   127.0.0.1       127.0.0.1          UH          0        0      0 lo0
   141.14.128.0    255.255.240.0      U           0        0      7 mve1
   141.14.128.128  00:24:38:93:C8:00  UHL         1        0   1209 mve1
   ************ IP Statistics ************
                total packets received          39
     packets rcvd for unreachable dest           1
    datagrams delivered to upper level          38
       total ip packets generated here           3

   ************ ICMP Statistics ************

   ************ UDP Statistics ************
                   total input packets          40
                     no socket on port           4
        of above, arrived as broadcast          42
                  total output packets           3

   ************ TCP Statistics ************


   ***** Setting up file system *****
   ***** Using compiled in file data *****
   -> /iocshTestBadArgIndirect.cmd - ok
   -> /iocshTestBadArg.cmd - ok
   -> /iocshTestSuccessIndirect.cmd - ok
   -> /iocshTestSuccess.cmd - ok
   ***** Initializing NFS *****
    check for time registered , C++ initialization ...
    Will try to start telnetd with prio 99 ...
   syslog: telnetd: started successfully on port 23
    telnetd initialized with result 0
   ***** Preparing EPICS application *****
   chdir("/")
   ***** Starting EPICS application *****
   Backwards time errors prevented 0 times.

   Current Time Providers:
       "OS Clock", priority = 999
           Current Time is 2021-01-07 16:36:08.056273.

   Event Time Providers:
           No Providers registered.

   ***** epicsThreadTest *****
   1..15
   # System has 1 CPUs
   ok  1 - ncpus > 0
   # main() thread 0x2d47e0
   ok  2 - Join delayed parent (2.00998 seconds)
   ok  3 - Join tests #1 completed
   ok  4 - Join delayed parent (2.00998 seconds)
   ok  5 - Join tests #2 completed
   ok  6 - pget == pset
   ok  7 - thread.getPriority() == epicsThreadGetPriority(self)
   ok  8 - pget == pset
   ok  9 - pget == pset
   ok 10 - thread.getPriority() == epicsThreadGetPriority(self)
   ok 11 - thread.getPriority() == epicsThreadGetPriority(self)
   ok 12 - threadA epicsThreadIsOkToBlock() = 0
   ok 13 - threadB epicsThreadIsOkToBlock() = 1
   ok 14 - infoB.didSomething
   ok 15 - infoA.didSomething

       Results
       =======
          Tests: 15
         Passed:  15 = 100.00%

   ***** epicsTimerTest *****
   1..41
   ok  1 - Q1==Q2
   # Testing timer accuracy
   ok  2 - timerCount == nTimers
   ok  3 - 0.195030 < 5.000000, delay = 1.000000 s, error = 0.001950 s (0.2 %)
   ok  4 - 0.175824 < 5.000000, delay = 1.100000 s, error = 0.001934 s (0.2 %)
   ok  5 - 0.160963 < 5.000000, delay = 1.200000 s, error = 0.001932 s (0.2 %)
   ok  6 - 0.148447 < 5.000000, delay = 1.300000 s, error = 0.001930 s (0.1 %)
   ok  7 - 0.137721 < 5.000000, delay = 1.400000 s, error = 0.001928 s (0.1 %)
   ok  8 - 0.128465 < 5.000000, delay = 1.500000 s, error = 0.001927 s (0.1 %)
   ok  9 - 0.120293 < 5.000000, delay = 1.600000 s, error = 0.001925 s (0.1 %)
   ok 10 - 0.113110 < 5.000000, delay = 1.700000 s, error = 0.001923 s (0.1 %)
   ok 11 - 0.106733 < 5.000000, delay = 1.800000 s, error = 0.001921 s (0.1 %)
   ok 12 - 0.101023 < 5.000000, delay = 1.900000 s, error = 0.001919 s (0.1 %)
   ok 13 - 0.095891 < 5.000000, delay = 2.000000 s, error = 0.001918 s (0.1 %)
   ok 14 - 0.091242 < 5.000000, delay = 2.100000 s, error = 0.001916 s (0.1 %)
   ok 15 - 0.087020 < 5.000000, delay = 2.200000 s, error = 0.001914 s (0.1 %)
   ok 16 - 0.083164 < 5.000000, delay = 2.300000 s, error = 0.001913 s (0.1 %)
   ok 17 - 0.079623 < 5.000000, delay = 2.400000 s, error = 0.001911 s (0.1 %)
   ok 18 - 0.076381 < 5.000000, delay = 2.500000 s, error = 0.001910 s (0.1 %)
   ok 19 - 0.073365 < 5.000000, delay = 2.600000 s, error = 0.001907 s (0.1 %)
   ok 20 - 0.070582 < 5.000000, delay = 2.700000 s, error = 0.001906 s (0.1 %)
   ok 21 - 0.068000 < 5.000000, delay = 2.800000 s, error = 0.001904 s (0.1 %)
   ok 22 - 0.065594 < 5.000000, delay = 2.900000 s, error = 0.001902 s (0.1 %)
   ok 23 - 0.063354 < 5.000000, delay = 3.000000 s, error = 0.001901 s (0.1 %)
   ok 24 - 0.061257 < 5.000000, delay = 3.100000 s, error = 0.001899 s (0.1 %)
   ok 25 - 0.059292 < 5.000000, delay = 3.200000 s, error = 0.001897 s (0.1 %)
   ok 26 - 0.057446 < 5.000000, delay = 3.300000 s, error = 0.001896 s (0.1 %)
   ok 27 - 0.055704 < 5.000000, delay = 3.400000 s, error = 0.001894 s (0.1 %)
   # average timer delay error 1.915062 ms
   # Testing timer cancellation
   ok 28 - timerCount == nTimers
   ok 29 - cancelVerify::expireCount == 0
   ok 30 - cancelVerify::cancelCount == 0
   # starting 25 timers
   ok 31 - cancelVerify::expireCount == 0
   ok 32 - cancelVerify::cancelCount == 0
   # cancelling timers
   ok 33 - cancelVerify::expireCount == 0
   ok 34 - cancelVerify::cancelCount == nTimers
   # waiting until after timers should have expired
   ok 35 - cancelVerify::expireCount == 0
   ok 36 - cancelVerify::cancelCount == nTimers
   # Testing timer destruction in expire()
   ok 37 - timerCount == nTimers
   ok 38 - expireDestroyVerify::destroyCount == 0
   # starting 25 timers
   # waiting until all timers should have expired
   ok 39 - expireDestroyVerify::destroyCount == nTimers
   # Testing periodic timers
   ok 40 - timerCount == nTimers
   # starting 25 timers
   # waiting until all timers should have expired
   ok 41 - All timers expiring

       Results
       =======
          Tests: 41
         Passed:  41 = 100.00%

   ***** aslibtest *****
   1..27
   # testSyntaxErrors()
   ok  1 - load "empty" config -> access security: bad configuration file
   # testHostNames()
   ok  2 - asInitMem(hostname_config, NULL)==0
   ok  3 - testAccess(ASG:invalid, USER:testing, HOST:localhost, ASL:0) -> 0 == 0
   ok  4 - testAccess(ASG:DEFAULT, USER:testing, HOST:localhost, ASL:0) -> 0 == 0
   ok  5 - testAccess(ASG:ro, USER:testing, HOST:localhost, ASL:0) -> 1 == 1
   ok  6 - testAccess(ASG:rw, USER:testing, HOST:localhost, ASL:0) -> 3 == 3
   ok  7 - testAccess(ASG:invalid, USER:testing, HOST:127.0.0.1, ASL:0) -> 0 == 0
   ok  8 - testAccess(ASG:DEFAULT, USER:testing, HOST:127.0.0.1, ASL:0) -> 0 == 0
   ok  9 - testAccess(ASG:ro, USER:testing, HOST:127.0.0.1, ASL:0) -> 0 == 0
   ok 10 - testAccess(ASG:rw, USER:testing, HOST:127.0.0.1, ASL:0) -> 0 == 0
   ok 11 - testAccess(ASG:invalid, USER:testing, HOST:guaranteed.invalid., ASL:0) -> 0 == 0
   ok 12 - testAccess(ASG:DEFAULT, USER:testing, HOST:guaranteed.invalid., ASL:0) -> 0 == 0
   ok 13 - testAccess(ASG:ro, USER:testing, HOST:guaranteed.invalid., ASL:0) -> 0 == 0
   ok 14 - testAccess(ASG:rw, USER:testing, HOST:guaranteed.invalid., ASL:0) -> 0 == 0
   # testUseIP()
   ok 15 - asInitMem(hostname_config, NULL)==0
   ok 16 - testAccess(ASG:invalid, USER:testing, HOST:localhost, ASL:0) -> 0 == 0
   ok 17 - testAccess(ASG:DEFAULT, USER:testing, HOST:localhost, ASL:0) -> 0 == 0
   ok 18 - testAccess(ASG:ro, USER:testing, HOST:localhost, ASL:0) -> 0 == 0
   ok 19 - testAccess(ASG:rw, USER:testing, HOST:localhost, ASL:0) -> 0 == 0
   ok 20 - testAccess(ASG:invalid, USER:testing, HOST:127.0.0.1, ASL:0) -> 0 == 0
   ok 21 - testAccess(ASG:DEFAULT, USER:testing, HOST:127.0.0.1, ASL:0) -> 0 == 0
   ok 22 - testAccess(ASG:ro, USER:testing, HOST:127.0.0.1, ASL:0) -> 1 == 1
   ok 23 - testAccess(ASG:rw, USER:testing, HOST:127.0.0.1, ASL:0) -> 3 == 3
   ok 24 - testAccess(ASG:invalid, USER:testing, HOST:guaranteed.invalid., ASL:0) -> 0 == 0
   ok 25 - testAccess(ASG:DEFAULT, USER:testing, HOST:guaranteed.invalid., ASL:0) -> 0 == 0
   ok 26 - testAccess(ASG:ro, USER:testing, HOST:guaranteed.invalid., ASL:0) -> 0 == 0
   ok 27 - testAccess(ASG:rw, USER:testing, HOST:guaranteed.invalid., ASL:0) -> 0 == 0

       Results
       =======
          Tests: 27
         Passed:  27 = 100.00%

   ***** blockingSockTest *****
   1..13
   ok  1 - Server socket valid
   ok  2 - Server socket listening
   ok  3 - Server thread created
   ok  4 - Socket valid
   ok  5 - Accepted socket valid
   ok  6 - Client end connected
   ok  7 - Socket valid
   ok  8 - Client thread created
   ok  9 - Server circuit thread created
   ok 10 - Server circuit created
   ok 11 - Client is asleep
   # Trying Shutdown mechanism
   # client circuit was disconnected
   # server circuit was disconnected
   ok 12 - Shutdown() returned Ok
   # Shutdown succeeded
   # This OS behaves like "esscimqi_socketBothShutdownRequired".
   ok 13 - Declared mechanism works

       Results
       =======
          Tests: 13
         Passed:  13 = 100.00%

   ***** epicsAlgorithm *****
   1..22
   ok  1 - epicsMin(f1, f2)
   ok  2 - epicsMin(f1, -Inf)
   ok  3 - epicsMin(f1, NaN)
   ok  4 - epicsMin(f1, Inf)
   ok  5 - epicsMin(f2, f1)
   ok  6 - epicsMin(-Inf, f1)
   ok  7 - epicsMin(NaN, f1)
   ok  8 - epicsMin(Inf, f1)
   ok  9 - epicsMax(f2, f1)
   ok 10 - epicsMax(-Inf, f1)
   ok 11 - epicsMax(NaN, f1)
   ok 12 - epicsMax(Inf, f1)
   ok 13 - epicsMax(f1, f2)
   ok 14 - epicsMax(f1, -Inf)
   ok 15 - epicsMax(f1, NaN)
   ok 16 - epicsMax(f1, Inf)
   ok 17 - epicsSwap(f1, f2)
   ok 18 - epicsMin(i1,i2)
   ok 19 - epicsMin(i2,i1)
   ok 20 - epicsMax(i1,i2)
   ok 21 - epicsMax(i2,i1)
   ok 22 - epicsSwap(i1, i2)

       Results
       =======
          Tests: 22
         Passed:  22 = 100.00%

   ***** epicsAtomicTest *****
   1..50
   # In int epicsAtomicTest()
   # Classify Build conditions
   # Compiler dependent impl name GCC
   # OS dependent impl name POSIX
   # GCC using atomic builtin memory barrier
   # GCC use builtin for int
   # GCC use builtin for size_t
   # Use default epicsAtomicSetIntT()
   # Use default epicsAtomicSetSizeT()
   # Use default epicsAtomicSetPtrT()
   # Use default epicsAtomicGetIntT()
   # Use default epicsAtomicGetSizeT()
   # Use default epicsAtomicGetPtrT()
   # Test basic operation symantics
   ok  1 - get(Int)==-41
   ok  2 - get(Sizet)==43
   ok  3 - get(voidp)==(void*)&voidp
   ok  4 - get(Int)==-42
   ok  5 - get(Sizet)==42
   ok  6 - get(Int)==-44
   ok  7 - get(Sizet)==40
   ok  8 - compareAndSwap(Int, -34, -10)==-44
   ok  9 - compareAndSwap(Sizet, 34, 10)==40
   ok 10 - compareAndSwap(voidp, NULL, (void*)&Sizet)==(void*)&voidp
   ok 11 - get(Int)==-44
   ok 12 - get(Sizet)==40
   ok 13 - get(voidp)==(void*)&voidp
   ok 14 - compareAndSwap(Int, -44, -10)==-44
   ok 15 - compareAndSwap(Sizet, 40, 10)==40
   ok 16 - compareAndSwap(voidp, (void*)&voidp, (void*)&Sizet)==(void*)&voidp
   ok 17 - get(Int)==-10
   ok 18 - get(Sizet)==10
   ok 19 - get(voidp)==(void*)&Sizet
   ok 20 # SKIP Tests assume time sliced thread scheduling
   ok 21 # SKIP Tests assume time sliced thread scheduling
   ok 22 # SKIP Tests assume time sliced thread scheduling
   ok 23 # SKIP Tests assume time sliced thread scheduling
   ok 24 # SKIP Tests assume time sliced thread scheduling
   ok 25 # SKIP Tests assume time sliced thread scheduling
   ok 26 # SKIP Tests assume time sliced thread scheduling
   ok 27 # SKIP Tests assume time sliced thread scheduling
   ok 28 # SKIP Tests assume time sliced thread scheduling
   ok 29 # SKIP Tests assume time sliced thread scheduling
   ok 30 # SKIP Tests assume time sliced thread scheduling
   ok 31 # SKIP Tests assume time sliced thread scheduling
   ok 32 # SKIP Tests assume time sliced thread scheduling
   ok 33 # SKIP Tests assume time sliced thread scheduling
   ok 34 # SKIP Tests assume time sliced thread scheduling
   ok 35 # SKIP Tests assume time sliced thread scheduling
   ok 36 # SKIP Tests assume time sliced thread scheduling
   ok 37 # SKIP Tests assume time sliced thread scheduling
   ok 38 # SKIP Tests assume time sliced thread scheduling
   ok 39 # SKIP Tests assume time sliced thread scheduling
   ok 40 # SKIP Tests assume time sliced thread scheduling
   ok 41 # SKIP Tests assume time sliced thread scheduling
   ok 42 # SKIP Tests assume time sliced thread scheduling
   ok 43 # SKIP Tests assume time sliced thread scheduling
   ok 44 # SKIP Tests assume time sliced thread scheduling
   ok 45 # SKIP Tests assume time sliced thread scheduling
   ok 46 # SKIP Tests assume time sliced thread scheduling
   ok 47 # SKIP Tests assume time sliced thread scheduling
   ok 48 # SKIP Tests assume time sliced thread scheduling
   ok 49 # SKIP Tests assume time sliced thread scheduling
   ok 50 # SKIP Tests assume time sliced thread scheduling

       Results
       =======
          Tests: 50
         Passed:  50 = 100.00%
        Skipped:  31 = 62.00%

   ***** epicsCalcTest *****
   1..630
   ok  1 - 0
   ok  2 - 1
   ok  3 - 2
   ok  4 - 3
   ok  5 - 4
   ok  6 - 5
   ok  7 - 6
   ok  8 - 7
   ok  9 - 8
   ok 10 - 9
   ok 11 - .1
   ok 12 - 0.1
   ok 13 - 0X0
   ok 14 - 0x10
   ok 15 - 0x7fffffff
   ok 16 - 0x80000000
   ok 17 - 0xffffffff
   ok 18 - Inf
   ok 19 - Infinity
   ok 20 - NaN
   ok 21 - a
   ok 22 - b
   ok 23 - c
   ok 24 - d
   ok 25 - e
   ok 26 - f
   ok 27 - g
   ok 28 - h
   ok 29 - i
   ok 30 - j
   ok 31 - k
   ok 32 - l
   ok 33 - PI
   ok 34 - D2R
   ok 35 - R2D
   ok 36 - rndm
   ok 37 - -1
   ok 38 - -Inf
   ok 39 - - -1
   ok 40 - -0x80000000
   ok 41 - (1)
   ok 42 - !0
   ok 43 - !1
   ok 44 - !!0
   ok 45 - ABS(1.0)
   ok 46 - ABS(-1.)
   ok 47 - acos(1.)
   ok 48 - asin(0.5)
   ok 49 - atan(0.5)
   ok 50 - ATAN2(1., 2.)
   ok 51 - ceil(0.5)
   ok 52 - cos(0.5)
   ok 53 - cosh(0.5)
   ok 54 - exp(1.)
   ok 55 - floor(1.5)
   ok 56 - finite(0.)
   ok 57 - finite(Inf)
   ok 58 - finite(-Inf)
   ok 59 - finite(NaN)
   ok 60 - finite(0,1,2)
   ok 61 - finite(0,1,NaN)
   ok 62 - finite(0,NaN,2)
   ok 63 - finite(NaN,1,2)
   ok 64 - finite(0,1,Inf)
   ok 65 - finite(0,Inf,2)
   ok 66 - finite(Inf,1,2)
   ok 67 - finite(0,1,-Inf)
   ok 68 - finite(0,-Inf,2)
   ok 69 - finite(-Inf,1,2)
   ok 70 - isinf(0.)
   ok 71 - isinf(Inf)
   ok 72 - !!isinf(-Inf)
   ok 73 - isinf(NaN)
   ok 74 - isnan(0.)
   ok 75 - isnan(Inf)
   ok 76 - isnan(-Inf)
   ok 77 - !!isnan(NaN)
   ok 78 - isnan(0,1,2)
   ok 79 - isnan(0,1,NaN)
   ok 80 - isnan(0,NaN,2)
   ok 81 - isnan(NaN,1,2)
   ok 82 - isnan(0,1,Inf)
   ok 83 - isnan(0,Inf,2)
   ok 84 - isnan(Inf,1,2)
   ok 85 - isnan(0,1,-Inf)
   ok 86 - isnan(0,-Inf,2)
   ok 87 - isnan(-Inf,1,2)
   ok 88 - LN(5.)
   ok 89 - LOG(5.)
   ok 90 - LOGE(2.)
   ok 91 - MAX(-99)
   ok 92 - MAX( 1., 2.)
   ok 93 - MAX( 1., Inf)
   ok 94 - MAX( 1.,-Inf)
   ok 95 - MAX( 1., NaN)
   ok 96 - MAX( Inf, 1.)
   ok 97 - MAX(-Inf, 1.)
   ok 98 - MAX( NaN, 1.)
   ok 99 - MAX( 1., 2.,3.)
   ok 100 - MAX( 1., 3.,2.)
   ok 101 - MAX( 2., 1.,3.)
   ok 102 - MAX( 2., 3.,1.)
   ok 103 - MAX( 3., 1.,2.)
   ok 104 - MAX( 3., 2.,1.)
   ok 105 - MAX( 1., 2., Inf)
   ok 106 - MAX( 1., 2.,-Inf)
   ok 107 - MAX( 1., 2., NaN)
   ok 108 - MAX( 1., Inf,2.)
   ok 109 - MAX( 1.,-Inf,2.)
   ok 110 - MAX( 1., NaN,2.)
   ok 111 - MAX( Inf, 1.,2.)
   ok 112 - MAX(-Inf, 1.,2.)
   ok 113 - MAX( NaN, 1.,2.)
   ok 114 - MAX( 1., 2., 3., 4.)
   ok 115 - MAX( 1., 2., 4., 3.)
   ok 116 - MAX( 1., 4., 3., 2.)
   ok 117 - MAX( 4., 2., 3., 1.)
   ok 118 - MAX( 1., 2., 3.,NaN)
   ok 119 - MAX( 1., 2.,NaN, 3.)
   ok 120 - MAX( 1.,NaN, 3., 2.)
   ok 121 - MAX(NaN, 2., 3., 1.)
   ok 122 - MAX( 1., 2., 3., 4., 5.)
   ok 123 - MAX( 1., 2., 3., 5., 4.)
   ok 124 - MAX( 1., 2., 5., 4., 3.)
   ok 125 - MAX( 1., 5., 3., 4., 2.)
   ok 126 - MAX( 5., 2., 3., 4., 1.)
   ok 127 - MAX( 1., 2., 3., 4.,NaN)
   ok 128 - MAX( 1., 2., 3.,NaN, 4.)
   ok 129 - MAX( 1., 2.,NaN, 4., 3.)
   ok 130 - MAX( 1.,NaN, 3., 4., 2.)
   ok 131 - MAX(NaN, 2., 3., 4., 1.)
   ok 132 - MAX( 1., 2., 3., 4., 5., 6.)
   ok 133 - MAX( 1., 2., 3., 4., 6., 5.)
   ok 134 - MAX( 1., 2., 3., 6., 5., 4.)
   ok 135 - MAX( 1., 2., 6., 4., 5., 3.)
   ok 136 - MAX( 1., 6., 3., 4., 5., 2.)
   ok 137 - MAX( 6., 2., 3., 4., 5., 1.)
   ok 138 - MAX( 1., 2., 3., 4., 5.,NaN)
   ok 139 - MAX( 1., 2., 3., 4.,NaN, 5.)
   ok 140 - MAX( 1., 2., 3.,NaN, 5., 4.)
   ok 141 - MAX( 1., 2.,NaN, 4., 5., 3.)
   ok 142 - MAX( 1.,NaN, 3., 4., 5., 2.)
   ok 143 - MAX(NaN, 2., 3., 4., 5., 1.)
   ok 144 - MAX( 1., 2., 3., 4., 5.,Inf)
   ok 145 - MAX( 1., 2., 3., 4.,Inf, 5.)
   ok 146 - MAX( 1., 2., 3.,Inf, 5., 4.)
   ok 147 - MAX( 1., 2.,Inf, 4., 5., 3.)
   ok 148 - MAX( 1.,Inf, 3., 4., 5., 2.)
   ok 149 - MAX(Inf, 2., 3., 4., 5., 1.)
   ok 150 - MAX(1,2,3,4,5,6,7,8,9,10,11,12)
   ok 151 - MAX(5,4,3,2,1,0,-1,-2,-3,-4,-5,-6)
   ok 152 - MAX(-1,1,0)
   ok 153 - MIN(99)
   ok 154 - MIN(1.,2.)
   ok 155 - MIN(1.,Inf)
   ok 156 - MIN(1.,-Inf)
   ok 157 - MIN(1.,NaN)
   ok 158 - MIN(NaN,1.)
   ok 159 - MIN( 1., 2.,3.)
   ok 160 - MIN( 1., 3.,2.)
   ok 161 - MIN( 2., 1.,3.)
   ok 162 - MIN( 2., 3.,1.)
   ok 163 - MIN( 3., 1.,2.)
   ok 164 - MIN( 3., 2.,1.)
   ok 165 - MIN( 1., 2., Inf)
   ok 166 - MIN( 1., 2.,-Inf)
   ok 167 - MIN( 1., 2., NaN)
   ok 168 - MIN( 1., Inf,2.)
   ok 169 - MIN( 1.,-Inf,2.)
   ok 170 - MIN( 1., NaN,2.)
   ok 171 - MIN( Inf, 1.,2.)
   ok 172 - MIN(-Inf, 1.,2.)
   ok 173 - MIN( NaN, 1.,2.)
   ok 174 - MIN( 1., 2., 3., 4.)
   ok 175 - MIN( 1., 2., 4., 3.)
   ok 176 - MIN( 1., 4., 3., 2.)
   ok 177 - MIN( 4., 2., 3., 1.)
   ok 178 - MIN( 1., 2., 3.,NaN)
   ok 179 - MIN( 1., 2.,NaN, 3.)
   ok 180 - MIN( 1.,NaN, 3., 2.)
   ok 181 - MIN(NaN, 2., 3., 1.)
   ok 182 - MIN( 1., 2., 3., 4., 5.)
   ok 183 - MIN( 1., 2., 3., 5., 4.)
   ok 184 - MIN( 1., 2., 5., 4., 3.)
   ok 185 - MIN( 1., 5., 3., 4., 2.)
   ok 186 - MIN( 5., 2., 3., 4., 1.)
   ok 187 - MIN( 1., 2., 3., 4.,NaN)
   ok 188 - MIN( 1., 2., 3.,NaN, 4.)
   ok 189 - MIN( 1., 2.,NaN, 4., 3.)
   ok 190 - MIN( 1.,NaN, 3., 4., 2.)
   ok 191 - MIN(NaN, 2., 3., 4., 1.)
   ok 192 - MIN( 1., 2., 3., 4., 5., 6.)
   ok 193 - MIN( 2., 1., 3., 4., 5., 6.)
   ok 194 - MIN( 3., 2., 1., 4., 5., 6.)
   ok 195 - MIN( 4., 2., 3., 1., 5., 6.)
   ok 196 - MIN( 5., 2., 3., 4., 1., 6.)
   ok 197 - MIN( 6., 2., 3., 4., 5., 1.)
   ok 198 - MIN( 1., 2., 3., 4., 5.,NaN)
   ok 199 - MIN( 1., 2., 3., 4.,NaN, 5.)
   ok 200 - MIN( 1., 2., 3.,NaN, 5., 4.)
   ok 201 - MIN( 1., 2.,NaN, 4., 5., 3.)
   ok 202 - MIN( 1.,NaN, 3., 4., 5., 2.)
   ok 203 - MIN(NaN, 2., 3., 4., 5., 1.)
   ok 204 - MIN( 1., 2., 3., 4., 5.,-Inf)
   ok 205 - MIN( 1., 2., 3., 4.,-Inf, 5.)
   ok 206 - MIN( 1., 2., 3.,-Inf, 5., 4.)
   ok 207 - MIN( 1., 2.,-Inf, 4., 5., 3.)
   ok 208 - MIN( 1.,-Inf, 3., 4., 5., 2.)
   ok 209 - MIN(-Inf, 2., 3., 4., 5., 1.)
   ok 210 - MIN(1,2,3,4,5,6,7,8,9,10,11,12)
   ok 211 - MIN(5,4,3,2,1,0,-1,-2,-3,-4,-5,-6)
   ok 212 - MIN(1,-1,0)
   ok 213 - MAX(MIN(0,2),MAX(0),MIN(3,2,1))
   ok 214 - NINT(0.4)
   ok 215 - NINT(0.6)
   ok 216 - NINT(-0.4)
   ok 217 - NINT(-0.6)
   ok 218 - sin(0.5)
   ok 219 - sinh(0.5)
   ok 220 - SQR(10.)
   ok 221 - sqrt(16.)
   ok 222 - tan(0.5)
   ok 223 - tanh(0.5)
   ok 224 - ~5
   ok 225 - ~~5
   ok 226 - 0 != 1
   ok 227 - 0 != 0
   ok 228 - 1 != 0
   ok 229 - 1 != 0 != 2
   ok 230 - 0.0 != Inf
   ok 231 - 0.0 != -Inf
   ok 232 - 0.0 != NaN
   ok 233 - Inf != 0.0
   ok 234 - Inf != Inf
   ok 235 - Inf != -Inf
   ok 236 - Inf != NaN
   ok 237 - -Inf != 0.0
   ok 238 - -Inf != Inf
   ok 239 - -Inf != -Inf
   ok 240 - -Inf != NaN
   ok 241 - NaN != 0.0
   ok 242 - NaN != Inf
   ok 243 - NaN != -Inf
   ok 244 - NaN != NaN
   ok 245 - 0 # 1
   ok 246 - 0 # 0
   ok 247 - 1 # 0
   ok 248 - 1 # 0 # 2
   ok 249 - 7 % 4
   ok 250 - -7 % 4
   ok 251 - 63 % 16 % 6
   ok 252 - 1 % 0
   ok 253 - 7 & 4
   ok 254 - 0 && 0
   ok 255 - 0 && 1
   ok 256 - 1 && 0
   ok 257 - 1 && 1
   ok 258 - 2 * 2
   ok 259 - 0.0 * Inf
   ok 260 - 0.0 * -Inf
   ok 261 - 0.0 * NaN
   ok 262 - Inf * 0.0
   ok 263 - Inf * Inf
   ok 264 - Inf * -Inf
   ok 265 - Inf * NaN
   ok 266 - -Inf * 0.0
   ok 267 - -Inf * Inf
   ok 268 - -Inf * -Inf
   ok 269 - -Inf * NaN
   ok 270 - NaN * 0.0
   ok 271 - NaN * Inf
   ok 272 - NaN * -Inf
   ok 273 - NaN * NaN
   ok 274 - 2 ** 0.2
   ok 275 - 2 ** -0.2
   ok 276 - -0.2 ** 2
   ok 277 - -0.2 ** -2
   ok 278 - 2 ** 2 ** 3
   ok 279 - 0 + 1
   ok 280 - 0.0 + Inf
   ok 281 - 0.0 + -Inf
   ok 282 - 0.0 + NaN
   ok 283 - Inf + 0.0
   ok 284 - Inf + Inf
   ok 285 - Inf + -Inf
   ok 286 - Inf + NaN
   ok 287 - -Inf + 0.0
   ok 288 - -Inf + Inf
   ok 289 - -Inf + -Inf
   ok 290 - -Inf + NaN
   ok 291 - NaN + 0.0
   ok 292 - NaN + Inf
   ok 293 - NaN + -Inf
   ok 294 - NaN + NaN
   ok 295 - 0 - 1
   ok 296 - 0 - 1 - 2
   ok 297 - 0.0 - Inf
   ok 298 - 0.0 - -Inf
   ok 299 - 0.0 - NaN
   ok 300 - Inf - 0.0
   ok 301 - Inf - Inf
   ok 302 - Inf - -Inf
   ok 303 - Inf - NaN
   ok 304 - -Inf - 0.0
   ok 305 - -Inf - Inf
   ok 306 - -Inf - -Inf
   ok 307 - -Inf - NaN
   ok 308 - NaN - 0.0
   ok 309 - NaN - Inf
   ok 310 - NaN - -Inf
   ok 311 - NaN - NaN
   ok 312 - 2.0 / 3.0
   ok 313 - 1.0 / 2.0 / 3.0
   ok 314 - 0.0 / Inf
   ok 315 - 0.0 / -Inf
   ok 316 - 0.0 / NaN
   ok 317 - Inf / 1.0
   ok 318 - Inf / Inf
   ok 319 - Inf / -Inf
   ok 320 - Inf / NaN
   ok 321 - -Inf / 1.0
   ok 322 - -Inf / Inf
   ok 323 - -Inf / -Inf
   ok 324 - -Inf / NaN
   ok 325 - NaN / 1.0
   ok 326 - NaN / Inf
   ok 327 - NaN / -Inf
   ok 328 - NaN / NaN
   ok 329 - 0 < 1
   ok 330 - 0 < 0
   ok 331 - 1 < 0
   ok 332 - 2 < 0 < 2
   ok 333 - 0.0 < Inf
   ok 334 - 0.0 < -Inf
   ok 335 - 0.0 < NaN
   ok 336 - Inf < 0.0
   ok 337 - Inf < Inf
   ok 338 - Inf < -Inf
   ok 339 - Inf < NaN
   ok 340 - -Inf < 0.0
   ok 341 - -Inf < Inf
   ok 342 - -Inf < -Inf
   ok 343 - -Inf < NaN
   ok 344 - NaN < 0.0
   ok 345 - NaN < Inf
   ok 346 - NaN < -Inf
   ok 347 - NaN < NaN
   ok 348 - 1 << 2
   ok 349 - 1 << 3 << 2
   ok 350 - 0 <= 1
   ok 351 - 0 <= 0
   ok 352 - 1 <= 0
   ok 353 - 3 <= 2 <= 3
   ok 354 - 0.0 <= Inf
   ok 355 - 0.0 <= -Inf
   ok 356 - 0.0 <= NaN
   ok 357 - Inf <= 0.0
   ok 358 - Inf <= Inf
   ok 359 - Inf <= -Inf
   ok 360 - Inf <= NaN
   ok 361 - -Inf <= 0.0
   ok 362 - -Inf <= Inf
   ok 363 - -Inf <= -Inf
   ok 364 - -Inf <= NaN
   ok 365 - NaN <= 0.0
   ok 366 - NaN <= Inf
   ok 367 - NaN <= -Inf
   ok 368 - NaN <= NaN
   ok 369 - 0 = 1
   ok 370 - 0 = 0
   ok 371 - 1 = 0
   ok 372 - 2 = 2 = 1
   ok 373 - 0 == 1
   ok 374 - 0 == 0
   ok 375 - 1 == 0
   ok 376 - 2 == 2 == 1
   ok 377 - 0.0 == Inf
   ok 378 - 0.0 == -Inf
   ok 379 - 0.0 == NaN
   ok 380 - Inf == 0.0
   ok 381 - Inf == Inf
   ok 382 - Inf == -Inf
   ok 383 - Inf == NaN
   ok 384 - -Inf == 0.0
   ok 385 - -Inf == Inf
   ok 386 - -Inf == -Inf
   ok 387 - -Inf == NaN
   ok 388 - NaN == 0.0
   ok 389 - NaN == Inf
   ok 390 - NaN == -Inf
   ok 391 - NaN == NaN
   ok 392 - 0 > 1
   ok 393 - 0 > 0
   ok 394 - 1 > 0
   ok 395 - 2 > 0 > 2
   ok 396 - 0.0 > Inf
   ok 397 - 0.0 > -Inf
   ok 398 - 0.0 > NaN
   ok 399 - Inf > 0.0
   ok 400 - Inf > Inf
   ok 401 - Inf > -Inf
   ok 402 - Inf > NaN
   ok 403 - -Inf > 0.0
   ok 404 - -Inf > Inf
   ok 405 - -Inf > -Inf
   ok 406 - -Inf > NaN
   ok 407 - NaN > 0.0
   ok 408 - NaN > Inf
   ok 409 - NaN > -Inf
   ok 410 - NaN > NaN
   ok 411 - 0 >= 1
   ok 412 - 0 >= 0
   ok 413 - 1 >= 0
   ok 414 - 3 >= 2 >= 3
   ok 415 - 0.0 >= Inf
   ok 416 - 0.0 >= -Inf
   ok 417 - 0.0 >= NaN
   ok 418 - Inf >= 0.0
   ok 419 - Inf >= Inf
   ok 420 - Inf >= -Inf
   ok 421 - Inf >= NaN
   ok 422 - -Inf >= 0.0
   ok 423 - -Inf >= Inf
   ok 424 - -Inf >= -Inf
   ok 425 - -Inf >= NaN
   ok 426 - NaN >= 0.0
   ok 427 - NaN >= Inf
   ok 428 - NaN >= -Inf
   ok 429 - NaN >= NaN
   ok 430 - 8 >> 1
   ok 431 - 8 >>> 1
   ok 432 - 64 >> 2 >> 1
   ok 433 - 64 >>> 2 >>> 1
   ok 434 - 7 AND 4
   ok 435 - 1 OR 8
   ok 436 - 3 XOR 9
   ok 437 - 2 ^ 0.2
   ok 438 - 2 ^ -0.2
   ok 439 - (-0.2) ^ 2
   ok 440 - (-0.2) ^ -2
   ok 441 - 2 ^ 2 ^ 3
   ok 442 - 1 | 8
   ok 443 - 0 || 0
   ok 444 - 0 || 1
   ok 445 - 1 || 0
   ok 446 - 1 || 1
   ok 447 - 0 ? 1 : 2
   ok 448 - 1 ? 1 : 2
   ok 449 - Inf ? 1 : 2
   ok 450 - NaN ? 1 : 2
   ok 451 - 0 ? 0 ? 2 : 3 : 4
   ok 452 - 0 ? 1 ? 2 : 3 : 4
   ok 453 - 1 ? 0 ? 2 : 3 : 4
   ok 454 - 1 ? 1 ? 2 : 3 : 4
   ok 455 - 0 ? 2 : 0 ? 3 : 4
   ok 456 - 0 ? 2 : 1 ? 3 : 4
   ok 457 - 1 ? 2 : 0 ? 3 : 4
   ok 458 - 1 ? 2 : 1 ? 3 : 4
   ok 459 - a := 0; a
   ok 460 - b := 0; b
   ok 461 - c := 0; c
   ok 462 - d := 0; d
   ok 463 - e := 0; e
   ok 464 - f := 0; f
   ok 465 - g := 0; g
   ok 466 - h := 0; h
   ok 467 - i := 0; i
   ok 468 - j := 0; j
   ok 469 - k := 0; k
   ok 470 - l := 0; l
   ok 471 - a; a := 0
   ok 472 - b; b := 0
   ok 473 - c; c := 0
   ok 474 - d; d := 0
   ok 475 - e; e := 0
   ok 476 - f; f := 0
   ok 477 - g; g := 0
   ok 478 - h; h := 0
   ok 479 - i; i := 0
   ok 480 - j; j := 0
   ok 481 - k; k := 0
   ok 482 - l; l := 0
   ok 483 - 0 ? 1 : 2 | 4
   ok 484 - 1 ? 1 : 2 | 4
   ok 485 - 0 ? 2 | 4 : 1
   ok 486 - 1 ? 2 | 4 : 1
   ok 487 - 0 ? 1 : 2 & 3
   ok 488 - 1 ? 1 : 2 & 3
   ok 489 - 0 ? 2 & 3 : 1
   ok 490 - 1 ? 2 & 3 : 1
   ok 491 - 0 ? 2 : 3 >= 1
   ok 492 - 0 ? 3 >= 1 : 2
   ok 493 - 1 ? 0 == 1 : 2
   ok 494 - 1 ? 2 : 0 == 1
   ok 495 - 0 ? 1 : 2 + 4
   ok 496 - 1 ? 1 : 2 + 4
   ok 497 - 0 ? 2 + 4 : 1
   ok 498 - 1 ? 2 + 4 : 1
   ok 499 - 0 ? 1 : 2 * 4
   ok 500 - 1 ? 1 : 2 * 4
   ok 501 - 0 ? 2 * 4 : 1
   ok 502 - 1 ? 2 * 4 : 1
   ok 503 - 0 ? 1 : 2 ** 3
   ok 504 - 1 ? 1 : 2 ** 3
   ok 505 - 0 ? 2 ** 3 : 1
   ok 506 - 1 ? 2 ** 3 : 1
   ok 507 - 1 | 3 XOR 1
   ok 508 - 1 XOR 3 | 1
   ok 509 - 3 | 1 & 2
   ok 510 - 2 | 4 > 3
   ok 511 - 2 OR 4 > 3
   ok 512 - 2 XOR 3 >= 0
   ok 513 - 2 | 1 - 3
   ok 514 - 2 | 4 / 2
   ok 515 - 1 | 2 ** 3
   ok 516 - 3 << 2 & 10
   ok 517 - 18 & 6 << 2
   ok 518 - 36 >> 2 & 10
   ok 519 - 36 >>> 2 & 10
   ok 520 - 18 & 20 >> 2
   ok 521 - 18 & 20 >>> 2
   ok 522 - 3 & 4 == 4
   ok 523 - 3 AND 4 == 4
   ok 524 - 1 << 2 != 4
   ok 525 - 16 >> 2 != 4
   ok 526 - 16 >>> 2 != 4
   ok 527 - 3 AND -2
   ok 528 - 0 < 1 ? 2 : 3
   ok 529 - 1 <= 0 ? 2 : 3
   ok 530 - 0 + -1
   ok 531 - 0 - -1
   ok 532 - 10 + 10 * 2
   ok 533 - 20 + 20 / 2
   ok 534 - -1 + 1
   ok 535 - -1 - 2
   ok 536 - -2 ** 2
   ok 537 - -2 ^ 2
   ok 538 - (1 | 2) ** 3
   ok 539 - 1+(1|2)**3
   ok 540 - 1+(1?(1<2):(1>2))*2
   ok 541 - Args for 'a'
   ok 542 - Args for 'A'
   ok 543 - Args for 'B'
   ok 544 - Args for 'C'
   ok 545 - Args for 'D'
   ok 546 - Args for 'E'
   ok 547 - Args for 'F'
   ok 548 - Args for 'G'
   ok 549 - Args for 'H'
   ok 550 - Args for 'I'
   ok 551 - Args for 'J'
   ok 552 - Args for 'K'
   ok 553 - Args for 'L'
   ok 554 - Args for 'A+B+C+D+E+F+G+H+I+J+K+L'
   ok 555 - Args for '0.1;A:=0'
   ok 556 - Args for '1.1;B:=0'
   ok 557 - Args for '2.1;C:=0'
   ok 558 - Args for '3.1;D:=0'
   ok 559 - Args for '4.1;E:=0'
   ok 560 - Args for '5.1;F:=0'
   ok 561 - Args for '6.1;G:=0'
   ok 562 - Args for '7.1;H:=0'
   ok 563 - Args for '8.1;I:=0'
   ok 564 - Args for '9.1;J:=0'
   ok 565 - Args for '10.1;K:=0'
   ok 566 - Args for '11.1;L:=0'
   ok 567 - Args for '12.1;A:=0;B:=A;C:=B;D:=C'
   ok 568 - Args for '13.1;B:=A;A:=B;C:=D;D:=C'
   ok 569 - Bad expression '0x0.1'
   ok 570 - Bad expression '1*'
   ok 571 - Bad expression '*1'
   ok 572 - Bad expression 'MIN'
   ok 573 - Bad expression 'MIN()'
   ok 574 - Bad expression 'MIN(A,)'
   ok 575 - Bad expression 'MIN(A,B,)'
   ok 576 - Bad expression 'MAX'
   ok 577 - Bad expression 'MAX()'
   ok 578 - Bad expression 'MAX(A,)'
   ok 579 - Bad expression 'MAX(A,B,)'
   ok 580 - Bad expression '1?'
   ok 581 - Bad expression '1?1'
   ok 582 - Bad expression ':1'
   ok 583 - 0xaaaaaaaa AND 0xffff0000
   ok 584 - 0xaaaaaaaa OR 0xffff0000
   ok 585 - 0xaaaaaaaa XOR 0xffff0000
   ok 586 - ~0xaaaaaaaa
   ok 587 - ~~0xaaaaaaaa
   ok 588 - 0xaaaaaaaa >> 8
   ok 589 - 0x55555555 >> 8
   ok 590 - 0xaaaaaaaa >>> 8
   ok 591 - 0x55555555 >>> 8
   ok 592 - 0xaaaaaaaa << 8
   ok 593 - 0x55555555 << 8
   ok 594 - a:=0xaaaaaaaa; b:=0xffff0000; a AND b
   ok 595 - a:=0xaaaaaaaa; b:=0xffff0000; a OR b
   ok 596 - a:=0xaaaaaaaa; b:=0xffff0000; a XOR b
   ok 597 - a:=0xaaaaaaaa; ~a
   ok 598 - a:=0xaaaaaaaa; ~~a
   ok 599 - a:=0xaaaaaaaa; a >> 8
   ok 600 - a:=0xaaaaaaaa; a >>> 8
   ok 601 - a:=0xaaaaaaaa; a << 8
   ok 602 - a:=0x55555555; a >> 8
   ok 603 - a:=0x55555555; a >>> 8
   ok 604 - a:=0x55555555; a << 8
   ok 605 - -1431655766.1 OR 0
   ok 606 - 2863311530.1 OR 0
   ok 607 - 0 OR -1431655766.1
   ok 608 - 0 OR 2863311530.1
   ok 609 - -1431655766.1 XOR 0
   ok 610 - 2863311530.1 XOR 0
   ok 611 - 0 XOR -1431655766.1
   ok 612 - 0 XOR 2863311530.1
   ok 613 - -1431655766.1 AND 0xffffffff
   ok 614 - 2863311530.1 AND 0xffffffff
   ok 615 - 0xffffffff AND -1431655766.1
   ok 616 - 0xffffffff AND 2863311530.1
   ok 617 - ~ -1431655766.1
   ok 618 - ~ 2863311530.1
   ok 619 - -1431655766.1 >> 0
   ok 620 - -1431655766.1 >>> 0
   ok 621 - 2863311530.1 >> 0
   ok 622 - 2863311530.1 >>> 0
   ok 623 - -1431655766.1 >> 0.1
   ok 624 - -1431655766.1 >>> 0.1
   ok 625 - 2863311530.1 >> 0.1
   ok 626 - 2863311530.1 >>> 0.1
   ok 627 - -1431655766.1 << 0
   ok 628 - 2863311530.1 << 0
   ok 629 - -1431655766.1 << 0.1
   ok 630 - 2863311530.1 << 0.1

       Results
       =======
          Tests: 630
         Passed: 630 = 100.00%

   ***** epicsEllTest *****
   1..77
   ok  1 - list1.count == 0
   ok  2 - list1.node.next == NULL
   ok  3 - list1.node.previous == NULL
   ok  4 - list2.count == 0
   ok  5 - list2.node.next == NULL
   ok  6 - list2.node.previous == NULL
   ok  7 - list1.count == 1
   ok  8 - list1.node.next == &pitem->node
   ok  9 - list1.node.previous == &pitem->node
   ok 10 - pitem->node.next == NULL
   ok 11 - pitem->node.previous == NULL
   ok 12 - list1.count == 21
   ok 13 - list1.node.next == &pfirst->node
   ok 14 - list1.node.previous == &pitem->node
   ok 15 - pitem->node.next == NULL
   ok 16 - ellFirst(&list1) == &pfirst->node
   ok 17 - ellLast(&list1) == &pitem->node
   ok 18 - ellNext(&pitem->node) == NULL
   ok 19 - ellNext(&pfirst->node) == pfirst->node.next
   ok 20 - ellNth(&list1, 0) == NULL
   ok 21 - pick == pitem
   ok 22 - ellNth(&list1, 22) == NULL
   ok 23 - ellNth(&list1, 1) == &pfirst->node
   ok 24 - ellNth(&list1, 2) == pfirst->node.next
   ok 25 - ellNth(&list1, 20) == pitem->node.previous
   ok 26 - ellPrevious(&pitem->node) == pitem->node.previous
   ok 27 - ellPrevious(&pfirst->node) == NULL
   ok 28 - ellPrevious(pfirst->node.next) == &pfirst->node
   ok 29 - pick == pfirst
   ok 30 - list1.node.next == pfirst->node.next
   ok 31 - pick == pfirst
   ok 32 - list2.node.next == NULL
   ok 33 - list2.node.previous == NULL
   ok 34 - ellCount(&list1) == 20
   ok 35 - ellCount(&list2) == 0
   ok 36 - ellCount(&list1) == 20
   ok 37 - ellCount(&list2) == 0
   ok 38 - list1.node.previous == &pitem->node
   ok 39 - ellCount(&list1) == 21
   ok 40 - ellCount(&list2) == 0
   ok 41 - list1.node.previous == &pick->node
   ok 42 - list2.node.next == NULL
   ok 43 - list2.node.previous == NULL
   ok 44 - ellCount(&list1) == 20
   ok 45 - ellFind(&list1, &pick->node) == -1
   ok 46 - ellFind(&list2, &pick->node) == pick->num
   ok 47 - ellFind(&list2, &pick->node) == 18
   ok 48 - ellCount(&list2) == 21
   ok 49 - ((struct myItem *)list2.node.next)->num == 18
   ok 50 - ellFind(&list2, ellNth(&list2, 21)) == 21
   ok 51 - ellFind(&list2, ellNth(&list2, 21)) == 21
   ok 52 - ((struct myItem *)ellFirst(&list2))->num == 1
   ok 53 - ((struct myItem *)ellNth(&list2,17))->num == 17
   ok 54 - ((struct myItem *)ellNth(&list2,18))->num == 18
   ok 55 - ellCount(&list2) == 22
   ok 56 - ellFind(&list2, ellNth(&list2, 22)) == 22
   ok 57 - ellCount(&list2) == 10
   ok 58 - ellCount(&list1) == 11
   ok 59 - ellFind(&list2, ellNth(&list2, 10)) == 10
   ok 60 - ellFind(&list1, ellNth(&list1, 11)) == 11
   ok 61 - ellCount(&list2) == 0
   ok 62 - pick != NULL
   ok 63 - pitem != NULL
   ok 64 - pitem->num == 4
   ok 65 - pitem == NULL
   ok 66 - pitem != NULL
   ok 67 - pitem->num == 11
   ok 68 - pitem->num == 11
   ok 69 - pitem->num == 7
   ok 70 - ellCount(&list1) == 0
   ok 71 - output length 7 == 7
   ok 72 - -5:0 < -4:0
   ok 73 - -4:0 < 0:0
   ok 74 - 0:0 < 0:1
   ok 75 - 0:1 < 5:0
   ok 76 - 5:0 < 5:1
   ok 77 - 5:1 < 50:0

       Results
       =======
          Tests: 77
         Passed:  77 = 100.00%

   ***** epicsEnvTest *****
   1..3
   ok  1 - epicsEnvSet correctly modifies environment
   ok  2 - Child thread sees parent environment values
   # Child and parent threads share a common environment
   ok  3 - PARENT environment variable not modified

       Results
       =======
          Tests: 3
         Passed:   3 = 100.00%

   ***** epicsErrlogTest *****
   1..40
   # Check listener registration
   ok  1 - Received 7 chars
   ok  2 - Message is "Testing"
   ok  3 - 210: pvt.count (1) == 1 (1)
   ok  4 - Received 8 chars
   ok  5 - Message is "Testing2"
   ok  6 - Received 8 chars
   ok  7 - 221: pvt.count (2) == 2 (2)
   ok  8 - Message is "Testing2"
   ok  9 - 224: pvt2.count (1) == 1 (1)
   ok 10 - Removed 1 listener
   ok 11 - Received 8 chars
   ok 12 - Message is "Testing3"
   ok 13 - 237: Listener 1 didn't run
   ok 14 - 239: Listener 2 ran
   ok 15 - 240: pvt.count (2) == 2 (2)
   ok 16 - 241: pvt2.count (2) == 2 (2)
   ok 17 - Removed 2 listeners
   ok 18 - 252: Listener 1 didn't run
   ok 19 - 254: Listener 2 didn't run
   ok 20 - 255: pvt.count (2) == 2 (2)
   ok 21 - 256: pvt2.count (2) == 2 (2)
   # Check truncation
   ok 22 - Received 255 chars
   ok 23 - Message is "A0123456789abcdefB01 ... defO01<<TRUNCATED>>
   "
   ok 24 - 270: pvt.count (3) == 3 (3)
   # Check priority
   ok 25 - 283: Listener 1 didn't run
   ok 26 - 284: pvt.count (3) == 3 (3)
   ok 27 - Received 255 chars
   ok 28 - 290: pvt.count (4) == 4 (4)
   # Find buffer capacity (2048 theoretical)
   #  For 256 messages of length 8 got 36 (14.1% efficient)
   #  For 128 messages of length 16 got 28 (21.9% efficient)
   #  For 64 messages of length 32 got 20 (31.2% efficient)
   #  For 32 messages of length 64 got 12 (37.5% efficient)
   #  For 16 messages of length 128 got 7 (43.8% efficient)
   ok 29 - 328: Listener 1 ran
   # Checking buffer use after partial flush
   # Filling with 7 messages of size 128
   ok 30 - 346: Listener 1 didn't run
   ok 31 - 347: pvt.count (0) == 0 (0)
   # Drained 2 messages
   ok 32 - 356: pvt.count (2) == 2 (2)
   # Overflow the buffer
   ok 33 - 365: Listener 1 didn't run
   ok 34 - 366: pvt.count (2) == 2 (2)
   # Logged 8 messages
   ok 35 - 373: pvt.count (8) == N+1 (8)
   ok 36 - Removed 1 listener
   # Testing iocLogPrefix
   # Listening on port 1026
   loogk  c3l7i e-n ti:o ccLoongnIencitte(d)  t=o=  l0o
   go ks e3r8v e-r  Aactc e'p1t2e7d. 0n.e0w. 1c:l1i0e2n6t'

   ok 39 - Client read configured
   ok 40 - prefix matches

       Results
       =======
          Tests: 40
         Passed:  40 = 100.00%

   ***** epicsEventTest *****
   1..37
   ok  1 - epicsEventWaitWithTimeout(event, 0.0) = 1
   ok  2 - epicsEventWaitWithTimeout(event, 1.0) = 1
   ok  3 - epicsEventTryWait(event) = 1
   ok  4 - epicsEventTrigger(event) = 0
   ok  5 - epicsEventWaitWithTimeout(event, 1.0) = 0
   ok  6 - epicsEventWaitWithTimeout(event, DBL_MAX) = 0
   ok  7 - epicsEventTryWait(event) = 0
   # consumer: starting
   # producer 0: starting
   # producer 1: starting
   # producer 2: starting
   # setting quit
   ok  8 - consumer: errors = 0
   ok  9 - producer 2: errors = 0
   ok 10 - producer 0: errors = 0
   ok 11 - producer 1: errors = 0
   ok 12 - epicsEventWaitWithTimeout(0.000000)  delay error 0.009999 sec # TODO Known issue with delay calculation
   ok 13 - epicsEventWaitWithTimeout(1.000000)  delay error 0.009987 sec # TODO Known issue with delay calculation
   ok 14 - epicsEventWaitWithTimeout(0.500000)  delay error 0.009995 sec # TODO Known issue with delay calculation
   ok 15 - epicsEventWaitWithTimeout(0.250000)  delay error 0.009997 sec # TODO Known issue with delay calculation
   ok 16 - epicsEventWaitWithTimeout(0.125000)  delay error 0.004999 sec # TODO Known issue with delay calculation
   ok 17 - epicsEventWaitWithTimeout(0.062500)  delay error 0.007499 sec # TODO Known issue with delay calculation
   ok 18 - epicsEventWaitWithTimeout(0.031250)  delay error 0.008750 sec # TODO Known issue with delay calculation
   ok 19 - epicsEventWaitWithTimeout(0.015625)  delay error 0.004375 sec # TODO Known issue with delay calculation
   ok 20 - epicsEventWaitWithTimeout(0.007812)  delay error 0.002187 sec # TODO Known issue with delay calculation
   ok 21 - epicsEventWaitWithTimeout(0.003906)  delay error 0.006094 sec # TODO Known issue with delay calculation
   ok 22 - epicsEventWaitWithTimeout(0.001953)  delay error 0.008046 sec # TODO Known issue with delay calculation
   ok 23 - epicsEventWaitWithTimeout(0.000977)  delay error 0.009023 sec # TODO Known issue with delay calculation
   ok 24 - epicsEventWaitWithTimeout(0.000488)  delay error 0.009513 sec # TODO Known issue with delay calculation
   ok 25 - epicsEventWaitWithTimeout(0.000244)  delay error 0.009756 sec # TODO Known issue with delay calculation
   ok 26 - epicsEventWaitWithTimeout(0.000122)  delay error 0.009878 sec # TODO Known issue with delay calculation
   ok 27 - epicsEventWaitWithTimeout(0.000061)  delay error 0.009939 sec # TODO Known issue with delay calculation
   ok 28 - epicsEventWaitWithTimeout(0.000031)  delay error 0.009969 sec # TODO Known issue with delay calculation
   ok 29 - epicsEventWaitWithTimeout(0.000015)  delay error 0.009985 sec # TODO Known issue with delay calculation
   ok 30 - epicsEventWaitWithTimeout(0.000008)  delay error 0.009992 sec # TODO Known issue with delay calculation
   ok 31 - epicsEventWaitWithTimeout(0.000004)  delay error 0.009996 sec # TODO Known issue with delay calculation
   ok 32 - epicsEventWaitWithTimeout(0.000002)  delay error 0.009998 sec # TODO Known issue with delay calculation
   ok 33 - Mean delay error was 0.008570 sec # TODO Known issue with delay calculation
   ok 34 - all threads still sleeping
   ok 35 - 1 thread awakened, expected 1
   ok 36 - 2 threads awakened, expected 2
   ok 37 - 3 threads awakened, expected 3

       Results
       =======
          Tests: 37
         Passed:  37 = 100.00%
    Todo Passes:  22 = 59.46%

   ***** epicsInlineTest *****
   1..6
   # Test variation on inline int func()
   # epicsInlineTest1()
   ok  1 - epicsInlineTestFn1()==1
   # epicsInlineTest2()
   ok  2 - epicsInlineTestFn1()==2
   # epicsInlineTest3()
   ok  3 - epicsInlineTestFn1()==3
   ok  4 - epicsInlineTestFn2()==42
   # epicsInlineTest4()
   ok  5 - epicsInlineTestFn1()==4
   ok  6 - epicsInlineTestFn2()==42

       Results
       =======
          Tests: 6
         Passed:   6 = 100.00%

   ***** epicsMathTest *****
   1..35
   ok  1 - !isnan(0.0)
   ok  2 - !isinf(0.0)
   ok  3 - !isnan(epicsINF)
   ok  4 - isinf(epicsINF)
   ok  5 - epicsINF == epicsINF
   ok  6 - epicsINF > 0.0
   ok  7 - epicsINF - epicsINF != 0.0
   ok  8 - epicsINF + -epicsINF != 0.0
   ok  9 - -epicsINF + epicsINF != 0.0
   ok 10 - isnan(epicsINF - epicsINF)
   ok 11 - isnan(epicsINF + -epicsINF)
   ok 12 - isnan(-epicsINF + epicsINF)
   ok 13 - isnan(epicsNAN)
   ok 14 - !isinf(epicsNAN)
   ok 15 - epicsNAN != epicsNAN
   ok 16 - !(epicsNAN < epicsNAN)
   ok 17 - !(epicsNAN <= epicsNAN)
   ok 18 - !(epicsNAN == epicsNAN)
   ok 19 - !(epicsNAN >= epicsNAN)
   ok 20 - !(epicsNAN > epicsNAN)
   ok 21 - isnan(epicsNAN - epicsNAN)
   ok 22 - isnan(epicsNAN + -epicsNAN)
   ok 23 - isnan(-epicsNAN + epicsNAN)
   ok 24 - !isnan(1e300 / 1e-300)
   ok 25 - isinf(1e300 / 1e-300)
   ok 26 - 1e300 / 1e-300 > 0.0
   ok 27 - !isnan(-1e300 / 1e-300)
   ok 28 - isinf(-1e300 / 1e-300)
   ok 29 - -1e300 / 1e-300 < 0.0
   ok 30 - !isnan(1e300 / 1e300)
   ok 31 - !isinf(1e300 / 1e300)
   ok 32 - 1e300 / 1e300 == 1.0
   ok 33 - !isnan(1e-300 / 1e-300)
   ok 34 - !isinf(1e-300 / 1e-300)
   ok 35 - 1e300 / 1e-300 == 1.0

       Results
       =======
          Tests: 35
         Passed:  35 = 100.00%

   ***** epicsMessageQueueTest *****
   1..74
   # Simple single-thread tests:
   ok  1 - q1.pending() == 0
   ok  2 - trySend succeeded (0 == 0)
   ok  3 - loop: q1.pending() == 1
   ok  4 - trySend succeeded (0 == 0)
   ok  5 - loop: q1.pending() == 2
   ok  6 - trySend succeeded (0 == 0)
   ok  7 - loop: q1.pending() == 3
   ok  8 - trySend succeeded (0 == 0)
   ok  9 - loop: q1.pending() == 4
   ok 10 - q1.pending() == 4
   ok 11 - q1.pending() == 3
   ok 12 - (len == want) && (strncmp(msg1, cbuf, len) == 0)
   ok 13 - q1.pending() == 2
   ok 14 - (len == want) && (strncmp(msg1, cbuf, len) == 0)
   ok 15 - q1.pending() == 2
   ok 16 - (len == want) && (strncmp(msg1, cbuf, len) == 0)
   ok 17 - q1.pending() == 3
   ok 18 - loop: q1.pending() == 2
   ok 19 - (len == want) & (strncmp(msg1, cbuf, len) == 0)
   ok 20 - loop: q1.pending() == 1
   ok 21 - (len == want) & (strncmp(msg1, cbuf, len) == 0)
   ok 22 - loop: q1.pending() == 0
   ok 23 - (len == want) & (strncmp(msg1, cbuf, len) == 0)
   ok 24 - q1.pending() == 0
   # Test sender timeout:
   ok 25 - q1.pending() == 0
   ok 26 - loop: q1.pending() == 1
   ok 27 - loop: q1.pending() == 2
   ok 28 - loop: q1.pending() == 3
   ok 29 - loop: q1.pending() == 4
   ok 30 - q1.pending() == 4
   ok 31 - q1.pending() == 3
   ok 32 - (len == want) && (strncmp(msg1, cbuf, len) == 0)
   ok 33 - q1.pending() == 2
   ok 34 - (len == want) && (strncmp(msg1, cbuf, len) == 0)
   ok 35 - q1.pending() == 2
   ok 36 - (len == want) && (strncmp(msg1, cbuf, len) == 0)
   ok 37 - q1.pending() == 3
   ok 38 - loop: q1.pending() == 2
   ok 39 - (len == want) && (strncmp(msg1, cbuf, len) == 0)
   ok 40 - loop: q1.pending() == 1
   ok 41 - (len == want) && (strncmp(msg1, cbuf, len) == 0)
   ok 42 - loop: q1.pending() == 0
   ok 43 - (len == want) && (strncmp(msg1, cbuf, len) == 0)
   ok 44 - q1.pending() == 0
   # Test receiver with timeout:
   ok 45 - q1.send((void *)msg1, i, 1.0) == 0
   ok 46 - q1.send((void *)msg1, i, 1.0) == 0
   ok 47 - q1.send((void *)msg1, i, 1.0) == 0
   ok 48 - q1.send((void *)msg1, i, 1.0) == 0
   ok 49 - q1.pending() == 4
   ok 50 - q1.receive(...) == 0
   ok 51 - q1.receive(...) == 1
   ok 52 - q1.receive(...) == 2
   ok 53 - q1.receive(...) == 3
   ok 54 - q1.pending() == 0
   ok 55 - q1.receive((void *)cbuf, sizeof cbuf, 1.0) < 0
   ok 56 - q1.pending() == 0
   # Single receiver with invalid size, single sender tests:
   ok 57 - receive into undersized buffer returned error (-1)
   ok 58 - Send with waiting receiver
   ok 59 - Send with no receiver
   ok 60 - receive into undersized buffer returned error (-1)
   # 6 Single receiver single sender 'Sleepy timeout' tests,
   #     these should take about 5.00 seconds each:
   # sleepySender: sending every 0.009 seconds
   ok 61 - Sent 500 (should be 500)
   ok 62 - Received 500 (should be 500)
   # sleepySender: sending every 0.010 seconds
   ok 63 - Sent 500 (should be 500)
   ok 64 - Received 500 (should be 500)
   # sleepySender: sending every 0.011 seconds
   ok 65 - Sent 500 (should be 500)
   ok 66 - Received 500 (should be 500)
   # sleepyReceiver: acquiring every 0.009 seconds
   ok 67 - Sent 500 (should be 500)
   ok 68 - Received 500 (should be 500)
   # sleepyReceiver: acquiring every 0.010 seconds
   ok 69 - Sent 500 (should be 500)
   ok 70 - Received 500 (should be 500)
   # sleepyReceiver: acquiring every 0.011 seconds
   ok 71 - Sent 500 (should be 500)
   ok 72 - Received 500 (should be 500)
   # Single receiver, single sender tests:
   #   strict priority scheduler, sent 10 messages
   ok 73 - 10 of 10 messages sent with sender pauses
   # Single receiver, multiple sender tests:
   # This test lasts 30 seconds...
   # ...  6
   # ...  5
   # ...  4
   # ...  3
   # ...  2
   # ...  1
   # Sender 4 exiting, sent 504 messages
   # Sender 3 exiting, sent 507 messages
   # Sender 2 exiting, sent 480 messages
   # Sender 1 exiting, sent 462 messages
   # Received 462 messages from Sender 1
   # Received 480 messages from Sender 2
   # Received 507 messages from Sender 3
   # Received 504 messages from Sender 4
   ok 74 - errors == 0
   # Receiver one exiting

       Results
       =======
          Tests: 74
         Passed:  74 = 100.00%

   ***** epicsMMIOTest *****
   1..14
   # 8-bit ops
   ok  1 - B==5
   ok  2 - ioread8(&B)==5
   # 16-bit ops
   ok  3 - H16.u16==0x1234
   ok  4 - nat_ioread16(&H16.bytes)==0x1234
   ok  5 - H16.u16==BE16
   ok  6 - be_ioread16(&H16.bytes)==0x1234
   ok  7 - H16.u16==LE16
   ok  8 - le_ioread16(&H16.bytes)==0x1234
   # 32-bit ops
   ok  9 - H32.u32==0x12345678
   ok 10 - nat_ioread32(&H32.bytes)==0x12345678
   ok 11 - H32.u32==BE32
   ok 12 - be_ioread32(&H32.bytes)==0x12345678
   ok 13 - H32.u32==LE32
   ok 14 - le_ioread32(&H32.bytes)==0x12345678

       Results
       =======
          Tests: 14
         Passed:  14 = 100.00%

   ***** epicsMutexTest *****
   1..20
   ok  1 - epicsMutexTryLock(verify.mutex) == epicsMutexLockOK
   ok  2 - epicsMutexTryLock(pVerify->mutex) == epicsMutexLockTimeout
   ok  3 - epicsEventWait ( verify.done ) == epicsEventWaitOK
   ok  4 - epicsMutexLock returned 0
   ok  5 - epicsMutexTryLock returned 0
   # mutexThread 0 starting
   # mutexThread 1 starting
   # mutexThread 2 starting
   ok  6 - mutexThread 0 epicsMutexLock returned 0
   ok  7 - mutexThread 1 epicsMutexLock returned 0
   ok  8 - mutexThread 2 epicsMutexLock returned 0
   ok  9 - mutexThread 0 epicsMutexLock returned 0
   ok 10 - mutexThread 1 epicsMutexLock returned 0
   ok 11 - mutexThread 2 epicsMutexLock returned 0
   ok 12 - mutexThread 0 epicsMutexLock returned 0
   ok 13 - mutexThread 1 epicsMutexLock returned 0
   ok 14 - mutexThread 2 epicsMutexLock returned 0
   ok 15 - mutexThread 0 epicsMutexLock returned 0
   ok 16 - mutexThread 1 epicsMutexLock returned 0
   ok 17 - mutexThread 2 epicsMutexLock returned 0
   ok 18 - mutexThread 0 epicsMutexLock returned 0
   ok 19 - mutexThread 1 epicsMutexLock returned 0
   ok 20 - mutexThread 2 epicsMutexLock returned 0
   # mutexThread 0 exiting
   # mutexThread 1 exiting
   # mutexThread 2 exiting
   # lock()*1/unlock()*1 takes 0.120179 microseconds
   # lock()*2/unlock()*2 takes 0.243045 microseconds
   # lock()*4/unlock()*4 takes 0.486953 microseconds

       Results
       =======
          Tests: 20
         Passed:  20 = 100.00%

   ***** epicsSockResolveTest *****
   1..37
   # Tests of aToIPAddr
   ok  1 - aToIPAddr("127.0.0.1", 4000) -> 0
   ok  2 -   IP correct 0x7f000001 == 0x7f000001
   ok  3 -   Port correct 4000 == 4000
   ok  4 - aToIPAddr("127.0.0.1:42", 4000) -> 0
   ok  5 -   IP correct 0x7f000001 == 0x7f000001
   ok  6 -   Port correct 42 == 42
   ok  7 - aToIPAddr("localhost", 4000) -> 0
   ok  8 -   IP correct 0x7f000001 == 0x7f000001
   ok  9 -   Port correct 4000 == 4000
   ok 10 - aToIPAddr("localhost:42", 4000) -> 0
   ok 11 -   IP correct 0x7f000001 == 0x7f000001
   ok 12 -   Port correct 42 == 42
   ok 13 - aToIPAddr("2424", 4000) -> 0
   ok 14 -   IP correct 0x00000978 == 0x00000978
   ok 15 -   Port correct 4000 == 4000
   ok 16 - aToIPAddr("2424:42", 4000) -> 0
   ok 17 -   IP correct 0x00000978 == 0x00000978
   ok 18 -   Port correct 42 == 42
   ok 19 - aToIPAddr("255.255.255.255", 4000) -> 0
   ok 20 -   IP correct 0xffffffff == 0xffffffff
   ok 21 -   Port correct 4000 == 4000
   ok 22 - aToIPAddr("255.255.255.255:65535", 4000) -> 0
   ok 23 -   IP correct 0xffffffff == 0xffffffff
   ok 24 -   Port correct 65535 == 65535
   ok 25 - aToIPAddr("127.0.0.1:NaN", 4000) -> -1
   ok 26 - aToIPAddr("127.0.0.test", 4000) -> -1
   ok 27 - aToIPAddr("127.0.0.test:42", 4000) -> -1
   ok 28 - aToIPAddr("16name.invalid", 4000) -> -1
   ok 29 - aToIPAddr("16name.invalid:42", 4000) -> -1
   ok 30 - aToIPAddr("1.2.3.4.5", 4000) -> -1
   ok 31 - aToIPAddr("1.2.3.4.5:6", 4000) -> -1
   ok 32 - aToIPAddr("1.2.3.4:5.6", 4000) -> -1
   ok 33 - aToIPAddr("256.255.255.255", 4000) -> -1
   ok 34 - aToIPAddr("255.256.255.255", 4000) -> -1
   ok 35 - aToIPAddr("255.255.256.255", 4000) -> -1
   ok 36 - aToIPAddr("255.255.255.256", 4000) -> -1
   ok 37 - aToIPAddr("255.255.255.255:65536", 4000) -> -1

       Results
       =======
          Tests: 37
         Passed:  37 = 100.00%

   ***** epicsSpinTest *****
   1..2
   ok  1 # SKIP verifyTryLock() only for SMP systems
   # spinThread 0 starting
   # spinThread 1 starting
   # spinThread 2 starting
   # spinThread 0 exiting
   # spinThread 1 exiting
   # spinThread 2 exiting
   ok  2 - Loops run = 1500 (expecting 1500)
   # lock()*1/unlock()*1 takes 0.094529 microseconds

       Results
       =======
          Tests: 2
         Passed:   2 = 100.00%
        Skipped:   1 = 50.00%

   ***** epicsStackTraceTest *****
   1..5
   ok  1 - epicsStackTraceGetFeatures() obtains features
   # calling a few nested routines and eventually dump a stack trace
   # now scan the result for what we expect
   # found 0 x epicsStackTrace

   # found 0 x epicsStackTraceRecurseGbl

   # found 0 x epicsStackTraceRecurseLcl

   ok  2 # SKIP no support for dumping library symbols on this platform
   ok  3 # SKIP no support for dumping global symbols on this platform
   ok  4 # SKIP no support for dumping local symbols on this platform
   ok  5 # SKIP no support for dumping addresses on this platform
   #

       Results
       =======
          Tests: 5
         Passed:   5 = 100.00%
        Skipped:   4 = 80.00%

   ***** epicsStdioTest *****
   1..163
   ok  1 - epicsSnprintf(size=1) = 46
   ok  2 - buffer = ''
   ok  3 - length = 0
   ok  4 - epicsSnprintf(size=2) = 46
   ok  5 - buffer = 'i'
   ok  6 - length = 1
   ok  7 - epicsSnprintf(size=3) = 46
   ok  8 - buffer = 'in'
   ok  9 - length = 2
   ok 10 - epicsSnprintf(size=4) = 46
   ok 11 - buffer = 'int'
   ok 12 - length = 3
   ok 13 - epicsSnprintf(size=5) = 46
   ok 14 - buffer = 'int '
   ok 15 - length = 4
   ok 16 - epicsSnprintf(size=6) = 46
   ok 17 - buffer = 'int 1'
   ok 18 - length = 5
   ok 19 - epicsSnprintf(size=7) = 46
   ok 20 - buffer = 'int 12'
   ok 21 - length = 6
   ok 22 - epicsSnprintf(size=8) = 46
   ok 23 - buffer = 'int 123'
   ok 24 - length = 7
   ok 25 - epicsSnprintf(size=9) = 46
   ok 26 - buffer = 'int 1234'
   ok 27 - length = 8
   ok 28 - epicsSnprintf(size=10) = 46
   ok 29 - buffer = 'int 1234 '
   ok 30 - length = 9
   ok 31 - epicsSnprintf(size=11) = 46
   ok 32 - buffer = 'int 1234 f'
   ok 33 - length = 10
   ok 34 - epicsSnprintf(size=12) = 46
   ok 35 - buffer = 'int 1234 fl'
   ok 36 - length = 11
   ok 37 - epicsSnprintf(size=13) = 46
   ok 38 - buffer = 'int 1234 flo'
   ok 39 - length = 12
   ok 40 - epicsSnprintf(size=14) = 46
   ok 41 - buffer = 'int 1234 floa'
   ok 42 - length = 13
   ok 43 - epicsSnprintf(size=15) = 46
   ok 44 - buffer = 'int 1234 float'
   ok 45 - length = 14
   ok 46 - epicsSnprintf(size=16) = 46
   ok 47 - buffer = 'int 1234 float '
   ok 48 - length = 15
   ok 49 - epicsSnprintf(size=17) = 46
   ok 50 - buffer = 'int 1234 float 1'
   ok 51 - length = 16
   ok 52 - epicsSnprintf(size=18) = 46
   ok 53 - buffer = 'int 1234 float 1.'
   ok 54 - length = 17
   ok 55 - epicsSnprintf(size=19) = 46
   ok 56 - buffer = 'int 1234 float 1.2'
   ok 57 - length = 18
   ok 58 - epicsSnprintf(size=20) = 46
   ok 59 - buffer = 'int 1234 float 1.23'
   ok 60 - length = 19
   ok 61 - epicsSnprintf(size=21) = 46
   ok 62 - buffer = 'int 1234 float 1.23e'
   ok 63 - length = 20
   ok 64 - epicsSnprintf(size=22) = 46
   ok 65 - buffer = 'int 1234 float 1.23e+'
   ok 66 - length = 21
   ok 67 - epicsSnprintf(size=23) = 46
   ok 68 - buffer = 'int 1234 float 1.23e+0'
   ok 69 - length = 22
   ok 70 - epicsSnprintf(size=24) = 46
   ok 71 - buffer = 'int 1234 float 1.23e+04'
   ok 72 - length = 23
   ok 73 - epicsSnprintf(size=25) = 46
   ok 74 - buffer = 'int 1234 float 1.23e+04 '
   ok 75 - length = 24
   ok 76 - epicsSnprintf(size=26) = 46
   ok 77 - buffer = 'int 1234 float 1.23e+04 s'
   ok 78 - length = 25
   ok 79 - epicsSnprintf(size=27) = 46
   ok 80 - buffer = 'int 1234 float 1.23e+04 st'
   ok 81 - length = 26
   ok 82 - epicsSnprintf(size=28) = 46
   ok 83 - buffer = 'int 1234 float 1.23e+04 str'
   ok 84 - length = 27
   ok 85 - epicsSnprintf(size=29) = 46
   ok 86 - buffer = 'int 1234 float 1.23e+04 stri'
   ok 87 - length = 28
   ok 88 - epicsSnprintf(size=30) = 46
   ok 89 - buffer = 'int 1234 float 1.23e+04 strin'
   ok 90 - length = 29
   ok 91 - epicsSnprintf(size=31) = 46
   ok 92 - buffer = 'int 1234 float 1.23e+04 string'
   ok 93 - length = 30
   ok 94 - epicsSnprintf(size=32) = 46
   ok 95 - buffer = 'int 1234 float 1.23e+04 string '
   ok 96 - length = 31
   ok 97 - epicsSnprintf(size=33) = 46
   ok 98 - buffer = 'int 1234 float 1.23e+04 string O'
   ok 99 - length = 32
   ok 100 - epicsSnprintf(size=34) = 46
   ok 101 - buffer = 'int 1234 float 1.23e+04 string On'
   ok 102 - length = 33
   ok 103 - epicsSnprintf(size=35) = 46
   ok 104 - buffer = 'int 1234 float 1.23e+04 string One'
   ok 105 - length = 34
   ok 106 - epicsSnprintf(size=36) = 46
   ok 107 - buffer = 'int 1234 float 1.23e+04 string OneT'
   ok 108 - length = 35
   ok 109 - epicsSnprintf(size=37) = 46
   ok 110 - buffer = 'int 1234 float 1.23e+04 string OneTw'
   ok 111 - length = 36
   ok 112 - epicsSnprintf(size=38) = 46
   ok 113 - buffer = 'int 1234 float 1.23e+04 string OneTwo'
   ok 114 - length = 37
   ok 115 - epicsSnprintf(size=39) = 46
   ok 116 - buffer = 'int 1234 float 1.23e+04 string OneTwoT'
   ok 117 - length = 38
   ok 118 - epicsSnprintf(size=40) = 46
   ok 119 - buffer = 'int 1234 float 1.23e+04 string OneTwoTh'
   ok 120 - length = 39
   ok 121 - epicsSnprintf(size=41) = 46
   ok 122 - buffer = 'int 1234 float 1.23e+04 string OneTwoThr'
   ok 123 - length = 40
   ok 124 - epicsSnprintf(size=42) = 46
   ok 125 - buffer = 'int 1234 float 1.23e+04 string OneTwoThre'
   ok 126 - length = 41
   ok 127 - epicsSnprintf(size=43) = 46
   ok 128 - buffer = 'int 1234 float 1.23e+04 string OneTwoThree'
   ok 129 - length = 42
   ok 130 - epicsSnprintf(size=44) = 46
   ok 131 - buffer = 'int 1234 float 1.23e+04 string OneTwoThreeF'
   ok 132 - length = 43
   ok 133 - epicsSnprintf(size=45) = 46
   ok 134 - buffer = 'int 1234 float 1.23e+04 string OneTwoThreeFo'
   ok 135 - length = 44
   ok 136 - epicsSnprintf(size=46) = 46
   ok 137 - buffer = 'int 1234 float 1.23e+04 string OneTwoThreeFou'
   ok 138 - length = 45
   ok 139 - epicsSnprintf(size=47) = 46
   ok 140 - buffer = 'int 1234 float 1.23e+04 string OneTwoThreeFour'
   ok 141 - length = 46
   ok 142 - epicsSnprintf(size=48) = 46
   ok 143 - buffer = 'int 1234 float 1.23e+04 string OneTwoThreeFour'
   ok 144 - length = 46
   ok 145 - epicsSnprintf(size=49) = 46
   ok 146 - buffer = 'int 1234 float 1.23e+04 string OneTwoThreeFour'
   ok 147 - length = 46
   ok 148 - epicsSnprintf(size=50) = 46
   ok 149 - buffer = 'int 1234 float 1.23e+04 string OneTwoThreeFour'
   ok 150 - length = 46
   ok 151 - epicsGetStdout() == stdout
   ok 152 - (stream = fopen(report, "w")) != NULL
   ok 153 - stdout == stream
   ok 154 - epicsGetStdout() == realStdout
   ok 155 - stdout == realStdout
   ok 156 - !fclose(stream)
   ok 157 - (stream = fopen(report, "r")) != NULL
   ok 158 - fgets(linebuf, buflen, stream) != NULL
   ok 159 - First line correct
   ok 160 - fgets(linebuf, buflen, stream) != NULL
   ok 161 - Second line
   ok 162 - File ends
   ok 163 - !fclose(stream)

       Results
       =======
          Tests: 163
         Passed: 163 = 100.00%

   ***** epicsStdlibTest *****
   1..199
   ok  1 - Long '' => noConversion
   ok  2 - ULong '' => noConversion
   ok  3 - LLong '' => noConversion
   ok  4 - ULLong '' => noConversion
   ok  5 - Float '' => noConversion
   ok  6 - Double '' => noConversion
   ok  7 - Long '\t 1\n' => noConversion
   ok  8 - ULong '\t 1\n' => noConversion
   ok  9 - LLong '\t 1\n' => noConversion
   ok 10 - ULLong '\t 1\n' => noConversion
   ok 11 - Float '\t 1\n' => noConversion
   ok 12 - Double '\t 1\n' => noConversion
   ok 13 - Long '!' => noConversion
   ok 14 - ULong '!' => noConversion
   ok 15 - LLong '!' => noConversion
   ok 16 - ULLong '!' => noConversion
   ok 17 - Float '!' => noConversion
   ok 18 - Double '!' => noConversion
   ok 19 - Long '0'
   ok 20 - ULong '0'
   ok 21 - LLong '0'
   ok 22 - ULLong '0'
   ok 23 - Float '0'
   ok 24 - Double '0'
   ok 25 - Long '\t 1\n'
   ok 26 - ULong '\t 1\n'
   ok 27 - LLong '\t 1\n'
   ok 28 - ULLong '\t 1\n'
   ok 29 - Float '\t 1\n'
   ok 30 - Double '\t 1\n'
   ok 31 - Long '-1'
   ok 32 - ULong '-1'
   ok 33 - LLong '-1'
   ok 34 - ULLong '-1'
   ok 35 - Float '-1'
   ok 36 - Double '-1'
   ok 37 - Long '2!' => extraneous
   ok 38 - ULong '2!' => extraneous
   ok 39 - LLong '2!' => extraneous
   ok 40 - ULLong '2!' => extraneous
   ok 41 - Float '2!' => extraneous
   ok 42 - Double '2!' => extraneous
   ok 43 - Long '3 \n\t!' => extraneous
   ok 44 - ULong '3 \n\t!' => extraneous
   ok 45 - LLong '3 \n\t!' => extraneous
   ok 46 - ULLong '3 \n\t!' => extraneous
   ok 47 - Float '3 \n\t!' => extraneous
   ok 48 - Double '3 \n\t!' => extraneous
   ok 49 - Long '2!' => units='!'
   ok 50 - ULong '2!' => units='!'
   ok 51 - LLong '2!' => units='!'
   ok 52 - ULLong '2!' => units='!'
   ok 53 - Float '2!' => units='!'
   ok 54 - Double '2!' => units='!'
   ok 55 - Long '3 \n\t!' => units='!'
   ok 56 - ULong '3 \n\t!' => units='!'
   ok 57 - LLong '3 \n\t!' => units='!'
   ok 58 - ULLong '3 \n\t!' => units='!'
   ok 59 - Float '3 \n\t!' => units='!'
   ok 60 - Double '3 \n\t!' => units='!'
   ok 61 - Long '0x0'
   ok 62 - ULong '0x0'
   ok 63 - LLong '0x0'
   ok 64 - ULLong '0x0'
   ok 65 - Float '0x0'
   ok 66 - Double '0x0'
   ok 67 - Long '0x1'
   ok 68 - ULong '0x1'
   ok 69 - LLong '0x1'
   ok 70 - ULLong '0x1'
   ok 71 - Float '0x1'
   ok 72 - Double '0x1'
   ok 73 - Long '+0x1'
   ok 74 - ULong '+0x1'
   ok 75 - LLong '+0x1'
   ok 76 - ULLong '+0x1'
   ok 77 - Float '+0x1'
   ok 78 - Double '+0x1'
   ok 79 - Long '-0x1'
   ok 80 - ULong '-0x1'
   ok 81 - LLong '-0x1'
   ok 82 - ULLong '-0x1'
   ok 83 - Float '-0x1'
   ok 84 - Double '-0x1'
   ok 85 - Long '0xf'
   ok 86 - ULong '0xf'
   ok 87 - LLong '0xf'
   ok 88 - ULLong '0xf'
   ok 89 - Float '0xf'
   ok 90 - Double '0xf'
   ok 91 - Long '0XF'
   ok 92 - ULong '0XF'
   ok 93 - LLong '0XF'
   ok 94 - ULLong '0XF'
   ok 95 - Float '0XF'
   ok 96 - Double '0XF'
   ok 97 - Long '0x0' in base 10 => extraneous
   ok 98 - ULong '0x0' in base 10 => extraneous
   ok 99 - LLong '0x0' in base 10 => extraneous
   ok 100 - ULLong '0x0' in base 10 => extraneous
   ok 101 - Long '0x10' in base 0
   ok 102 - ULong '0x10' in base 0
   ok 103 - Long '0x10' in base 16
   ok 104 - ULong '0x10' in base 16
   ok 105 - Long '10' in base 16
   ok 106 - ULong '10' in base 16
   ok 107 - Long '0x7fffffff'
   ok 108 - ULong '0xffffffff'
   ok 109 - LLong '0x7fffffffffffffff'
   ok 110 - ULLong '0xffffffffffffffff'
   ok 111 - Float '0xffffff'
   ok 112 - Double '0xffffffff'
   ok 113 - Long '-0x7fffffff'
   ok 114 - ULong '-0x7fffffff'
   ok 115 - LLong '-0x7fffffffffffffff'
   ok 116 - ULLong '-0x7fffffffffffffff'
   ok 117 - Float '-0xffffff'
   ok 118 - Double '-0x7fffffff'
   ok 119 - Int8 '0x7f'
   ok 120 - Int8 '-0x80'
   ok 121 - UInt8 '0xff'
   ok 122 - UInt8 '-1'
   ok 123 - Int8 '0x80' => overflow
   ok 124 - Int8 '-0x81' => overflow
   ok 125 - UInt8 '0x100' => overflow
   ok 126 - UInt8 '-0x100' => overflow
   ok 127 - Int16 '0x7fff'
   ok 128 - Int16 '-0x8000'
   ok 129 - UInt16 '0xffff'
   ok 130 - UInt16 '-1'
   ok 131 - Int16 '0x8000' => overflow
   ok 132 - Int16 '-0x8001' => overflow
   ok 133 - UInt16 '0x10000' => overflow
   ok 134 - UInt16 '-0x10000' => overflow
   ok 135 - Int32 '0x7fffffff'
   ok 136 - Int32 '-0x80000000'
   ok 137 - UInt32 '0xffffffff'
   ok 138 - UInt32 '-1'
   ok 139 - Int32 '0x80000000' => overflow
   ok 140 - Int32 '-0x80000001' => overflow
   ok 141 - UInt32 '0x100000000' => overflow
   ok 142 - UInt32 '-0x100000000' => overflow
   ok 143 - Int64 '0x7fffffffffffffff'
   ok 144 - Int64 '-0x8000000000000000'
   ok 145 - UInt64 '0xffffffffffffffff'
   ok 146 - UInt64 '-1'
   ok 147 - Int64 '0x8000000000000000' => overflow
   ok 148 - Int64 '-0x8000000000000001' => overflow
   ok 149 - UInt64 '0x10000000000000000' => overflow
   ok 150 - UInt64 '-0x10000000000000000' => overflow
   ok 151 - Float '.1'
   ok 152 - Double '.1'
   ok 153 - Float '0.1'
   ok 154 - Double '0.1'
   ok 155 - Float '1e-1'
   ok 156 - Double '1e-1'
   ok 157 - Float '-.1'
   ok 158 - Double '-.1'
   ok 159 - Float '-0.1'
   ok 160 - Double '-0.1'
   ok 161 - Float '-1e-1'
   ok 162 - Double '-1e-1'
   ok 163 - Float '1e-30'
   ok 164 - Double '1e-300'
   ok 165 - Float '1e-40' => underflow
   ok 166 - Double '1e-330' => underflow
   ok 167 - Float '1e30'
   ok 168 - Double '1e300'
   ok 169 - Float '1e40' => overflow
   ok 170 - Double '1e330' => overflow
   ok 171 - Long '2147483647'
   ok 172 - Long '-2147483647'
   ok 173 - ULong '4294967295'
   ok 174 - Float '16777214'
   ok 175 - Float '16777215'
   ok 176 - Float '-16777215'
   ok 177 - Float '-16777216'
   ok 178 - Double '4294967294'
   ok 179 - Double '4294967295'
   ok 180 - Double '-4294967295'
   ok 181 - Double '-4294967296'
   ok 182 - Float 'NAN'
   ok 183 - Double 'NAN'
   ok 184 - Float 'Nan'
   ok 185 - Double 'Nan'
   ok 186 - Float 'nan()' # TODO RTEMS (newlib) parser doesn't recognise 'nan()'
   ok 187 - Double 'nan()' # TODO RTEMS (newlib) parser doesn't recognise 'nan()'
   ok 188 - Float 'INF'
   ok 189 - Double 'INF'
   ok 190 - Float 'Infinity'
   ok 191 - Double 'Infinity'
   ok 192 - Float '+INF'
   ok 193 - Double '+INF'
   ok 194 - Float '+Infinity'
   ok 195 - Double '+Infinity'
   ok 196 - Float '-INF'
   ok 197 - Double '-INF'
   ok 198 - Float '-Infinity'
   ok 199 - Double '-Infinity'
   # This target defines epicsStrtod as strtod

       Results
       =======
          Tests: 199
         Passed: 199 = 100.00%
    Todo Passes:   2 =  1.01%

   ***** epicsStringTest *****
   1..406
   ok  1 - escaped char 0xff -> "\377" (4) -> 0xff
   ok  2 - escaped char 0xfe -> "\376" (4) -> 0xfe
   ok  3 - escaped char 0xfd -> "\375" (4) -> 0xfd
   ok  4 - escaped char 0xfc -> "\374" (4) -> 0xfc
   ok  5 - escaped char 0xfb -> "\373" (4) -> 0xfb
   ok  6 - escaped char 0xfa -> "\372" (4) -> 0xfa
   ok  7 - escaped char 0xf9 -> "\371" (4) -> 0xf9
   ok  8 - escaped char 0xf8 -> "\370" (4) -> 0xf8
   ok  9 - escaped char 0xf7 -> "\367" (4) -> 0xf7
   ok 10 - escaped char 0xf6 -> "\366" (4) -> 0xf6
   ok 11 - escaped char 0xf5 -> "\365" (4) -> 0xf5
   ok 12 - escaped char 0xf4 -> "\364" (4) -> 0xf4
   ok 13 - escaped char 0xf3 -> "\363" (4) -> 0xf3
   ok 14 - escaped char 0xf2 -> "\362" (4) -> 0xf2
   ok 15 - escaped char 0xf1 -> "\361" (4) -> 0xf1
   ok 16 - escaped char 0xf0 -> "\360" (4) -> 0xf0
   ok 17 - escaped char 0xef -> "\357" (4) -> 0xef
   ok 18 - escaped char 0xee -> "\356" (4) -> 0xee
   ok 19 - escaped char 0xed -> "\355" (4) -> 0xed
   ok 20 - escaped char 0xec -> "\354" (4) -> 0xec
   ok 21 - escaped char 0xeb -> "\353" (4) -> 0xeb
   ok 22 - escaped char 0xea -> "\352" (4) -> 0xea
   ok 23 - escaped char 0xe9 -> "\351" (4) -> 0xe9
   ok 24 - escaped char 0xe8 -> "\350" (4) -> 0xe8
   ok 25 - escaped char 0xe7 -> "\347" (4) -> 0xe7
   ok 26 - escaped char 0xe6 -> "\346" (4) -> 0xe6
   ok 27 - escaped char 0xe5 -> "\345" (4) -> 0xe5
   ok 28 - escaped char 0xe4 -> "\344" (4) -> 0xe4
   ok 29 - escaped char 0xe3 -> "\343" (4) -> 0xe3
   ok 30 - escaped char 0xe2 -> "\342" (4) -> 0xe2
   ok 31 - escaped char 0xe1 -> "\341" (4) -> 0xe1
   ok 32 - escaped char 0xe0 -> "\340" (4) -> 0xe0
   ok 33 - escaped char 0xdf -> "\337" (4) -> 0xdf
   ok 34 - escaped char 0xde -> "\336" (4) -> 0xde
   ok 35 - escaped char 0xdd -> "\335" (4) -> 0xdd
   ok 36 - escaped char 0xdc -> "\334" (4) -> 0xdc
   ok 37 - escaped char 0xdb -> "\333" (4) -> 0xdb
   ok 38 - escaped char 0xda -> "\332" (4) -> 0xda
   ok 39 - escaped char 0xd9 -> "\331" (4) -> 0xd9
   ok 40 - escaped char 0xd8 -> "\330" (4) -> 0xd8
   ok 41 - escaped char 0xd7 -> "\327" (4) -> 0xd7
   ok 42 - escaped char 0xd6 -> "\326" (4) -> 0xd6
   ok 43 - escaped char 0xd5 -> "\325" (4) -> 0xd5
   ok 44 - escaped char 0xd4 -> "\324" (4) -> 0xd4
   ok 45 - escaped char 0xd3 -> "\323" (4) -> 0xd3
   ok 46 - escaped char 0xd2 -> "\322" (4) -> 0xd2
   ok 47 - escaped char 0xd1 -> "\321" (4) -> 0xd1
   ok 48 - escaped char 0xd0 -> "\320" (4) -> 0xd0
   ok 49 - escaped char 0xcf -> "\317" (4) -> 0xcf
   ok 50 - escaped char 0xce -> "\316" (4) -> 0xce
   ok 51 - escaped char 0xcd -> "\315" (4) -> 0xcd
   ok 52 - escaped char 0xcc -> "\314" (4) -> 0xcc
   ok 53 - escaped char 0xcb -> "\313" (4) -> 0xcb
   ok 54 - escaped char 0xca -> "\312" (4) -> 0xca
   ok 55 - escaped char 0xc9 -> "\311" (4) -> 0xc9
   ok 56 - escaped char 0xc8 -> "\310" (4) -> 0xc8
   ok 57 - escaped char 0xc7 -> "\307" (4) -> 0xc7
   ok 58 - escaped char 0xc6 -> "\306" (4) -> 0xc6
   ok 59 - escaped char 0xc5 -> "\305" (4) -> 0xc5
   ok 60 - escaped char 0xc4 -> "\304" (4) -> 0xc4
   ok 61 - escaped char 0xc3 -> "\303" (4) -> 0xc3
   ok 62 - escaped char 0xc2 -> "\302" (4) -> 0xc2
   ok 63 - escaped char 0xc1 -> "\301" (4) -> 0xc1
   ok 64 - escaped char 0xc0 -> "\300" (4) -> 0xc0
   ok 65 - escaped char 0xbf -> "\277" (4) -> 0xbf
   ok 66 - escaped char 0xbe -> "\276" (4) -> 0xbe
   ok 67 - escaped char 0xbd -> "\275" (4) -> 0xbd
   ok 68 - escaped char 0xbc -> "\274" (4) -> 0xbc
   ok 69 - escaped char 0xbb -> "\273" (4) -> 0xbb
   ok 70 - escaped char 0xba -> "\272" (4) -> 0xba
   ok 71 - escaped char 0xb9 -> "\271" (4) -> 0xb9
   ok 72 - escaped char 0xb8 -> "\270" (4) -> 0xb8
   ok 73 - escaped char 0xb7 -> "\267" (4) -> 0xb7
   ok 74 - escaped char 0xb6 -> "\266" (4) -> 0xb6
   ok 75 - escaped char 0xb5 -> "\265" (4) -> 0xb5
   ok 76 - escaped char 0xb4 -> "\264" (4) -> 0xb4
   ok 77 - escaped char 0xb3 -> "\263" (4) -> 0xb3
   ok 78 - escaped char 0xb2 -> "\262" (4) -> 0xb2
   ok 79 - escaped char 0xb1 -> "\261" (4) -> 0xb1
   ok 80 - escaped char 0xb0 -> "\260" (4) -> 0xb0
   ok 81 - escaped char 0xaf -> "\257" (4) -> 0xaf
   ok 82 - escaped char 0xae -> "\256" (4) -> 0xae
   ok 83 - escaped char 0xad -> "\255" (4) -> 0xad
   ok 84 - escaped char 0xac -> "\254" (4) -> 0xac
   ok 85 - escaped char 0xab -> "\253" (4) -> 0xab
   ok 86 - escaped char 0xaa -> "\252" (4) -> 0xaa
   ok 87 - escaped char 0xa9 -> "\251" (4) -> 0xa9
   ok 88 - escaped char 0xa8 -> "\250" (4) -> 0xa8
   ok 89 - escaped char 0xa7 -> "\247" (4) -> 0xa7
   ok 90 - escaped char 0xa6 -> "\246" (4) -> 0xa6
   ok 91 - escaped char 0xa5 -> "\245" (4) -> 0xa5
   ok 92 - escaped char 0xa4 -> "\244" (4) -> 0xa4
   ok 93 - escaped char 0xa3 -> "\243" (4) -> 0xa3
   ok 94 - escaped char 0xa2 -> "\242" (4) -> 0xa2
   ok 95 - escaped char 0xa1 -> "\241" (4) -> 0xa1
   ok 96 - escaped char 0xa0 -> "\240" (4) -> 0xa0
   ok 97 - escaped char 0x9f -> "\237" (4) -> 0x9f
   ok 98 - escaped char 0x9e -> "\236" (4) -> 0x9e
   ok 99 - escaped char 0x9d -> "\235" (4) -> 0x9d
   ok 100 - escaped char 0x9c -> "\234" (4) -> 0x9c
   ok 101 - escaped char 0x9b -> "\233" (4) -> 0x9b
   ok 102 - escaped char 0x9a -> "\232" (4) -> 0x9a
   ok 103 - escaped char 0x99 -> "\231" (4) -> 0x99
   ok 104 - escaped char 0x98 -> "\230" (4) -> 0x98
   ok 105 - escaped char 0x97 -> "\227" (4) -> 0x97
   ok 106 - escaped char 0x96 -> "\226" (4) -> 0x96
   ok 107 - escaped char 0x95 -> "\225" (4) -> 0x95
   ok 108 - escaped char 0x94 -> "\224" (4) -> 0x94
   ok 109 - escaped char 0x93 -> "\223" (4) -> 0x93
   ok 110 - escaped char 0x92 -> "\222" (4) -> 0x92
   ok 111 - escaped char 0x91 -> "\221" (4) -> 0x91
   ok 112 - escaped char 0x90 -> "\220" (4) -> 0x90
   ok 113 - escaped char 0x8f -> "\217" (4) -> 0x8f
   ok 114 - escaped char 0x8e -> "\216" (4) -> 0x8e
   ok 115 - escaped char 0x8d -> "\215" (4) -> 0x8d
   ok 116 - escaped char 0x8c -> "\214" (4) -> 0x8c
   ok 117 - escaped char 0x8b -> "\213" (4) -> 0x8b
   ok 118 - escaped char 0x8a -> "\212" (4) -> 0x8a
   ok 119 - escaped char 0x89 -> "\211" (4) -> 0x89
   ok 120 - escaped char 0x88 -> "\210" (4) -> 0x88
   ok 121 - escaped char 0x87 -> "\207" (4) -> 0x87
   ok 122 - escaped char 0x86 -> "\206" (4) -> 0x86
   ok 123 - escaped char 0x85 -> "\205" (4) -> 0x85
   ok 124 - escaped char 0x84 -> "\204" (4) -> 0x84
   ok 125 - escaped char 0x83 -> "\203" (4) -> 0x83
   ok 126 - escaped char 0x82 -> "\202" (4) -> 0x82
   ok 127 - escaped char 0x81 -> "\201" (4) -> 0x81
   ok 128 - escaped char 0x80 -> "\200" (4) -> 0x80
   ok 129 - escaped char 0x7f -> "\177" (4) -> 0x7f
   ok 130 - escaped char 0x7e -> "~" (1) -> 0x7e
   ok 131 - escaped char 0x7d -> "}" (1) -> 0x7d
   ok 132 - escaped char 0x7c -> "|" (1) -> 0x7c
   ok 133 - escaped char 0x7b -> "{" (1) -> 0x7b
   ok 134 - escaped char 0x7a -> "z" (1) -> 0x7a
   ok 135 - escaped char 0x79 -> "y" (1) -> 0x79
   ok 136 - escaped char 0x78 -> "x" (1) -> 0x78
   ok 137 - escaped char 0x77 -> "w" (1) -> 0x77
   ok 138 - escaped char 0x76 -> "v" (1) -> 0x76
   ok 139 - escaped char 0x75 -> "u" (1) -> 0x75
   ok 140 - escaped char 0x74 -> "t" (1) -> 0x74
   ok 141 - escaped char 0x73 -> "s" (1) -> 0x73
   ok 142 - escaped char 0x72 -> "r" (1) -> 0x72
   ok 143 - escaped char 0x71 -> "q" (1) -> 0x71
   ok 144 - escaped char 0x70 -> "p" (1) -> 0x70
   ok 145 - escaped char 0x6f -> "o" (1) -> 0x6f
   ok 146 - escaped char 0x6e -> "n" (1) -> 0x6e
   ok 147 - escaped char 0x6d -> "m" (1) -> 0x6d
   ok 148 - escaped char 0x6c -> "l" (1) -> 0x6c
   ok 149 - escaped char 0x6b -> "k" (1) -> 0x6b
   ok 150 - escaped char 0x6a -> "j" (1) -> 0x6a
   ok 151 - escaped char 0x69 -> "i" (1) -> 0x69
   ok 152 - escaped char 0x68 -> "h" (1) -> 0x68
   ok 153 - escaped char 0x67 -> "g" (1) -> 0x67
   ok 154 - escaped char 0x66 -> "f" (1) -> 0x66
   ok 155 - escaped char 0x65 -> "e" (1) -> 0x65
   ok 156 - escaped char 0x64 -> "d" (1) -> 0x64
   ok 157 - escaped char 0x63 -> "c" (1) -> 0x63
   ok 158 - escaped char 0x62 -> "b" (1) -> 0x62
   ok 159 - escaped char 0x61 -> "a" (1) -> 0x61
   ok 160 - escaped char 0x60 -> "`" (1) -> 0x60
   ok 161 - escaped char 0x5f -> "_" (1) -> 0x5f
   ok 162 - escaped char 0x5e -> "^" (1) -> 0x5e
   ok 163 - escaped char 0x5d -> "]" (1) -> 0x5d
   ok 164 - escaped char 0x5c -> "\\" (2) -> 0x5c
   ok 165 - escaped char 0x5b -> "[" (1) -> 0x5b
   ok 166 - escaped char 0x5a -> "Z" (1) -> 0x5a
   ok 167 - escaped char 0x59 -> "Y" (1) -> 0x59
   ok 168 - escaped char 0x58 -> "X" (1) -> 0x58
   ok 169 - escaped char 0x57 -> "W" (1) -> 0x57
   ok 170 - escaped char 0x56 -> "V" (1) -> 0x56
   ok 171 - escaped char 0x55 -> "U" (1) -> 0x55
   ok 172 - escaped char 0x54 -> "T" (1) -> 0x54
   ok 173 - escaped char 0x53 -> "S" (1) -> 0x53
   ok 174 - escaped char 0x52 -> "R" (1) -> 0x52
   ok 175 - escaped char 0x51 -> "Q" (1) -> 0x51
   ok 176 - escaped char 0x50 -> "P" (1) -> 0x50
   ok 177 - escaped char 0x4f -> "O" (1) -> 0x4f
   ok 178 - escaped char 0x4e -> "N" (1) -> 0x4e
   ok 179 - escaped char 0x4d -> "M" (1) -> 0x4d
   ok 180 - escaped char 0x4c -> "L" (1) -> 0x4c
   ok 181 - escaped char 0x4b -> "K" (1) -> 0x4b
   ok 182 - escaped char 0x4a -> "J" (1) -> 0x4a
   ok 183 - escaped char 0x49 -> "I" (1) -> 0x49
   ok 184 - escaped char 0x48 -> "H" (1) -> 0x48
   ok 185 - escaped char 0x47 -> "G" (1) -> 0x47
   ok 186 - escaped char 0x46 -> "F" (1) -> 0x46
   ok 187 - escaped char 0x45 -> "E" (1) -> 0x45
   ok 188 - escaped char 0x44 -> "D" (1) -> 0x44
   ok 189 - escaped char 0x43 -> "C" (1) -> 0x43
   ok 190 - escaped char 0x42 -> "B" (1) -> 0x42
   ok 191 - escaped char 0x41 -> "A" (1) -> 0x41
   ok 192 - escaped char 0x40 -> "@" (1) -> 0x40
   ok 193 - escaped char 0x3f -> "?" (1) -> 0x3f
   ok 194 - escaped char 0x3e -> ">" (1) -> 0x3e
   ok 195 - escaped char 0x3d -> "=" (1) -> 0x3d
   ok 196 - escaped char 0x3c -> "<" (1) -> 0x3c
   ok 197 - escaped char 0x3b -> ";" (1) -> 0x3b
   ok 198 - escaped char 0x3a -> ":" (1) -> 0x3a
   ok 199 - escaped char 0x39 -> "9" (1) -> 0x39
   ok 200 - escaped char 0x38 -> "8" (1) -> 0x38
   ok 201 - escaped char 0x37 -> "7" (1) -> 0x37
   ok 202 - escaped char 0x36 -> "6" (1) -> 0x36
   ok 203 - escaped char 0x35 -> "5" (1) -> 0x35
   ok 204 - escaped char 0x34 -> "4" (1) -> 0x34
   ok 205 - escaped char 0x33 -> "3" (1) -> 0x33
   ok 206 - escaped char 0x32 -> "2" (1) -> 0x32
   ok 207 - escaped char 0x31 -> "1" (1) -> 0x31
   ok 208 - escaped char 0x30 -> "0" (1) -> 0x30
   ok 209 - escaped char 0x2f -> "/" (1) -> 0x2f
   ok 210 - escaped char 0x2e -> "." (1) -> 0x2e
   ok 211 - escaped char 0x2d -> "-" (1) -> 0x2d
   ok 212 - escaped char 0x2c -> "," (1) -> 0x2c
   ok 213 - escaped char 0x2b -> "+" (1) -> 0x2b
   ok 214 - escaped char 0x2a -> "*" (1) -> 0x2a
   ok 215 - escaped char 0x29 -> ")" (1) -> 0x29
   ok 216 - escaped char 0x28 -> "(" (1) -> 0x28
   ok 217 - escaped char 0x27 -> "\'" (2) -> 0x27
   ok 218 - escaped char 0x26 -> "&" (1) -> 0x26
   ok 219 - escaped char 0x25 -> "%" (1) -> 0x25
   ok 220 - escaped char 0x24 -> "$" (1) -> 0x24
   ok 221 - escaped char 0x23 -> "#" (1) -> 0x23
   ok 222 - escaped char 0x22 -> "\"" (2) -> 0x22
   ok 223 - escaped char 0x21 -> "!" (1) -> 0x21
   ok 224 - escaped char 0x20 -> " " (1) -> 0x20
   ok 225 - escaped char 0x1f -> "\037" (4) -> 0x1f
   ok 226 - escaped char 0x1e -> "\036" (4) -> 0x1e
   ok 227 - escaped char 0x1d -> "\035" (4) -> 0x1d
   ok 228 - escaped char 0x1c -> "\034" (4) -> 0x1c
   ok 229 - escaped char 0x1b -> "\033" (4) -> 0x1b
   ok 230 - escaped char 0x1a -> "\032" (4) -> 0x1a
   ok 231 - escaped char 0x19 -> "\031" (4) -> 0x19
   ok 232 - escaped char 0x18 -> "\030" (4) -> 0x18
   ok 233 - escaped char 0x17 -> "\027" (4) -> 0x17
   ok 234 - escaped char 0x16 -> "\026" (4) -> 0x16
   ok 235 - escaped char 0x15 -> "\025" (4) -> 0x15
   ok 236 - escaped char 0x14 -> "\024" (4) -> 0x14
   ok 237 - escaped char 0x13 -> "\023" (4) -> 0x13
   ok 238 - escaped char 0x12 -> "\022" (4) -> 0x12
   ok 239 - escaped char 0x11 -> "\021" (4) -> 0x11
   ok 240 - escaped char 0x10 -> "\020" (4) -> 0x10
   ok 241 - escaped char 0x0f -> "\017" (4) -> 0x0f
   ok 242 - escaped char 0x0e -> "\016" (4) -> 0x0e
   ok 243 - escaped char 0x0d -> "\r" (2) -> 0x0d
   ok 244 - escaped char 0x0c -> "\f" (2) -> 0x0c
   ok 245 - escaped char 0x0b -> "\v" (2) -> 0x0b
   ok 246 - escaped char 0x0a -> "\n" (2) -> 0x0a
   ok 247 - escaped char 0x09 -> "\t" (2) -> 0x09
   ok 248 - escaped char 0x08 -> "\b" (2) -> 0x08
   ok 249 - escaped char 0x07 -> "\a" (2) -> 0x07
   ok 250 - escaped char 0x06 -> "\006" (4) -> 0x06
   ok 251 - escaped char 0x05 -> "\005" (4) -> 0x05
   ok 252 - escaped char 0x04 -> "\004" (4) -> 0x04
   ok 253 - escaped char 0x03 -> "\003" (4) -> 0x03
   ok 254 - escaped char 0x02 -> "\002" (4) -> 0x02
   ok 255 - escaped char 0x01 -> "\001" (4) -> 0x01
   ok 256 - escaped char 0x00 -> "\000" (4) -> 0x00
   ok 257 - epicsStrnCaseCmp(empty, "", 0) == 0
   ok 258 - epicsStrnCaseCmp(empty, "", 1) == 0
   ok 259 - epicsStrnCaseCmp(space, empty, 1) > 0
   ok 260 - epicsStrnCaseCmp(empty, space, 1) < 0
   ok 261 - epicsStrnCaseCmp(a, A, 1) == 0
   ok 262 - epicsStrnCaseCmp(a, A, 2) == 0
   ok 263 - epicsStrnCaseCmp(abcd, ABCD, 2) == 0
   ok 264 - epicsStrnCaseCmp(abcd, ABCD, 4) == 0
   ok 265 - epicsStrnCaseCmp(abcd, ABCD, 1000) == 0
   ok 266 - epicsStrnCaseCmp(abcd, ABCDE, 2) == 0
   ok 267 - epicsStrnCaseCmp(abcd, ABCDE, 4) == 0
   ok 268 - epicsStrnCaseCmp(abcd, ABCDE, 1000) < 0
   ok 269 - epicsStrnCaseCmp(abcde, ABCD, 2) == 0
   ok 270 - epicsStrnCaseCmp(abcde, ABCD, 4) == 0
   ok 271 - epicsStrnCaseCmp(abcde, ABCD, 1000) > 0
   ok 272 - epicsStrCaseCmp(empty, "") == 0
   ok 273 - epicsStrCaseCmp(a, A) == 0
   ok 274 - epicsStrCaseCmp(abcd, ABCD) == 0
   ok 275 - epicsStrCaseCmp(abcd, ABCDE) < 0
   ok 276 - epicsStrCaseCmp(abcde, ABCD) > 0
   ok 277 - epicsStrCaseCmp(abcde, "ABCDF") < 0
   ok 278 - epicsStrDup
   ok 279 - epicsStrHash(abcd, 0) != epicsStrHash("bacd", 0)
   ok 280 - epicsStrHash(abcd, 0) == epicsMemHash(abcde, 4, 0)
   ok 281 - epicsStrHash(abcd, 0) != epicsMemHash("abcd\0", 5, 0)
   ok 282 - epicsStrnLen("abcd", 5)==4
   ok 283 - epicsStrnLen("abcd", 4)==4
   ok 284 - epicsStrnLen("abcd", 3)==3
   ok 285 - epicsStrnLen("abcd", 0)==0
   ok 286 - epicsStrGlobMatch("xyz","xyz")
   ok 287 - !epicsStrGlobMatch("xyz","xyzm")
   ok 288 - !epicsStrGlobMatch("xyzm","xyz")
   ok 289 - !epicsStrGlobMatch("","xyzm")
   ok 290 - !epicsStrGlobMatch("xyz","")
   ok 291 - epicsStrGlobMatch("","")
   ok 292 - epicsStrGlobMatch("","*")
   ok 293 - !epicsStrGlobMatch("","?")
   ok 294 - !epicsStrGlobMatch("","?*")
   ok 295 - epicsStrGlobMatch("hello","h*o")
   ok 296 - !epicsStrGlobMatch("hello","h*x")
   ok 297 - !epicsStrGlobMatch("hellx","h*o")
   ok 298 - epicsStrGlobMatch("hello","he?lo")
   ok 299 - !epicsStrGlobMatch("hello","he?xo")
   ok 300 - epicsStrGlobMatch("hello","he??o")
   ok 301 - !epicsStrGlobMatch("helllo","he?lo")
   ok 302 - epicsStrGlobMatch("hello world","he*o w*d")
   ok 303 - !epicsStrGlobMatch("hello_world","he*o w*d")
   ok 304 - epicsStrGlobMatch("hello world","he**d")
   ok 305 - epicsStrGlobMatch("hello hello world","he*o w*d")
   ok 306 - !epicsStrGlobMatch("hello hello xorld","he*o w*d")
   ok 307 - epicsStrGlobMatch("hello","he*")
   ok 308 - epicsStrGlobMatch("hello","*lo")
   ok 309 - epicsStrGlobMatch("hello","*")
   ok 310 - epicsStrnEscapedFromRaw(out, 0) -> 4 (exp. 4)
   ok 311 -   No output
   ok 312 - epicsStrnRawFromEscaped(out, 0) -> 0 (exp. 0)
   ok 313 -   No output
   ok 314 - epicsStrnEscapedFromRaw(out, 1) -> 4 (exp. 4)
   ok 315 -   0-terminated
   ok 316 -   No overrun
   ok 317 - epicsStrnRawFromEscaped(out, 1) -> 0 (exp. 0)
   ok 318 -   0-terminated
   ok 319 -   No overrun
   # Testing size = epicsStrnEscapedFromRawSize
   ok 320 - size("ABCD", 3) -> 3 (exp. 3)
   ok 321 - size("ABCD", 4) -> 4 (exp. 4)
   ok 322 - size("ABCD", 5) -> 8 (exp. 8)
   # Testing esc = epicsStrnEscapedFromRaw(out, 4, ...)
   ok 323 - esc("ABCD", 3) -> 3 (exp. 3)
   ok 324 -   0-terminated
   ok 325 -   No overrun
   ok 326 - esc("ABCD", 4) -> 4 (exp. 4)
   ok 327 -   0-terminated
   ok 328 -   No overrun
   ok 329 - esc("ABCD", 5) -> 8 (exp. 8)
   ok 330 -   0-terminated
   ok 331 -   No overrun
   # Testing raw = epicsStrnRawFromEscaped(out, 4, ...)
   ok 332 - raw("ABCD", 0) -> 0 (exp. 0)
   ok 333 -   0-terminated
   ok 334 - raw("ABCD", 1) -> 1 (exp. 1)
   ok 335 -   Char 'A' (exp. 'A')
   ok 336 -   0-terminated
   ok 337 - raw("ABCD", 2) -> 2 (exp. 2)
   ok 338 -   Char 'A' (exp. 'A')
   ok 339 -   Char 'B' (exp. 'B')
   ok 340 -   0-terminated
   ok 341 - raw("ABCD", 3) -> 3 (exp. 3)
   ok 342 -   Char 'A' (exp. 'A')
   ok 343 -   Char 'B' (exp. 'B')
   ok 344 -   Char 'C' (exp. 'C')
   ok 345 -   0-terminated
   ok 346 -   No write outside buffer
   ok 347 - raw("ABCD", 4) -> 3 (exp. 3)
   ok 348 -   Char 'A' (exp. 'A')
   ok 349 -   Char 'B' (exp. 'B')
   ok 350 -   Char 'C' (exp. 'C')
   ok 351 -   0-terminated
   ok 352 -   No write outside buffer
   ok 353 - raw("ABCDE", 5) -> 3 (exp. 3)
   ok 354 -   Char 'A' (exp. 'A')
   ok 355 -   Char 'B' (exp. 'B')
   ok 356 -   Char 'C' (exp. 'C')
   ok 357 -   0-terminated
   ok 358 -   No write outside buffer
   ok 359 - raw("A", 2) -> 1 (exp. 1)
   ok 360 -   Char 'A' (exp. 'A')
   ok 361 -   0-terminated
   ok 362 - raw("\123", 1) -> 0 (exp. 0)
   ok 363 -   0-terminated
   ok 364 - raw("\123", 2) -> 1 (exp. 1)
   ok 365 -   Octal escape (got \001)
   ok 366 -   0-terminated
   ok 367 - raw("\123", 3) -> 1 (exp. 1)
   ok 368 -   Octal escape (got \012)
   ok 369 -   0-terminated
   ok 370 - raw("\123", 4) -> 1 (exp. 1)
   ok 371 -   Octal escape (got \123)
   ok 372 -   0-terminated
   ok 373 - raw("\812", 2) -> 1 (exp. 1)
   ok 374 -   Escaped '8')
   ok 375 -   0-terminated
   ok 376 - raw("\182", 3) -> 2 (exp. 2)
   ok 377 -   Octal escape (got \001)
   ok 378 -   Terminated with '8'
   ok 379 -   0-terminated
   ok 380 - raw("\128", 4) -> 2 (exp. 2)
   ok 381 -   Octal escape (got \012)
   ok 382 -   Terminator char got '8'
   ok 383 -   0-terminated
   ok 384 - raw("\x12", 1) -> 0 (exp. 0)
   ok 385 -   0-terminated
   ok 386 - raw("\x12", 2) -> 0 (exp. 0)
   ok 387 -   0-terminated
   ok 388 - raw("\x12", 3) -> 1 (exp. 1)
   ok 389 -   Hex escape (got \x1)
   ok 390 -   0-terminated
   ok 391 - raw("\x12", 4) -> 1 (exp. 1)
   ok 392 -   Hex escape (got \x12)
   ok 393 -   0-terminated
   ok 394 - raw("\xaF", 4) -> 1 (exp. 1)
   ok 395 -   Hex escape (got \xaf)
   ok 396 -   0-terminated
   ok 397 - raw("\x012", 5) -> 1 (exp. 1)
   ok 398 -   Hex escape (got \x12)
   ok 399 -   0-terminated
   ok 400 - raw("\x0012", 6) -> 1 (exp. 1)
   ok 401 -   Hex escape (got \x12)
   ok 402 -   0-terminated
   ok 403 - raw("\x1g", 4) -> 2 (exp. 2)
   ok 404 -   Hex escape (got \x1)
   ok 405 -   Terminator char got 'g'
   ok 406 -   0-terminated

       Results
       =======
          Tests: 406
         Passed: 406 = 100.00%

   ***** epicsThreadHooksTest *****
   1..9
   ok  1 - All my tasks covered once by epicsThreadMap
   ok  2 - All hooks for task 0 called in correct order
   ok  3 - All hooks for task 1 called in correct order
   ok  4 - All hooks for task 2 called in correct order
   ok  5 - All hooks for task 3 called in correct order
   ok  6 - All hooks for task 4 called in correct order
   ok  7 - All hooks for task 5 called in correct order
   ok  8 - All hooks for task 6 called in correct order
   ok  9 - All hooks for task 7 called in correct order

       Results
       =======
          Tests: 9
         Passed:   9 = 100.00%

   ***** epicsThreadOnceTest *****
   1..11
   ok  1 - runCount = 8
   ok  2 - once-0: initCount = 1
   ok  3 - once-1: initCount = 1
   ok  4 - once-2: initCount = 1
   ok  5 - once-3: initCount = 1
   ok  6 - once-4: initCount = 1
   ok  7 - once-5: initCount = 1
   ok  8 - once-6: initCount = 1
   ok  9 - once-7: initCount = 1
   ok 10 - doneCount = 8
   # init was run by once-0
   ok 11 - Recursive epicsThreadOnce() detected

       Results
       =======
          Tests: 11
         Passed:  11 = 100.00%

   ***** epicsThreadPoolTest *****
   1..171
   # nullop()
   ok  1 - conf.maxThreads>0
   ok  2 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # oneop()
   ok  3 - conf.maxThreads>0
   ok  4 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # Queue with delayed start
   # postjobs(1,1)
   ok  5 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok  6 - priv->job[i]!=NULL
   ok  7 - epicsJobQueue(priv->job[i])==0
   ok  8 - priv->count==mcnt
   ok  9 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   # Waiting for all jobs to start
   # Job 1
   # All jobs running
   # Stop all
   # i=0
   # postjobs(0,1)
   ok 10 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok 11 - priv->job[i]!=NULL
   ok 12 - epicsJobQueue(priv->job[i])==0
   ok 13 - priv->count==mcnt
   ok 14 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   # Waiting for all jobs to start
   # Job 1
   # All jobs running
   # Stop all
   # i=0
   # postjobs(4,4)
   ok 15 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok 16 - priv->job[i]!=NULL
   ok 17 - epicsJobQueue(priv->job[i])==0
   # i=1
   ok 18 - priv->job[i]!=NULL
   ok 19 - epicsJobQueue(priv->job[i])==0
   # i=2
   ok 20 - priv->job[i]!=NULL
   ok 21 - epicsJobQueue(priv->job[i])==0
   # i=3
   ok 22 - priv->job[i]!=NULL
   ok 23 - epicsJobQueue(priv->job[i])==0
   ok 24 - priv->count==mcnt
   ok 25 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 26 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 27 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 28 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   # Waiting for all jobs to start
   # Job 4
   # Job 3
   # Job 2
   # Job 1
   # All jobs running
   # Stop all
   # i=0
   # i=1
   # i=2
   # i=3
   # postjobs(0,4)
   ok 29 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok 30 - priv->job[i]!=NULL
   ok 31 - epicsJobQueue(priv->job[i])==0
   # i=1
   ok 32 - priv->job[i]!=NULL
   ok 33 - epicsJobQueue(priv->job[i])==0
   # i=2
   ok 34 - priv->job[i]!=NULL
   ok 35 - epicsJobQueue(priv->job[i])==0
   # i=3
   ok 36 - priv->job[i]!=NULL
   ok 37 - epicsJobQueue(priv->job[i])==0
   ok 38 - priv->count==mcnt
   ok 39 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 40 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 41 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 42 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   # Waiting for all jobs to start
   # Job 4
   # Job 3
   # Job 2
   # Job 1
   # All jobs running
   # Stop all
   # i=0
   # i=1
   # i=2
   # i=3
   # postjobs(2,4)
   ok 43 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok 44 - priv->job[i]!=NULL
   ok 45 - epicsJobQueue(priv->job[i])==0
   # i=1
   ok 46 - priv->job[i]!=NULL
   ok 47 - epicsJobQueue(priv->job[i])==0
   # i=2
   ok 48 - priv->job[i]!=NULL
   ok 49 - epicsJobQueue(priv->job[i])==0
   # i=3
   ok 50 - priv->job[i]!=NULL
   ok 51 - epicsJobQueue(priv->job[i])==0
   ok 52 - priv->count==mcnt
   ok 53 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 54 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 55 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 56 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   # Waiting for all jobs to start
   # Job 4
   # Job 3
   # Job 2
   # Job 1
   # All jobs running
   # Stop all
   # i=0
   # i=1
   # i=2
   # i=3
   # Queue with immediate start
   # postjobs(1,1)
   ok 57 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok 58 - priv->job[i]!=NULL
   ok 59 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 60 - epicsJobQueue(priv->job[i])==0
   # Job 1
   # Waiting for all jobs to start
   # All jobs running
   # Stop all
   # i=0
   # postjobs(0,1)
   ok 61 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok 62 - priv->job[i]!=NULL
   ok 63 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 64 - epicsJobQueue(priv->job[i])==0
   # Job 1
   # Waiting for all jobs to start
   # All jobs running
   # Stop all
   # i=0
   # postjobs(4,4)
   ok 65 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok 66 - priv->job[i]!=NULL
   ok 67 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 68 - epicsJobQueue(priv->job[i])==0
   # Job 4
   # i=1
   ok 69 - priv->job[i]!=NULL
   ok 70 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 71 - epicsJobQueue(priv->job[i])==0
   # Job 3
   # i=2
   ok 72 - priv->job[i]!=NULL
   ok 73 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 74 - epicsJobQueue(priv->job[i])==0
   # Job 2
   # i=3
   ok 75 - priv->job[i]!=NULL
   ok 76 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 77 - epicsJobQueue(priv->job[i])==0
   # Job 1
   # Waiting for all jobs to start
   # All jobs running
   # Stop all
   # i=0
   # i=1
   # i=2
   # i=3
   # postjobs(0,4)
   ok 78 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok 79 - priv->job[i]!=NULL
   ok 80 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 81 - epicsJobQueue(priv->job[i])==0
   # Job 4
   # i=1
   ok 82 - priv->job[i]!=NULL
   ok 83 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 84 - epicsJobQueue(priv->job[i])==0
   # Job 3
   # i=2
   ok 85 - priv->job[i]!=NULL
   ok 86 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 87 - epicsJobQueue(priv->job[i])==0
   # Job 2
   # i=3
   ok 88 - priv->job[i]!=NULL
   ok 89 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 90 - epicsJobQueue(priv->job[i])==0
   # Job 1
   # Waiting for all jobs to start
   # All jobs running
   # Stop all
   # i=0
   # i=1
   # i=2
   # i=3
   # postjobs(2,4)
   ok 91 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   # i=0
   ok 92 - priv->job[i]!=NULL
   ok 93 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 94 - epicsJobQueue(priv->job[i])==0
   # Job 4
   # i=1
   ok 95 - priv->job[i]!=NULL
   ok 96 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 97 - epicsJobQueue(priv->job[i])==0
   # Job 3
   # i=2
   ok 98 - priv->job[i]!=NULL
   ok 99 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 100 - epicsJobQueue(priv->job[i])==0
   # Job 2
   # i=3
   ok 101 - priv->job[i]!=NULL
   ok 102 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 103 - epicsJobQueue(priv->job[i])==0
   # Job 1
   # Waiting for all jobs to start
   # All jobs running
   # Stop all
   # i=0
   # i=1
   # i=2
   # i=3
   # testcleanup()
   ok 104 - (pool=epicsThreadPoolCreate(NULL))!=NULL
   ok 105 - (job[0]=epicsJobCreate(pool, cleanupjobs[0], EPICSJOB_SELF))!=NULL
   ok 106 - (job[1]=epicsJobCreate(pool, cleanupjobs[1], EPICSJOB_SELF))!=NULL
   ok 107 - (job[2]=epicsJobCreate(pool, cleanupjobs[2], EPICSJOB_SELF))!=NULL
   ok 108 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 109 - epicsJobQueue(job[i])==0
   ok 110 - epicsJobQueue(job)==0
   ok 111 - epicsJobQueue(job[i])==0
   ok 112 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 113 - epicsJobQueue(job[i])==0
   ok 114 - epicsJobQueue(job)==0
   ok 115 - epicsJobUnqueue(job)==0
   ok 116 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 117 - epicsJobUnqueue(job)==S_pool_jobIdle
   ok 118 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   # testreadd
   ok 119 - (pool=epicsThreadPoolCreate(&conf))!=NULL
   ok 120 - (priv->job=epicsJobCreate(pool, &readdjob, priv))!=NULL
   ok 121 - (priv2->job=epicsJobCreate(pool, &readdjob, priv2))!=NULL
   ok 122 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 123 - epicsJobQueue(priv->job)==0
   ok 124 - priv->inprogress==0
   ok 125 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 126 - epicsJobQueue(priv2->job)==0
   # count==5
   ok 127 - priv->inprogress==0
   # count==5
   ok 128 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 129 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 130 - priv->inprogress==0
   ok 131 - priv->inprogress==0
   # count==4
   # count==4
   ok 132 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 133 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 134 - priv->inprogress==0
   ok 135 - priv->inprogress==0
   # count==3
   # count==3
   ok 136 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 137 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 138 - priv->inprogress==0
   ok 139 - priv->inprogress==0
   # count==2
   # count==2
   ok 140 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 141 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 142 - priv->inprogress==0
   ok 143 - priv->inprogress==0
   # count==1
   # count==1
   ok 144 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 145 - mode==epicsJobModeRun||mode==epicsJobModeCleanup
   ok 146 - priv->inprogress==0
   ok 147 - priv->inprogress==0
   # count==0
   # count==0
   ok 148 - epicsThreadPoolNThreads(pool)==2
   # epicsThreadPoolNThreads = 2
   ok 149 - (pool=epicsThreadPoolCreate(NULL))!=NULL
   ok 150 - (job[0]=epicsJobCreate(pool, &neverrun, EPICSJOB_SELF))!=NULL
   ok 151 - (job[1]=epicsJobCreate(pool, &toolate, EPICSJOB_SELF))!=NULL
   ok 152 - epicsJobUnqueue(job[0])==S_pool_jobIdle
   ok 153 - epicsJobUnqueue(job[0])==0
   ok 154 - epicsJobUnqueue(job[0])==S_pool_jobIdle
   ok 155 - epicsJobUnqueue(job[0])==0
   ok 156 - epicsJobUnqueue(job[0])==S_pool_jobIdle
   ok 157 - Job runs
   ok 158 - epicsJobUnqueue(job[0])==S_pool_jobIdle
   ok 159 - mode==epicsJobModeCleanup
   ok 160 - shouldneverrun==0
   ok 161 - numtoolate==1
   # Check reference counting of shared pools
   ok 162 - (poolA=epicsThreadPoolGetShared(&conf))!=NULL
   ok 163 - poolA->sharedCount==1
   ok 164 - (poolB=epicsThreadPoolGetShared(&conf))!=NULL
   ok 165 - poolA==poolB
   ok 166 - poolA->sharedCount==2
   ok 167 - poolB->sharedCount==1
   ok 168 - (job=epicsJobCreate(poolB, &lastjob, EPICSJOB_SELF))!=NULL
   ok 169 - sharedWasDeleted==1
   ok 170 - (poolA=epicsThreadPoolGetShared(&conf))!=NULL
   ok 171 - poolA->sharedCount==1

       Results
       =======
          Tests: 171
         Passed: 171 = 100.00%

   ***** epicsThreadPriorityTest *****
   1..7
   ok  1 - task 0xd0bc28 epicsEventWait returned 0
   ok  2 - epicsEventWaitWithTimeout returned 0
   ok  3 - task 0xd0bc28 epicsEventWait returned 0
   ok  4 - epicsEventWaitWithTimeout returned 0
   ok  5 - task 0xd0bc28 epicsEventWait returned 0
   # No strict priority scheduler
   ok  6 - epicsEventWaitWithTimeout returned 0
   ok  7 - epicsEventWait returned 0

       Results
       =======
          Tests: 7
         Passed:   7 = 100.00%

   ***** epicsThreadPrivateTest *****
   1..5
   ok  1 - &var == priv.get()
   ok  2 - NULL == priv.get ()
   ok  3 - &var == priv.get ()
   ok  4 - &var == priv.get()
   ok  5 - NULL == priv.get()

       Results
       =======
          Tests: 5
         Passed:   5 = 100.00%

   ***** epicsTimeTest *****
   1..212
   ok  1 - epicsTime_gmtime() for EPICS epoch
   ok  2 - nanosecond overflow throws
   ok  3 - undefined => '<undefined>'
   ok  4 - '%Y-%m-%d %S.%09f' => '1990-01-01 00.098765432'
   ok  5 - '%S.%03f' => '00.099'
   ok  6 - '%S.%04f' => '00.0988'
   ok  7 - '%S.%05f' => '00.09877'
   ok  8 - '%S.%05f %S.%05f' => '00.09877 00.09877'
   ok  9 - '%S.%05f' => '00.*'
   ok 10 - 0.998765 => '00.999'
   ok 11 - 0.999765 => '00.999'
   ok 12 - '%%S.%%05f' => '%S.%05f'
   ok 13 - bad format => '<invalid format>'
   ok 14 - default time provider
   ok 15 - diff <= precisionEPICS + precisionNTP
   # Running 10 loops
   # 100000 calls to epicsTime::getCurrent() averaged  0.274 usec each
   ok 16 - copy == now
   ok 17 - copy <= now
   ok 18 - copy >= now
   ok 19 - now > begin
   ok 20 - now >= begin
   ok 21 - begin != now
   ok 22 - begin < now
   ok 23 - begin <= now
   ok 24 - now - now == 0
   ok 25 - now - begin ~= diff
   ok 26 - begin + 0 == begin
   ok 27 - begin + diff == now
   ok 28 - now - 0 == now
   ok 29 - now - diff == begin
   ok 30 - (begin += diff) == now
   ok 31 - (now -= diff) == begin
   ok 32 - beginANSI + diff == now
   ok 33 - beginGMANSI + diff == now
   ok 34 - beginTS + diff == now
   ok 35 - copy == now
   ok 36 - copy <= now
   ok 37 - copy >= now
   ok 38 - now > begin
   ok 39 - now >= begin
   ok 40 - begin != now
   ok 41 - begin < now
   ok 42 - begin <= now
   ok 43 - now - now == 0
   ok 44 - now - begin ~= diff
   ok 45 - begin + 0 == begin
   ok 46 - begin + diff == now
   ok 47 - now - 0 == now
   ok 48 - now - diff == begin
   ok 49 - (begin += diff) == now
   ok 50 - (now -= diff) == begin
   ok 51 - beginANSI + diff == now
   ok 52 - beginGMANSI + diff == now
   ok 53 - beginTS + diff == now
   ok 54 - copy == now
   ok 55 - copy <= now
   ok 56 - copy >= now
   ok 57 - now > begin
   ok 58 - now >= begin
   ok 59 - begin != now
   ok 60 - begin < now
   ok 61 - begin <= now
   ok 62 - now - now == 0
   ok 63 - now - begin ~= diff
   ok 64 - begin + 0 == begin
   ok 65 - begin + diff == now
   ok 66 - now - 0 == now
   ok 67 - now - diff == begin
   ok 68 - (begin += diff) == now
   ok 69 - (now -= diff) == begin
   ok 70 - beginANSI + diff == now
   ok 71 - beginGMANSI + diff == now
   ok 72 - beginTS + diff == now
   ok 73 - copy == now
   ok 74 - copy <= now
   ok 75 - copy >= now
   ok 76 - now > begin
   ok 77 - now >= begin
   ok 78 - begin != now
   ok 79 - begin < now
   ok 80 - begin <= now
   ok 81 - now - now == 0
   ok 82 - now - begin ~= diff
   ok 83 - begin + 0 == begin
   ok 84 - begin + diff == now
   ok 85 - now - 0 == now
   ok 86 - now - diff == begin
   ok 87 - (begin += diff) == now
   ok 88 - (now -= diff) == begin
   ok 89 - beginANSI + diff == now
   ok 90 - beginGMANSI + diff == now
   ok 91 - beginTS + diff == now
   ok 92 - copy == now
   ok 93 - copy <= now
   ok 94 - copy >= now
   ok 95 - now > begin
   ok 96 - now >= begin
   ok 97 - begin != now
   ok 98 - begin < now
   ok 99 - begin <= now
   ok 100 - now - now == 0
   ok 101 - now - begin ~= diff
   ok 102 - begin + 0 == begin
   ok 103 - begin + diff == now
   ok 104 - now - 0 == now
   ok 105 - now - diff == begin
   ok 106 - (begin += diff) == now
   ok 107 - (now -= diff) == begin
   ok 108 - beginANSI + diff == now
   ok 109 - beginGMANSI + diff == now
   ok 110 - beginTS + diff == now
   ok 111 - copy == now
   ok 112 - copy <= now
   ok 113 - copy >= now
   ok 114 - now > begin
   ok 115 - now >= begin
   ok 116 - begin != now
   ok 117 - begin < now
   ok 118 - begin <= now
   ok 119 - now - now == 0
   ok 120 - now - begin ~= diff
   ok 121 - begin + 0 == begin
   ok 122 - begin + diff == now
   ok 123 - now - 0 == now
   ok 124 - now - diff == begin
   ok 125 - (begin += diff) == now
   ok 126 - (now -= diff) == begin
   ok 127 - beginANSI + diff == now
   ok 128 - beginGMANSI + diff == now
   ok 129 - beginTS + diff == now
   ok 130 - copy == now
   ok 131 - copy <= now
   ok 132 - copy >= now
   ok 133 - now > begin
   ok 134 - now >= begin
   ok 135 - begin != now
   ok 136 - begin < now
   ok 137 - begin <= now
   ok 138 - now - now == 0
   ok 139 - now - begin ~= diff
   ok 140 - begin + 0 == begin
   ok 141 - begin + diff == now
   ok 142 - now - 0 == now
   ok 143 - now - diff == begin
   ok 144 - (begin += diff) == now
   ok 145 - (now -= diff) == begin
   ok 146 - beginANSI + diff == now
   ok 147 - beginGMANSI + diff == now
   ok 148 - beginTS + diff == now
   ok 149 - copy == now
   ok 150 - copy <= now
   ok 151 - copy >= now
   ok 152 - now > begin
   ok 153 - now >= begin
   ok 154 - begin != now
   ok 155 - begin < now
   ok 156 - begin <= now
   ok 157 - now - now == 0
   ok 158 - now - begin ~= diff
   ok 159 - begin + 0 == begin
   ok 160 - begin + diff == now
   ok 161 - now - 0 == now
   ok 162 - now - diff == begin
   ok 163 - (begin += diff) == now
   ok 164 - (now -= diff) == begin
   ok 165 - beginANSI + diff == now
   ok 166 - beginGMANSI + diff == now
   ok 167 - beginTS + diff == now
   ok 168 - copy == now
   ok 169 - copy <= now
   ok 170 - copy >= now
   ok 171 - now > begin
   ok 172 - now >= begin
   ok 173 - begin != now
   ok 174 - begin < now
   ok 175 - begin <= now
   ok 176 - now - now == 0
   ok 177 - now - begin ~= diff
   ok 178 - begin + 0 == begin
   ok 179 - begin + diff == now
   ok 180 - now - 0 == now
   ok 181 - now - diff == begin
   ok 182 - (begin += diff) == now
   ok 183 - (now -= diff) == begin
   ok 184 - beginANSI + diff == now
   ok 185 - beginGMANSI + diff == now
   ok 186 - beginTS + diff == now
   ok 187 - copy == now
   ok 188 - copy <= now
   ok 189 - copy >= now
   ok 190 - now > begin
   ok 191 - now >= begin
   ok 192 - begin != now
   ok 193 - begin < now
   ok 194 - begin <= now
   ok 195 - now - now == 0
   ok 196 - now - begin ~= diff
   ok 197 - begin + 0 == begin
   ok 198 - begin + diff == now
   ok 199 - now - 0 == now
   ok 200 - now - diff == begin
   ok 201 - (begin += diff) == now
   ok 202 - (now -= diff) == begin
   ok 203 - beginANSI + diff == now
   ok 204 - beginGMANSI + diff == now
   ok 205 - beginTS + diff == now
   ok 206 - epicsTime can represent 10 years hence
   ok 207 - OS time_t can represent 10 years hence
   ok 208 - crossCheck(2.100000) actual 2.100086 (-0.004117 %)
   ok 209 - crossCheck(0.100000) actual 0.109977 (-9.976731 %)
   ok 210 - crossCheck(0.020000) actual 0.019983 (0.087245 %)
   ok 211 - crossCheck(0.020000) actual 0.010489 (47.555650 %)
   ok 212 - crossCheck(0.020000) actual 0.016946 (15.270245 %)
   # Resolution 10000000 ns
   # epicsThreadSleep(0.0) Delta 6320219 ns
   # Small Delta 120 ns

       Results
       =======
          Tests: 212
         Passed: 212 = 100.00%

   ***** epicsTimeZoneTest *****
   1..160
   # POSIX 1445259616
   # TZ = "EST5EDT"
   # test_localtime(1445259616, ...)
   ok  1 - epicsTime_localtime() success
   ok  2 - sec 16==16
   ok  3 - min 0==0
   ok  4 - hour 9==9
   ok  5 - mday 19==19
   ok  6 - mon 9==9
   ok  7 - year 2015==2015
   ok  8 - wday 1==1
   ok  9 - yday 291==291
   ok 10 - isdst 1==1
   # test_gmtime(1445259616, ...)
   ok 11 - epicsTime_localtime() success
   ok 12 - sec 16==16
   ok 13 - min 0==0
   ok 14 - hour 13==13
   ok 15 - mday 19==19
   ok 16 - mon 9==9
   ok 17 - year 2015==2015
   ok 18 - wday 1==1
   ok 19 - yday 291==291
   ok 20 - isdst 0==0
   # TZ = "CST6CDT"
   # test_localtime(1445259616, ...)
   ok 21 - epicsTime_localtime() success
   ok 22 - sec 16==16
   ok 23 - min 0==0
   ok 24 - hour 8==8
   ok 25 - mday 19==19
   ok 26 - mon 9==9
   ok 27 - year 2015==2015
   ok 28 - wday 1==1
   ok 29 - yday 291==291
   ok 30 - isdst 1==1
   # test_gmtime(1445259616, ...)
   ok 31 - epicsTime_localtime() success
   ok 32 - sec 16==16
   ok 33 - min 0==0
   ok 34 - hour 13==13
   ok 35 - mday 19==19
   ok 36 - mon 9==9
   ok 37 - year 2015==2015
   ok 38 - wday 1==1
   ok 39 - yday 291==291
   ok 40 - isdst 0==0
   # TZ = "HST10HST10"
   # test_localtime(1445259616, ...)
   ok 41 - epicsTime_localtime() success
   ok 42 - sec 16==16
   ok 43 - min 0==0
   ok 44 - hour 3==3
   ok 45 - mday 19==19
   ok 46 - mon 9==9
   ok 47 - year 2015==2015
   ok 48 - wday 1==1
   ok 49 - yday 291==291
   ok 50 - isdst 0==0
   # test_gmtime(1445259616, ...)
   ok 51 - epicsTime_localtime() success
   ok 52 - sec 16==16
   ok 53 - min 0==0
   ok 54 - hour 13==13
   ok 55 - mday 19==19
   ok 56 - mon 9==9
   ok 57 - year 2015==2015
   ok 58 - wday 1==1
   ok 59 - yday 291==291
   ok 60 - isdst 0==0
   # TZ = "UTC0"
   # test_localtime(1445259616, ...)
   ok 61 - epicsTime_localtime() success
   ok 62 - sec 16==16
   ok 63 - min 0==0
   ok 64 - hour 13==13
   ok 65 - mday 19==19
   ok 66 - mon 9==9
   ok 67 - year 2015==2015
   ok 68 - wday 1==1
   ok 69 - yday 291==291
   ok 70 - isdst 0==0
   # test_gmtime(1445259616, ...)
   ok 71 - epicsTime_localtime() success
   ok 72 - sec 16==16
   ok 73 - min 0==0
   ok 74 - hour 13==13
   ok 75 - mday 19==19
   ok 76 - mon 9==9
   ok 77 - year 2015==2015
   ok 78 - wday 1==1
   ok 79 - yday 291==291
   ok 80 - isdst 0==0
   # POSIX 1421244931
   # TZ = "EST5EDT"
   # test_localtime(1421244931, ...)
   ok 81 - epicsTime_localtime() success
   ok 82 - sec 31==31
   ok 83 - min 15==15
   ok 84 - hour 9==9
   ok 85 - mday 14==14
   ok 86 - mon 0==0
   ok 87 - year 2015==2015
   ok 88 - wday 3==3
   ok 89 - yday 13==13
   ok 90 - isdst 0==0
   # test_gmtime(1421244931, ...)
   ok 91 - epicsTime_localtime() success
   ok 92 - sec 31==31
   ok 93 - min 15==15
   ok 94 - hour 14==14
   ok 95 - mday 14==14
   ok 96 - mon 0==0
   ok 97 - year 2015==2015
   ok 98 - wday 3==3
   ok 99 - yday 13==13
   ok 100 - isdst 0==0
   # TZ = "CST6CDT"
   # test_localtime(1421244931, ...)
   ok 101 - epicsTime_localtime() success
   ok 102 - sec 31==31
   ok 103 - min 15==15
   ok 104 - hour 8==8
   ok 105 - mday 14==14
   ok 106 - mon 0==0
   ok 107 - year 2015==2015
   ok 108 - wday 3==3
   ok 109 - yday 13==13
   ok 110 - isdst 0==0
   # test_gmtime(1421244931, ...)
   ok 111 - epicsTime_localtime() success
   ok 112 - sec 31==31
   ok 113 - min 15==15
   ok 114 - hour 14==14
   ok 115 - mday 14==14
   ok 116 - mon 0==0
   ok 117 - year 2015==2015
   ok 118 - wday 3==3
   ok 119 - yday 13==13
   ok 120 - isdst 0==0
   # TZ = "HST10HST10"
   # test_localtime(1421244931, ...)
   ok 121 - epicsTime_localtime() success
   ok 122 - sec 31==31
   ok 123 - min 15==15
   ok 124 - hour 4==4
   ok 125 - mday 14==14
   ok 126 - mon 0==0
   ok 127 - year 2015==2015
   ok 128 - wday 3==3
   ok 129 - yday 13==13
   ok 130 - isdst 0==0
   # test_gmtime(1421244931, ...)
   ok 131 - epicsTime_localtime() success
   ok 132 - sec 31==31
   ok 133 - min 15==15
   ok 134 - hour 14==14
   ok 135 - mday 14==14
   ok 136 - mon 0==0
   ok 137 - year 2015==2015
   ok 138 - wday 3==3
   ok 139 - yday 13==13
   ok 140 - isdst 0==0
   # TZ = "UTC0"
   # test_localtime(1421244931, ...)
   ok 141 - epicsTime_localtime() success
   ok 142 - sec 31==31
   ok 143 - min 15==15
   ok 144 - hour 14==14
   ok 145 - mday 14==14
   ok 146 - mon 0==0
   ok 147 - year 2015==2015
   ok 148 - wday 3==3
   ok 149 - yday 13==13
   ok 150 - isdst 0==0
   # test_gmtime(1421244931, ...)
   ok 151 - epicsTime_localtime() success
   ok 152 - sec 31==31
   ok 153 - min 15==15
   ok 154 - hour 14==14
   ok 155 - mday 14==14
   ok 156 - mon 0==0
   ok 157 - year 2015==2015
   ok 158 - wday 3==3
   ok 159 - yday 13==13
   ok 160 - isdst 0==0

       Results
       =======
          Tests: 160
         Passed: 160 = 100.00%

   ***** epicsTypesTest *****
   1..10
   ok  1 - sizeof(epicsInt8) == 1
   ok  2 - sizeof(epicsUInt8) == 1
   ok  3 - sizeof(epicsInt16) == 2
   ok  4 - sizeof(epicsUInt16) == 2
   ok  5 - sizeof(epicsInt32) == 4
   ok  6 - sizeof(epicsUInt32) == 4
   ok  7 - sizeof(epicsInt64) == 8
   ok  8 - sizeof(epicsUInt64) == 8
   ok  9 - sizeof(epicsFloat32) == 4
   ok 10 - sizeof(epicsFloat64) == 8

       Results
       =======
          Tests: 10
         Passed:  10 = 100.00%

   ***** ipAddrToAsciiTest *****
   1..5
   # In doLookup
   # Start lookup
   # Poke
   # In transactionComplete(localhost:42) for cb
   # Finish
   # Finished
   ok  1 - cb.cont
   ok  2 - cb.done
   # In doCancel
   ok  3 - &trn1!=&trn2
   # Start lookup1
   # Wait start1
   # In transactionComplete(localhost:42) for cb1
   # Start lookup2
   # release engine2, implicitly cancels lookup2
   # Poke
   # Wait for lookup2 timeout
   # Finish
   # Finished
   ok  4 - !cb2.done
   # Complete lookup1
   # Poke
   # Finish
   # Finished
   ok  5 - cb1.done

       Results
       =======
          Tests: 5
         Passed:   5 = 100.00%

   ***** macDefExpandTest *****
   1..97
   ok  1 - FOO
   ok  2 - ${FOO}
   ok  3 - ${FOO,BAR}
   ok  4 - ${FOO,BAR=baz}
   ok  5 - ${FOO,BAR=$(FOO)}
   ok  6 - ${FOO,FOO}
   ok  7 - ${FOO,FOO=$(FOO)}
   ok  8 - ${FOO,BAR=baz,FUM}
   ok  9 - ${=}
   ok 10 - x${=}y
   ok 11 - ${,=}
   ok 12 - x${,=}y
   ok 13 - ${FOO=}
   ok 14 - x${FOO=}y
   ok 15 - ${FOO=,}
   ok 16 - x${FOO=,}y
   ok 17 - ${FOO,FOO=}
   ok 18 - x${FOO,FOO=}y
   ok 19 - ${FOO=,BAR}
   ok 20 - x${FOO=,BAR}y
   ok 21 - ${FOO=$(BAR=)}
   ok 22 - x${FOO=$(BAR=)}y
   ok 23 - ${FOO=,BAR=baz}
   ok 24 - x${FOO=,BAR=baz}y
   ok 25 - ${FOO=$(BAR),BAR=}
   ok 26 - x${FOO=$(BAR),BAR=}y
   ok 27 - ${=BAR}
   ok 28 - x${=BAR}y
   ok 29 - ${FOO=BAR}
   ok 30 - x${FOO=BAR}y
   ok 31 - ${FOO}
   ok 32 - ${FOO,FOO}
   ok 33 - x${FOO}y
   ok 34 - x${FOO}y${FOO}z
   ok 35 - ${FOO=BAR}
   ok 36 - x${FOO=BAR}y
   ok 37 - ${FOO=${BAZ}}
   ok 38 - ${FOO=${BAZ},BAR=$(BAZ)}
   ok 39 - x${FOO=${BAZ}}y
   ok 40 - x${FOO=${BAZ},BAR=$(BAZ)}y
   ok 41 - ${BAR=${FOO}}
   ok 42 - x${BAR=${FOO}}y
   ok 43 - w${BAR=x${FOO}y}z
   ok 44 - ${FOO,FOO=BAR}
   ok 45 - x${FOO,FOO=BAR}y
   ok 46 - ${BAR,BAR=$(FOO)}
   ok 47 - x${BAR,BAR=$(FOO)}y
   ok 48 - ${BAR,BAR=$($(FOO)),BLETCH=GRIBBLE}
   ok 49 - x${BAR,BAR=$($(FOO)),BLETCH=GRIBBLE}y
   ok 50 - ${$(BAR,BAR=$(FOO)),BLETCH=GRIBBLE}
   ok 51 - x${$(BAR,BAR=$(FOO)),BLETCH=GRIBBLE}y
   ok 52 - ${FOO}/${BAR}
   ok 53 - x${FOO}/${BAR}y
   ok 54 - ${FOO,BAR}/${BAR}
   ok 55 - ${FOO,BAR=x}/${BAR}
   ok 56 - ${BAZ=BLETCH,BAR}/${BAR}
   ok 57 - ${BAZ=BLETCH,BAR=x}/${BAR}
   ok 58 - ${${FOO}}
   ok 59 - x${${FOO}}y
   ok 60 - ${${FOO}=GRIBBLE}
   ok 61 - x${${FOO}=GRIBBLE}y
   ok 62 - ${${FOO}}
   ok 63 - ${FOO}
   ok 64 - ${FOO}
   ok 65 - ${FOO}
   ok 66 - ${FOO}
   ok 67 - ${FOO}
   ok 68 - ${FOO}
   ok 69 - ${FOO,FOO=$(FOO)}
   ok 70 - ${FOO=$(FOO)}
   ok 71 - ${FOO=$(BAR),BAR=$(FOO)}
   ok 72 - Macro A is 1
   ok 73 - Macro B is 2
   ok 74 - Macro C is 3
   ok 75 - Macro D is 4
   ok 76 - Macro E is 15
   ok 77 - Macro F undefined
   ok 78 - Macro A is 11
   ok 79 - Macro B is 2
   ok 80 - Macro C is 13
   ok 81 - Macro D is 14
   ok 82 - Macro E is 15
   ok 83 - Macro F undefined
   ok 84 - Macro G is 7
   ok 85 - Macro D is 24
   ok 86 - Macro F is 6
   ok 87 - Macro G is 17
   ok 88 - Macro A is 1
   ok 89 - Macro B is 2
   ok 90 - Macro C is 3
   ok 91 - Macro D is 24
   ok 92 - Macro E is 15
   ok 93 - Macro F is 6
   ok 94 - Macro G is 17
   ok 95 - Macro D is 34
   ok 96 - Macro G is 27
   ok 97 - Macro D is 24

       Results
       =======
          Tests: 97
         Passed:  97 = 100.00%

   ***** macLibTest *****
   1..93
   ok  1 - FOO => FOO
   ok  2 - $(FOO) => $(FOO,undefined)
   ok  3 - ${FOO} => $(FOO,undefined)
   ok  4 - ${FOO=${FOO}} => $(FOO,undefined)
   ok  5 - ${FOO,FOO} => $(FOO,undefined)
   ok  6 - ${FOO,FOO=${FOO}} => $(FOO,recursive)
   ok  7 - ${FOO,BAR} => $(FOO,undefined)
   ok  8 - ${FOO,BAR=baz} => $(FOO,undefined)
   ok  9 - ${FOO,BAR=${FOO}} => $(FOO,undefined)
   ok 10 - ${FOO,BAR=baz,FUM} => $(FOO,undefined)
   ok 11 - ${FOO=${BAR},BAR=${FOO}} => $(FOO,undefined)
   ok 12 - ${FOO,FOO=${BAR},BAR=${FOO}} => $(BAR,recursive)
   ok 13 - ${=} =>
   ok 14 - x${=}y => xy
   ok 15 - ${,=} =>
   ok 16 - x${,=}y => xy
   ok 17 - ${FOO=} =>
   ok 18 - x${FOO=}y => xy
   ok 19 - ${FOO=,} =>
   ok 20 - x${FOO=,}y => xy
   ok 21 - ${FOO,FOO=} =>
   ok 22 - x${FOO,FOO=}y => xy
   ok 23 - ${FOO=,BAR} =>
   ok 24 - x${FOO=,BAR}y => xy
   ok 25 - ${FOO=${BAR=}} =>
   ok 26 - x${FOO=${BAR=}}y => xy
   ok 27 - ${FOO=,BAR=baz} =>
   ok 28 - x${FOO=,BAR=baz}y => xy
   ok 29 - ${FOO=${BAR},BAR=} =>
   ok 30 - x${FOO=${BAR},BAR=}y => xy
   ok 31 - ${=BAR} => BAR
   ok 32 - x${=BAR}y => xBARy
   ok 33 - ${FOO=BAR} => BAR
   ok 34 - x${FOO=BAR}y => xBARy
   ok 35 - ${FOO} => BLETCH
   ok 36 - ${FOO,FOO} => BLETCH
   ok 37 - x${FOO}y => xBLETCHy
   ok 38 - x${FOO}y${FOO}z => xBLETCHyBLETCHz
   ok 39 - ${FOO=BAR} => BLETCH
   ok 40 - x${FOO=BAR}y => xBLETCHy
   ok 41 - ${FOO=${BAZ}} => BLETCH
   ok 42 - ${FOO=${BAZ},BAR=${BAZ}} => BLETCH
   ok 43 - x${FOO=${BAZ}}y => xBLETCHy
   ok 44 - x${FOO=${BAZ},BAR=${BAZ}}y => xBLETCHy
   ok 45 - ${BAR=${FOO}} => BLETCH
   ok 46 - x${BAR=${FOO}}y => xBLETCHy
   ok 47 - w${BAR=x${FOO}y}z => wxBLETCHyz
   ok 48 - ${FOO,FOO=BAR} => BAR
   ok 49 - x${FOO,FOO=BAR}y => xBARy
   ok 50 - ${BAR,BAR=${FOO}} => BLETCH
   ok 51 - x${BAR,BAR=${FOO}}y => xBLETCHy
   ok 52 - ${BAR,BAR=${${FOO}},BLETCH=GRIBBLE} => GRIBBLE
   ok 53 - x${BAR,BAR=${${FOO}},BLETCH=GRIBBLE}y => xGRIBBLEy
   ok 54 - ${${BAR,BAR=${FOO}},BLETCH=GRIBBLE} => GRIBBLE
   ok 55 - x${${BAR,BAR=${FOO}},BLETCH=GRIBBLE}y => xGRIBBLEy
   ok 56 - ${N=${FOO}/${BAR},BAR=GLEEP} => BLETCH/GLEEP
   ok 57 - ${FOO}/${BAR} => BLETCH/GLEEP
   ok 58 - x${FOO}/${BAR}y => xBLETCH/GLEEPy
   ok 59 - ${FOO,BAR}/${BAR} => BLETCH/GLEEP
   ok 60 - ${FOO,BAR=x}/${BAR} => BLETCH/GLEEP
   ok 61 - ${BAZ=BLETCH,BAR}/${BAR} => BLETCH/GLEEP
   ok 62 - ${BAZ=BLETCH,BAR=x}/${BAR} => BLETCH/GLEEP
   ok 63 - ${N=${FOO}/${BAR}} => BLETCH/GLEEP
   ok 64 - ${${FOO}} => BAR
   ok 65 - x${${FOO}}y => xBARy
   ok 66 - ${${FOO}=GRIBBLE} => BAR
   ok 67 - x${${FOO}=GRIBBLE}y => xBARy
   ok 68 - ${${FOO}} => GLEEP
   ok 69 - ${BLETCH=${FOO}} => GLEEP
   ok 70 - ${FOO} => GLEEP
   ok 71 - ${FOO=BLETCH,BAR=BAZ} => BAZ
   ok 72 - ${FOO} => $(BAZ,undefined)
   ok 73 - ${FOO} => GRIBBLE
   ok 74 - ${FOO,BAZ=GEEK} => GEEK
   ok 75 - ${FOO} => VAL1
   ok 76 - ${FOO} => VAL2
   ok 77 - $(FOO)$(FOO1) => VAL2$(FOO1,undefined)
   ok 78 - $(FOO1)$(FOO) => $(FOO1,undefined)VAL2
   ok 79 - ${FOO} => $(BAR,recursive)
   ok 80 - ${FOO=GRIBBLE} => $(BAR,recursive)
   ok 81 - ${FOO=GRIBBLE,BAR=${FOO}} => $(BAR,recursive)
   ok 82 - ${FOO,FOO=${FOO}} => $(FOO,recursive)
   ok 83 - ${FOO=GRIBBLE,FOO=${FOO}} => $(FOO,recursive)
   ok 84 - $(CRUX) => $(CRUX)
   ok 85 - ${FOO} => $(BAR)
   ok 86 - expansion returned 51, expected 51
   ok 87 - final character 79, expect 79 (y)
   ok 88 - terminator character 0, expect 0
   ok 89 - sentinel character 7e, expect 7e, (~)
   ok 90 - expansion returned 52, expected 52
   ok 91 - final character 7a, expect 7a (z)
   ok 92 - terminator character 0, expect 0
   ok 93 - sentinel character 7e, expect 7e, (~)

       Results
       =======
          Tests: 93
         Passed:  93 = 100.00%

   ***** osiSockTest *****
   1..24
   ok  1 - osiSockAttach
   # udpSockTest()
   ok  2 - epicsSocketCreate INET, DGRAM, 0
   ok  3 - setsockopt BROADCAST := 1
   ok  4 - getsockopt BROADCAST => 32
   ok  5 - setsockopt BROADCAST := 0
   ok  6 - getsockopt BROADCAST => 0
   ok  7 - setsockopt MULTICAST_LOOP := 1
   ok  8 - getsockopt MULTICAST_LOOP => 1
   ok  9 - setsockopt MULTICAST_LOOP := 0
   ok 10 - getsockopt MULTICAST_LOOP => 0
   ok 11 - setsockopt IP_MULTICAST_TTL := 2
   ok 12 - getsockopt IP_MULTICAST_TTL => 2
   ok 13 - setsockopt IP_MULTICAST_TTL := 1
   ok 14 - getsockopt IP_MULTICAST_TTL => 1
   # udpSockFanoutBindTest()
   # First test if epicsSocketEnableAddressUseForDatagramFanout() is necessary
   ok 15 - bind() to port 1043
   ok 16 - bind() to 1043 error -1, 112
   # Now the real test
   ok 17 - bind() to port 1043
   ok 18 - bind() to port 1043
   # udpSockFanoutTest()
   # Interface 141.14.143.255:5064
   # Not LO
   # RX1 start
   # RX2 start
   # RX2 success 0
   # RX1 success 0
   # RX2 success 1
   # RX1 success 1
   # RX2 success 2
   # RX1 success 2
   # RX ignore
   # RX ignore
   # RX2 success 3
   # RX1 success 3
   # RX ignore
   # RX ignore
   # RX2 success 4
   # RX1 success 4
   # RX ignore
   # RX ignore
   # RX ignore
   # RX ignore
   # RX2 success 5
   # RX2 end
   # RX1 success 5
   # RX1 end
   # Result: RX1 3f:0 RX2 3f:0
   ok 19 - Found non-loopback interface
   ok 20 - Successes 1
   # tcpSockReuseBindTest(0)
   ok 21 - bind() to port 1028
   ok 22 - bind() to 1028 error -1, 112
   # tcpSockReuseBindTest(1)
   # epicsSocketEnableAddressReuseDuringTimeWaitState
   ok 23 - bind() to port 1029
   ok 24 - bind() to 1029 error -1, 112

       Results
       =======
          Tests: 24
         Passed:  24 = 100.00%

   ***** ringBytesTest *****
   1..292
   ok  1 - Free: 10 == 10
   ok  2 - Used: 0 == 0
   ok  3 - Empty: 1 == 1
   ok  4 - Full: 0 == 0
   ok  5 - HighWaterMark: 0 == 0
   ok  6 - ring put 0
   ok  7 - Free: 10 == 10
   ok  8 - Used: 0 == 0
   ok  9 - Empty: 1 == 1
   ok 10 - Full: 0 == 0
   ok 11 - HighWaterMark: 0 == 0
   ok 12 - ring get 0
   ok 13 - Free: 10 == 10
   ok 14 - Used: 0 == 0
   ok 15 - Empty: 1 == 1
   ok 16 - Full: 0 == 0
   ok 17 - HighWaterMark: 0 == 0
   ok 18 - get matches write
   ok 19 - ring put 1
   ok 20 - Free: 9 == 9
   ok 21 - Used: 1 == 1
   ok 22 - Empty: 0 == 0
   ok 23 - Full: 0 == 0
   ok 24 - HighWaterMark: 1 == 1
   ok 25 - ring get 1
   ok 26 - Free: 10 == 10
   ok 27 - Used: 0 == 0
   ok 28 - Empty: 1 == 1
   ok 29 - Full: 0 == 0
   ok 30 - HighWaterMark: 1 == 1
   ok 31 - get matches write
   ok 32 - ring put 2
   ok 33 - Free: 8 == 8
   ok 34 - Used: 2 == 2
   ok 35 - Empty: 0 == 0
   ok 36 - Full: 0 == 0
   ok 37 - HighWaterMark: 2 == 2
   ok 38 - ring get 2
   ok 39 - Free: 10 == 10
   ok 40 - Used: 0 == 0
   ok 41 - Empty: 1 == 1
   ok 42 - Full: 0 == 0
   ok 43 - HighWaterMark: 2 == 2
   ok 44 - get matches write
   ok 45 - ring put 3
   ok 46 - Free: 7 == 7
   ok 47 - Used: 3 == 3
   ok 48 - Empty: 0 == 0
   ok 49 - Full: 0 == 0
   ok 50 - HighWaterMark: 3 == 3
   ok 51 - ring get 3
   ok 52 - Free: 10 == 10
   ok 53 - Used: 0 == 0
   ok 54 - Empty: 1 == 1
   ok 55 - Full: 0 == 0
   ok 56 - HighWaterMark: 3 == 3
   ok 57 - get matches write
   ok 58 - ring put 4
   ok 59 - Free: 6 == 6
   ok 60 - Used: 4 == 4
   ok 61 - Empty: 0 == 0
   ok 62 - Full: 0 == 0
   ok 63 - HighWaterMark: 4 == 4
   ok 64 - ring get 4
   ok 65 - Free: 10 == 10
   ok 66 - Used: 0 == 0
   ok 67 - Empty: 1 == 1
   ok 68 - Full: 0 == 0
   ok 69 - HighWaterMark: 4 == 4
   ok 70 - get matches write
   ok 71 - ring put 5
   ok 72 - Free: 5 == 5
   ok 73 - Used: 5 == 5
   ok 74 - Empty: 0 == 0
   ok 75 - Full: 0 == 0
   ok 76 - HighWaterMark: 5 == 5
   ok 77 - ring get 5
   ok 78 - Free: 10 == 10
   ok 79 - Used: 0 == 0
   ok 80 - Empty: 1 == 1
   ok 81 - Full: 0 == 0
   ok 82 - HighWaterMark: 5 == 5
   ok 83 - get matches write
   ok 84 - ring put 6
   ok 85 - Free: 4 == 4
   ok 86 - Used: 6 == 6
   ok 87 - Empty: 0 == 0
   ok 88 - Full: 0 == 0
   ok 89 - HighWaterMark: 6 == 6
   ok 90 - ring get 6
   ok 91 - Free: 10 == 10
   ok 92 - Used: 0 == 0
   ok 93 - Empty: 1 == 1
   ok 94 - Full: 0 == 0
   ok 95 - HighWaterMark: 6 == 6
   ok 96 - get matches write
   ok 97 - ring put 7
   ok 98 - Free: 3 == 3
   ok 99 - Used: 7 == 7
   ok 100 - Empty: 0 == 0
   ok 101 - Full: 0 == 0
   ok 102 - HighWaterMark: 7 == 7
   ok 103 - ring get 7
   ok 104 - Free: 10 == 10
   ok 105 - Used: 0 == 0
   ok 106 - Empty: 1 == 1
   ok 107 - Full: 0 == 0
   ok 108 - HighWaterMark: 7 == 7
   ok 109 - get matches write
   ok 110 - ring put 8
   ok 111 - Free: 2 == 2
   ok 112 - Used: 8 == 8
   ok 113 - Empty: 0 == 0
   ok 114 - Full: 0 == 0
   ok 115 - HighWaterMark: 8 == 8
   ok 116 - ring get 8
   ok 117 - Free: 10 == 10
   ok 118 - Used: 0 == 0
   ok 119 - Empty: 1 == 1
   ok 120 - Full: 0 == 0
   ok 121 - HighWaterMark: 8 == 8
   ok 122 - get matches write
   ok 123 - ring put 9
   ok 124 - Free: 1 == 1
   ok 125 - Used: 9 == 9
   ok 126 - Empty: 0 == 0
   ok 127 - Full: 0 == 0
   ok 128 - HighWaterMark: 9 == 9
   ok 129 - ring get 9
   ok 130 - Free: 10 == 10
   ok 131 - Used: 0 == 0
   ok 132 - Empty: 1 == 1
   ok 133 - Full: 0 == 0
   ok 134 - HighWaterMark: 9 == 9
   ok 135 - get matches write
   ok 136 - ring put 1, 0
   ok 137 - Free: 9 == 9
   ok 138 - Used: 1 == 1
   ok 139 - Empty: 0 == 0
   ok 140 - Full: 0 == 0
   ok 141 - HighWaterMark: 1 == 1
   ok 142 - ring put 1, 1
   ok 143 - Free: 8 == 8
   ok 144 - Used: 2 == 2
   ok 145 - Empty: 0 == 0
   ok 146 - Full: 0 == 0
   ok 147 - HighWaterMark: 2 == 2
   ok 148 - ring put 1, 2
   ok 149 - Free: 7 == 7
   ok 150 - Used: 3 == 3
   ok 151 - Empty: 0 == 0
   ok 152 - Full: 0 == 0
   ok 153 - HighWaterMark: 3 == 3
   ok 154 - ring put 1, 3
   ok 155 - Free: 6 == 6
   ok 156 - Used: 4 == 4
   ok 157 - Empty: 0 == 0
   ok 158 - Full: 0 == 0
   ok 159 - HighWaterMark: 4 == 4
   ok 160 - ring put 1, 4
   ok 161 - Free: 5 == 5
   ok 162 - Used: 5 == 5
   ok 163 - Empty: 0 == 0
   ok 164 - Full: 0 == 0
   ok 165 - HighWaterMark: 5 == 5
   ok 166 - ring put 1, 5
   ok 167 - Free: 4 == 4
   ok 168 - Used: 6 == 6
   ok 169 - Empty: 0 == 0
   ok 170 - Full: 0 == 0
   ok 171 - HighWaterMark: 6 == 6
   ok 172 - ring put 1, 6
   ok 173 - Free: 3 == 3
   ok 174 - Used: 7 == 7
   ok 175 - Empty: 0 == 0
   ok 176 - Full: 0 == 0
   ok 177 - HighWaterMark: 7 == 7
   ok 178 - ring put 1, 7
   ok 179 - Free: 2 == 2
   ok 180 - Used: 8 == 8
   ok 181 - Empty: 0 == 0
   ok 182 - Full: 0 == 0
   ok 183 - HighWaterMark: 8 == 8
   ok 184 - ring put 1, 8
   ok 185 - Free: 1 == 1
   ok 186 - Used: 9 == 9
   ok 187 - Empty: 0 == 0
   ok 188 - Full: 0 == 0
   ok 189 - HighWaterMark: 9 == 9
   ok 190 - ring put 1, 9
   ok 191 - Free: 0 == 0
   ok 192 - Used: 10 == 10
   ok 193 - Empty: 0 == 0
   ok 194 - Full: 1 == 1
   ok 195 - HighWaterMark: 10 == 10
   ok 196 - put to full ring
   ok 197 - Free: 0 == 0
   ok 198 - Used: 10 == 10
   ok 199 - Empty: 0 == 0
   ok 200 - Full: 1 == 1
   ok 201 - HighWaterMark: 10 == 10
   ok 202 - ring get 1, 0
   ok 203 - Free: 1 == 1
   ok 204 - Used: 9 == 9
   ok 205 - Empty: 0 == 0
   ok 206 - Full: 0 == 0
   ok 207 - HighWaterMark: 10 == 10
   ok 208 - ring get 1, 1
   ok 209 - Free: 2 == 2
   ok 210 - Used: 8 == 8
   ok 211 - Empty: 0 == 0
   ok 212 - Full: 0 == 0
   ok 213 - HighWaterMark: 10 == 10
   ok 214 - ring get 1, 2
   ok 215 - Free: 3 == 3
   ok 216 - Used: 7 == 7
   ok 217 - Empty: 0 == 0
   ok 218 - Full: 0 == 0
   ok 219 - HighWaterMark: 10 == 10
   ok 220 - ring get 1, 3
   ok 221 - Free: 4 == 4
   ok 222 - Used: 6 == 6
   ok 223 - Empty: 0 == 0
   ok 224 - Full: 0 == 0
   ok 225 - HighWaterMark: 10 == 10
   ok 226 - ring get 1, 4
   ok 227 - Free: 5 == 5
   ok 228 - Used: 5 == 5
   ok 229 - Empty: 0 == 0
   ok 230 - Full: 0 == 0
   ok 231 - HighWaterMark: 10 == 10
   ok 232 - ring get 1, 5
   ok 233 - Free: 6 == 6
   ok 234 - Used: 4 == 4
   ok 235 - Empty: 0 == 0
   ok 236 - Full: 0 == 0
   ok 237 - HighWaterMark: 10 == 10
   ok 238 - ring get 1, 6
   ok 239 - Free: 7 == 7
   ok 240 - Used: 3 == 3
   ok 241 - Empty: 0 == 0
   ok 242 - Full: 0 == 0
   ok 243 - HighWaterMark: 10 == 10
   ok 244 - ring get 1, 7
   ok 245 - Free: 8 == 8
   ok 246 - Used: 2 == 2
   ok 247 - Empty: 0 == 0
   ok 248 - Full: 0 == 0
   ok 249 - HighWaterMark: 10 == 10
   ok 250 - ring get 1, 8
   ok 251 - Free: 9 == 9
   ok 252 - Used: 1 == 1
   ok 253 - Empty: 0 == 0
   ok 254 - Full: 0 == 0
   ok 255 - HighWaterMark: 10 == 10
   ok 256 - ring get 1, 9
   ok 257 - Free: 10 == 10
   ok 258 - Used: 0 == 0
   ok 259 - Empty: 1 == 1
   ok 260 - Full: 0 == 0
   ok 261 - HighWaterMark: 10 == 10
   ok 262 - get matches write
   ok 263 - get from empty ring
   ok 264 - Free: 10 == 10
   ok 265 - Used: 0 == 0
   ok 266 - Empty: 1 == 1
   ok 267 - Full: 0 == 0
   ok 268 - HighWaterMark: 10 == 10
   ok 269 - ring put beyond ring capacity (0, expected 0)
   ok 270 - Free: 10 == 10
   ok 271 - Used: 0 == 0
   ok 272 - Empty: 1 == 1
   ok 273 - Full: 0 == 0
   ok 274 - HighWaterMark: 0 == 0
   ok 275 - ring put 1
   ok 276 - Free: 9 == 9
   ok 277 - Used: 1 == 1
   ok 278 - Empty: 0 == 0
   ok 279 - Full: 0 == 0
   ok 280 - HighWaterMark: 1 == 1
   ok 281 - ring put beyond ring capacity (0, expected 0)
   ok 282 - Free: 9 == 9
   ok 283 - Used: 1 == 1
   ok 284 - Empty: 0 == 0
   ok 285 - Full: 0 == 0
   ok 286 - HighWaterMark: 1 == 1
   ok 287 - ring get 1
   ok 288 - Free: 10 == 10
   ok 289 - Used: 0 == 0
   ok 290 - Empty: 1 == 1
   ok 291 - Full: 0 == 0
   ok 292 - HighWaterMark: 1 == 1

       Results
       =======
          Tests: 292
         Passed: 292 = 100.00%

   ***** ringPointerTest *****
   1..42
   # Testing operations w/o threading
   ok  1 - epicsRingPointerIsEmpty(ring)
   ok  2 - !epicsRingPointerIsFull(ring)
   ok  3 - epicsRingPointerGetFree(ring)==rsize
   ok  4 - epicsRingPointerGetSize(ring)==rsize
   ok  5 - epicsRingPointerGetUsed(ring)==0
   ok  6 - epicsRingPointerGetHighWaterMark(ring)==0
   ok  7 - epicsRingPointerPop(ring)==NULL
   ok  8 - epicsRingPointerPush(ring, addr)==1
   ok  9 - !epicsRingPointerIsEmpty(ring)
   ok 10 - !epicsRingPointerIsFull(ring)
   ok 11 - epicsRingPointerGetFree(ring)==rsize-1
   ok 12 - epicsRingPointerGetSize(ring)==rsize
   ok 13 - epicsRingPointerGetUsed(ring)==1
   ok 14 - epicsRingPointerGetHighWaterMark(ring)==1
   ok 15 - epicsRingPointerGetHighWaterMark(ring)==1
   # Fill it up
   ok 16 - 101 == 101
   ok 17 - !epicsRingPointerIsEmpty(ring)
   ok 18 - epicsRingPointerIsFull(ring)
   ok 19 - epicsRingPointerGetFree(ring)==0
   ok 20 - epicsRingPointerGetSize(ring)==rsize
   ok 21 - epicsRingPointerGetUsed(ring)==rsize
   ok 22 - epicsRingPointerGetHighWaterMark(ring)==rsize
   # Drain it out
   ok 23 - !foundCorruption
   ok 24 - 101 == 101
   ok 25 - epicsRingPointerIsEmpty(ring)
   ok 26 - !epicsRingPointerIsFull(ring)
   ok 27 - epicsRingPointerGetFree(ring)==rsize
   ok 28 - epicsRingPointerGetSize(ring)==rsize
   ok 29 - epicsRingPointerGetUsed(ring)==0
   ok 30 - epicsRingPointerGetHighWaterMark(ring)==rsize
   # Fill it up again
   # flush
   ok 31 - epicsRingPointerIsFull(ring)
   ok 32 - epicsRingPointerIsEmpty(ring)
   ok 33 - !epicsRingPointerIsFull(ring)
   ok 34 - epicsRingPointerGetFree(ring)==rsize
   ok 35 - epicsRingPointerGetSize(ring)==rsize
   ok 36 - epicsRingPointerGetUsed(ring)==0
   # single producer, single consumer without locking
   # Everything enqueued, Stopping consumer
   # Pushed 1000, have 0 remaining unconsumed
   # Expect 1000 consumed
   ok 37 - 0x3e703e7 == 0x3e703e7
   ok 38 - Consumer consumed all
   ok 39 - !foundCorruption
   # single producer, single consumer with locking
   # Everything enqueued, Stopping consumer
   # Pushed 1000, have 0 remaining unconsumed
   # Expect 1000 consumed
   ok 40 - 0x3e703e7 == 0x3e703e7
   ok 41 - Consumer consumed all
   ok 42 - !foundCorruption

       Results
       =======
          Tests: 42
         Passed:  42 = 100.00%

   ***** taskwdTest *****
   1..8
   ok  1 - monInsert(thread='testTask1')
   ok  2 - monInsert(thread='testTask2')
   # Task 2 suspending
   ok  3 - monNotify(thread='testTask2', suspended=1)
   ok  4 - anyNotify(thread='testTask2')
   ok  5 - taskNotify id='2'
   # Task 2 alive again
   ok  6 - monNotify(thread='testTask2', suspended=0)
   # Task 2 cleaning up
   ok  7 - monRemove(thread='testTask2')
   # Task 1 cleaning up
   ok  8 - monRemove(thread='testTask1')

       Results
       =======
          Tests: 8
         Passed:   8 = 100.00%


       EPICS Test Harness Results
       ==========================

   All tests successful.
   Programs=37, Tests=3062, 352 wallclock secs


   ***** epicsExitTest *****
   1..15
   ok  1 - Registered counter()


       EPICS Test Harness Results
       ==========================

   All tests successful.
   Programs=37, Tests=3062, 352 wallclock secs

   ok  2 - counter() called once
   ok  3 - unregistered counter() not called
   ok  4 - Registered mainExit()
   # threadA starting
   ok  5 - Registered atExit(0xc918f0)
   ok  6 - Registered atThreadExit(0xc918f0)
   # threadA waiting for atExit
   # threadB starting
   ok  7 - Registered atExit(0xc91940)
   ok  8 - Registered atThreadExit(0xc91940)
   # threadB waiting for atExit
   # Calling epicsExit
   ok  9 - threadB reached atExit
   ok 10 - threadB terminating
   ok 11 - threadB destroying pinfo
   ok 12 - threadA reached atExit
   ok 13 - threadA terminating
   ok 14 - threadA destroying pinfo
   ok 15 - Reached mainExit

       Results
       =======
          Tests: 15
         Passed:  15 = 100.00%
   fatal source: RTEMS_FATAL_SOURCE_EXIT
   bsp_fatal_extension(): RTEMS terminated -- no way back to MotLoad so I reset the card
   Printing a stack trace for your convenience :-)

   0x01968576--> 0x01968572--> 0x00527160--> 0x00527732--> 0x00538444
   0x00450052--> 0x01856708--> 0x01750120--> 0x00343720--> 0x00086144
   0x00358976--> 0x00262740--> 0x00453068--> 0x00518084--> 0x00514140
   0x00513964



   Copyright(C)2008-2009,Emerson Network Power-Embedded Computing,Inc.
   All Rights Reserved
   Copyright Motorola Inc. 1999-2007, All Rights Reserved
   MOTLoad RTOS Version 2.0,  PAL Version 2.3 RM01
   Fri Jan 23 14:47:54 MST 2009

   MPU-Type             =MPC74x7
   MPU-Int Clock Speed  =1266MHz
   MPU-Ext Clock Speed  =133MHz
   MPU-Int Cache(L2) Enabled, 512KB, L2CR =C0000000
   MPU-Ext Cache(L3) Enabled, 2MB, 211MHz, L3CR =DC026300

   PCI bus instance 0   =64 bit, 133 Mhz, PCI-X
   PCI bus instance 1   =64 bit, PCI

   Reset/Boot Vector    =Flash1

   Local Memory Found   =20000000 (&536870912)
   User Download Buffer =006B7000:008B6FFF

   Boot Script - Press <ESC> to Bypass, <SPC> to Continue
   MVME6100>
