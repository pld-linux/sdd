Summary:	disk dump and restore to and from tape or file
Summary(pl.UTF-8):   Narzędzia do zrzutów i odtwarzania dysku do/z taśmy lub pliku
Name:		sdd
Version:	1.52
Release:	0.2
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.berlios.de/pub/sdd/%{name}-%{version}.tar.gz
# Source0-md5:	efb6f2d8a39080c8ad085211e01293d6
BuildRequires:	automake
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sdd is a replacement for a program called 'dd'. sdd is much faster
than dd in cases where input block size (ibs) is not equal to the
output block size (obs). Statistics are more easily understoon than
those from 'dd'. Timing available, -time option will print transfer
speed. Timing & Statistics available at any time with SIGQUIT (^\).
Can seek on input and output. Fast null input. Fast null output.
Support for the RMT (Remote Tape Server) protocol makes remote I/O
fast and easy.

%description -l pl.UTF-8
sdd to zamiennik programu o nazwie "dd". sdd jest o wiele szybszy niż
dd w przypadkach, kiedy rozmiar bloku wejściowego (ibs) nie jest równy
rozmiarowi bloku wyjściowego (obs). Statystyki są bardziej zrozumiałe
od tych podawanych przez dd. Dostępny jest pomiar czasu - opcja -time
wypisuje szybkość transweru. Czas i statystyka są dostępne w każdej
chwili przez SIGQUIT (^\). Może ustawiać pozycję w pliku wejściowym i
wyjściowym; szybkie wczytywanie i zapis pustej zawartości. Obsługa
protokołu RMT (Remote Tape Server) czyni zdalne wejście/wyjście
szybkim i łatwym.

%package devel
Summary:	Header file for sdd
Summary(pl.UTF-8):   Pliki nagłówkowe bibliotek sdd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
sdd header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek sdd.

%package static
Summary:	Static libraries for sdd
Summary(pl.UTF-8):   Statyczne biblioteki dla sdd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
sdd static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne dla sdd.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub conf/
#fix locate mandir
sed -i 's/$(MANDIR)\/$(MANSECT)/share\/$(MANDIR)\/$(MANSECT)/' RULES/rules.man

MAKEPROG=gmake
export MAKEPROG
%{__make} \
	COPTS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INS_BASE=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AN-%{version}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/sdd.1*
%{_mandir}/man3/*.3*
%{_mandir}/man5/make*.5*
%lang(de) %{_mandir}/de/man1/sdd.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
