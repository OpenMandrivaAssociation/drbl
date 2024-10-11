Summary:	DRBL (Diskless Remote Boot in Linux) package
Name:		drbl
Version:	5.3.2
Release:	1
License:	GPLv2+
Group:		Networking/Other
URL:		https://drbl.org
Source0:  https://free.nchc.org.tw/drbl/src/stable/%{name}-%{version}.tar.xz

# Old source below:
#Source0:	https://sourceforge.net/projects/drbl/files/drbl_stable/%{version}/drbl-%{version}.tar.xz
BuildArch:	noarch

%description
DRBL (Diskless Remote Boot in Linux).
DRBL provides a diskless or systemless environment for client machines.
It works on various Linux distro like Arch, Debian, Ubuntu, Red Hat, Fedora, OpenSuSE and OpenMandriva.
DRBL uses distributed hardware resources and makes it possible for
clients to fully access local hardware.
It also includes Clonezilla, a partition and disk cloning utility similar
to Symantec Ghost(TM) or True Image(TM).

For more details, check
1. http://drbl.org or http://drbl.sourceforge.net (English)
2. http://drbl.nchc.org.tw (Traditional Chinese - Taiwan) 

%prep
%autosetup -p1

%build
%make_build all

%install
%make_install
mv %{buildroot}%{_prefix}/sbin/* %{buildroot}%{_bindir}/
rmdir %{buildroot}%{_prefix}/sbin

%files
%doc doc/*
%_bindir/*
%_datadir/%name
%_sysconfdir/%name
%_datadir/gdm/themes/drbl-gdm
