%define		php_min_version 5.2.4
%include	/usr/lib/rpm/macros.php
Summary:	A powerful PHP framework with a very small footprint
Name:		CodeIgniter
Version:	2.0.2
Release:	0.7
License:	other
Group:		Development/Languages/PHP
Source0:	http://www.codeigniter.com/download_files/reactor/%{name}_%{version}.zip
# Source0-md5:	e75bab8cf27d2fb2483c5bb61b85a524
Source1:	INSTALL-PLD.txt
Source2:	codeigniter-install
URL:		http://www.kohanaframework.org/
BuildRequires:	rpm-php-pearprov >= 4.3
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-ctype
Requires:	php-date
Requires:	php-hash
Requires:	php-mbstring
Requires:	php-mysql
Requires:	php-pcre
Requires:	php-session
Requires:	php-simplexml
Requires:	php-spl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
CodeIgniter is a powerful PHP framework with a very small footprint,
built for PHP coders who need a simple and elegant toolkit to create
full-featured web applications. If you're a developer who lives in the
real world of shared hosting accounts and clients with deadlines, and
if you're tired of ponderously large and thoroughly undocumented
frameworks.

%prep
%setup -q -n %{name}_%{version}
%{__sed} -i 's,\$application_folder.*=.*,$application_folder = "PLEASE SET TO CORRECT PATH";,' index.php
%{__sed} -i '59 s,\$system_path.*=.*,$system_path = "%{_datadir}/CodeIgniter/system"\;, ' index.php

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_appdir}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

cp -r index.php application system $RPM_BUILD_ROOT%{_appdir}
cp -r user_guide/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner -e %{name} <<-EOF
Please read INSTALL-PLD.txt to know how can use the users the installed CodeIgniter!
EOF

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/codeigniter-install
%{_appdir}
