Summary:	Theme based on StarTrek LCARS console
Summary(pl):	Temat bazuj±cy na konsoli komputerów z serialu StarTrek
Name:		mozilla-theme-LCARStrek
%define		_realname	LCARStrek
Version:	1.0
%define	fver	%(echo %{version} | tr -d .)
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.hirsch.sth.ac.at/~robert/kairo.at/dl/%{_realname}%{fver}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://www.kairo.at/download/mozskins.html
BuildRequires:	unzip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Theme based on StarTrek LCARS console.

%description -l pl
Temat bazuj±cy na wygl±dzie konsol komputerów z serialu StarTrek.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%post 
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
