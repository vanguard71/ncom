# $Id: ncom.spec 2009-03-24  $
# Authority:
# Upstream: 

%{?dist: %{expand: %%define %dist 1}}

Summary: Perl-based Command Line utility for Nagios
Name: ncom
Version: 0.5
Release: 5
License: GPL
Group: Applications/System
URL: https://wiki.cc.columbia.edu/net:nagios:nagios_command_line_documentation/
Source: svn+ssh://svn.cc.columba.edu/svn/netdev/nagios/trunk/nagiosscripts/commandline/ncom-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
AutoReq: no
Requires: perl

%description
This package contains the ncom command line utility for nagios.

But you may need additional packages. Depending on what plugins you
use, the following packages may be required:

    perl 

%prep
tar -xvzf $RPM_SOURCE_DIR/ncom-%{version}.tar.gz 

%setup

%build

%install
%{__install} -d -m0755 %{buildroot}/usr/local/bin/
%{__install} -m0755 ncom %{buildroot}/usr/local/bin/ncom

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, nagios, 0755)
/usr/local/bin/ncom

%changelog

