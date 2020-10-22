Installation on Windows
=======================

Introduction
------------
We assume that you know more or less what EPICS is. You can get the basic ideas from https://epics-controls.org/about-epics/. These instructions start from scratch on a Windows system and get you to the point where you have a working IOC and can connect to it from a command line shell. Other How-Tos will guide you further.

Path Names
----------

Make based builds do not work properly when there are space characters in the paths that are part of the build (including the path where the `make` application resides).

Try to avoid paths with embedded spaces. If you can't, use the Windows short path (can be displayed with ``dir /x``) for the path component with spaces in any path settings.

Thoughts on CYGWIN
------------------

EPICS Base has its own native Windows implementation of the necessary low level services. There is no need to go through the Posix emulation layer that Cygwin provides. The native Windows implementation is more portable and performs better. Unless you need to use Cygwin, e.g., if you are using a binary vendor library for Cygwin, you should prefer a native Windows build.

Cygwin is deprecated as a target platform for EPICS.

That said,...

Prepare Your System
-------------------

You will need the following software packages / applications available on your machine to compile EPICS from sources:

* C++ compiler with its libraries: either MinGW (GCC) or Microsoft's Visual Studio compiler (VS)
* an archive unpacker (7zip or similar)
* GNU Make
* Perl
* Python (if not already, very soon)

There are different ways to get and install these parts.

MSYS2
^^^^^

`MSYS2 <https://www.msys2.org/>`_ (available for Windows 7 and up) is a pretty complete "feels like Linux" environment. It includes a Linux style package manager (`pacman`), which makes it very easy to install the MinGW toolchains (32 and 64 bit) and the other necessary tools. It also offers a bash shell. If you are used to working in a Linux environment, you will like working on MSYS2.

For using the MinGW/GCC compilers, MSYS2 is strongly recommended. It makes it especially easy to update the compiler chains.

For using the Visual Studio compilers, MSYS2 makes getting and updating the other tools very simple. You can run the build from the MSYS2 bash shell as well as from any other shell (command.com, PowerShell).

Windows Installers
^^^^^^^^^^^^^^^^^^

If you choose not to use MSYS2, you will need to install the required tools independently using their proper Windows installers.

For Perl, both Strawberry Perl and ActivePerl are known to work. Strawberry Perl is more popular; it includes GNU Make (as `gmake.exe`) and the GCC compiler necessary to build the Channel Access Perl module that is part of EPICS Base.

Any Visual Studio installation will need the "C++ development" parts.

For GNU Make, the easiest way is to use the one included in Strawberry Perl or the Windows binary that is provided on the EPICS web site at: https://epics.anl.gov/download/tools/make-4.2.1-win64.zip

Tools in the PATH
^^^^^^^^^^^^^^^^^

No matter which shell you use, the tools (perl, make, python) should end up being in the `%PATH%`, so that they are found when called just by their name.

Install and Build
-----------------

The detailed instructions for installing and building with MSYS2 and without are shown in the next two sections (pages).

.. toctree::
   :maxdepth: 1

   installation-windows-msys2
   installation-windows-plain
