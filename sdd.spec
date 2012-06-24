Summary:	disk dump and restore to and from tape or file
Summary(pl):	Narz�dzia do zrzut�w i odtwarzania dysku do/z ta�my lub pliku
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
speed. Timing & Statistics available at any time with SIGQUIT (^\).
Can seek on input and output. Fast null input. Fast null output.
Support for the RMT (Remote Tape Server) protocol makes remote I/O
fast and easy.

%description -l pl
sdd to zamiennik programu o nazwie "dd". sdd jest o wiele szybszy ni�
dd w przypadkach, kiedy rozmiar bloku wej�ciowego (ibs) nie jest r�wny
rozmiarowi bloku wyj�ciowego (obs). Statystyki s� bardziej zrozumia�e
od tych podawanych przez dd. Dost�pny jest pomiar czasu - opcja -time
wypisuje szybko�� transweru. Czas i statystyka s� dost�pne w ka�dej
chwili przez SIGQUIT (^\). Mo�e ustawia� pozycj� w pliku wej�ciowym i
wyj�ciowym; szybkie wczytywanie i zapis pustej zawarto�ci. Obs�uga
protoko�u RMT (Remote Tape Server) czyni zdalne wej�cie/wyj�cie
szybkim i �atwym.

%prep
%setup -q

%build
# TODO: CC and CFLAGS
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
