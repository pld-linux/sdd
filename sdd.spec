Summary:	disk dump and restore to and from tape or file
Name:		sdd
Version:	1.31
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.fokus.gmd.de/pub/unix/sdd/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sdd is a replacement for a program called 'dd'. sdd is much faster
than dd in cases where input block size (ibs) is not equal to the
output block size (obs). Statistics are more easily understoon than
those from 'dd'. Timing available, -time option will print transfer
speed Timing & Statistics available at any time with SIGQUIT (^\) Can
seek on input and output Fast null input Fast null output. Support for
the RMT (Remote Tape Server) protocol makes remote I/O fast and easy.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man4}

install sdd/OBJ/amd_athlon-tm-_processor-linux-cc/sdd $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AN-%{version}
%attr(755,root,root) %{_bindir}/*
