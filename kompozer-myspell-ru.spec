%define _enable_debug_packages %{nil}
%define debug_package          %{nil}
%define distsuffix edm

%define version 0.8
%define pre b3
%if %pre
%define release %mkrel -c %pre 6
%else
%define release %mkrel 2
%endif

%define _mozillaextpath /usr/lib/kompozer/extensions

Summary: Russian dictionary for Kompozer
Summary(ru): Русский словарь идля Kompozer
Name: kompozer-myspell-ru
Version:        %{version}
Release:        %{release}
License: GPLv2+
Group: Networking/WWW
URL: http://kompozer.net/download.php
Source: http://kompozer.sourceforge.net/l10n/myspell/myspell-dict.ru.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: kompozer
Obsoletes: kompozer-myspell-ru < %{version}-%{release}
Provides: kompozer-myspell-ru = %{version}-%{release}
BuildRequires: firefox-devel

%description
Russian dictionary for Kompozer %{version}%{pre}

%description -l ru
Русский словарь для Kompozer %{version}%{pre}

%prep
%setup -q -c -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %{_libdir}/kompozer
%{_mozillaextpath}


