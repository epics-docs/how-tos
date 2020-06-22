Packages required for EPICS on Centos 8
=======================================

.. contents:: Contents


Overview
--------
This document describes the packages that must be installed in order to build EPICS base, 
synApps, and areaDetector on a new Centos 8 system.  
For other versions of Linux the package manager and package names may be different, 
but the requirements are likely to be the same.

Add the Extra Packages for Enterprise Linux (EPEL) site for the dnf package manager.  
This site has additional packages that are needed::

  dnf install epel-release

Edit ``/etc/yum.repos.d/CentOS-PowerTools.repo`` to set ``enabled=1`` to enable that repository,
because it also contains needed packages.

Packages required to build EPICS base
-------------------------------------

::

  dnf install gcc
  dnf install gcc-c++
  dnf install gcc-toolset-9-make
  dnf install readline-devel
  dnf install perl-ExtUtils-Install


Packages required by the sequencer
----------------------------------

::

  dnf install re2c

Packages required by epics-modules/asyn
---------------------------------------

::

  dnf install rpcgen
  dnf install libtirpc-devel

Packages required by the Canberra and Amptek support in epics-modules/mca
-------------------------------------------------------------------------

::

  dnf install libnet-devel
  dnf install libpcap-devel
  dnf install libusb-devel

Packages required by the Linux drivers in epics-modules/measComp
----------------------------------------------------------------

::

  dnf install libnet-devel
  dnf install libpcap-devel
  dnf install libusb-devel

Packages required by areaDetector/ADSupport/GraphicsMagick
----------------------------------------------------------

::

  dnf install xorg-x11-proto-devel
  dnf install libX11-devel
  dnf install libXext-devel


Packages required by areaDetector/ADEiger
-----------------------------------------

::

  dnf install zeromq-devel


Packages required to build aravis 7.0.2 for areaDetector/ADAravis
-----------------------------------------------------------------

::

  dnf install ninja-build
  dnf install meson
  dnf install glib2-devel
  dnf install libxml2-devel
  dnf install gtk3-devel
  dnf install gstreamer1
  dnf install gstreamer1-devel
  dnf install gstreamer1-plugins-base-devel
  dnf install libnotify-devel
  dnf install gtk-doc
  dnf install gobject-introspection-devel


Packages required to build areaDetector/ADVimba
-----------------------------------------------

::

 dnf install glibmm24-devel


Packages required to build EDM
------------------------------

::

  dnf install giflib 
  dnf install giflib-devel
  dnf install zlib-devel
  dnf install libpng-devel
  dnf install motif-devel
  dnf install libXtst-devel

Packages required to build MEDM
------------------------------

::

  dnf install libXt-devel
  dnf install motif-devel


