Summary:        Theme based on StarTrek LCARS console.
Summary(pl):    Temat bazuj±cy na konsoli komputerów z serialu StarTrek
Name:           mozilla-theme-LCARStrek
Version:        1.0.rc2
Release:        1
License:        GPL
Group:          X11/Applications/Networking
Source0:        http://downloads.mozdev.org/themes/LCARStrek10rc2.jar
Source1:        LCARStrek-installed-chrome.txt
URL:            http://www0.mozdev.org/themes/skins/lcarstrek.html
BuildRequires:  unzip
Requires:       mozilla >= 1.0
BuildRoot:      %{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome
%define		_realname	LCARStrek

%description
%description -l pl
Temat bazuj±cy na wygl±dzie konsol komputerów z serialu StarTrek.

%prep
%setup -q -c -T
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt |grep -v "LCARStrek" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
