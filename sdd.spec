Summary:	disk dump and restore to and from tape or file
Summary(pl):	Narzêdzia do zrzutów i odtwarzania dysku do/z ta¶my lub pliku
Name:		sdd
Version:	1.52
Release:	0.1
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

%description -l pl
sdd to zamiennik programu o nazwie "dd". sdd jest o wiele szybszy ni¿
dd w przypadkach, kiedy rozmiar bloku wej¶ciowego (ibs) nie jest równy
rozmiarowi bloku wyj¶ciowego (obs). Statystyki s± bardziej zrozumia³e
od tych podawanych przez dd. Dostêpny jest pomiar czasu - opcja -time
wypisuje szybko¶æ transweru. Czas i statystyka s± dostêpne w ka¿dej
chwili przez SIGQUIT (^\). Mo¿e ustawiaæ pozycjê w pliku wej¶ciowym i
wyj¶ciowym; szybkie wczytywanie i zapis pustej zawarto¶ci. Obs³uga
protoko³u RMT (Remote Tape Server) czyni zdalne wej¶cie/wyj¶cie
szybkim i ³atwym.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub conf/
#fix locate mandir
sed -i 's/$(MANDIR)\/$(MANSECT)/share\/$(MANDIR)\/$(MANSECT)/' RULES/rules.man

MAKEPROG=gmake
export MAKEPROG
%{__make} COPTS="%{rpmcflags}" CC="%{__cc}"

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
%{_mandir}/man1/sdd.1.*
%lang(de) %{_mandir}/de/man1/sdd.1.*
